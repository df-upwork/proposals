#!/usr/bin/env python3
import argparse
import json
import os
import time
from typing import Optional, Dict, List, Union
import logging
import re
import anthropic

# Set up logging
# File handler - detailed debug logging
file_handler = logging.FileHandler('analysis_debug.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# Console handler - only important info
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter('%(message)s'))

# Set up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

class DomainAnalyzer:
    def __init__(self, api_key: str):
        self.client = anthropic.Client(api_key=api_key)
        self.metamodel_data = {}
        # Ensure output directory exists
        os.makedirs("output", exist_ok=True)
        # Load existing metamodel if it exists
        self._load_existing_metamodel()

    def _load_existing_metamodel(self):
        """Load existing metamodel if it exists."""
        try:
            # Try to load from unknown first
            filename = os.path.join("output", "unknown_organization_metamodel.json")
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as f:
                    self.metamodel_data = json.load(f)
                logger.info(f"Loaded existing metamodel from {filename}")
        except Exception as e:
            logger.warning(f"Could not load existing metamodel: {str(e)}")

    def _get_metamodel_filename(self) -> str:
        """Get appropriate metamodel filename based on current data."""
        org_name = "unknown_organization"
        if "Organization" in self.metamodel_data:
            org_data = self.metamodel_data["Organization"]
            if isinstance(org_data, dict) and org_data.get("Title", "N/A") not in ["N/A", ""]:
                org_name = org_data["Title"].lower().replace(' ', '_')
                # Remove special characters except underscore
                org_name = re.sub(r'[^a-z0-9_]', '', org_name)
        
        return os.path.join("output", f"{org_name}_metamodel.json")

    def _chunk_document(self, content: str, max_chunk_size: int = 12000) -> list:
        """Split document into manageable chunks."""
        paragraphs = content.split('\n\n')
        chunks = []
        current_chunk = []
        current_size = 0

        for para in paragraphs:
            para_size = len(para)
            if current_size + para_size > max_chunk_size and current_chunk:
                chunks.append('\n\n'.join(current_chunk))
                current_chunk = []
                current_size = 0
            current_chunk.append(para)
            current_size += para_size

        if current_chunk:
            chunks.append('\n\n'.join(current_chunk))

        return chunks

    def _save_metamodel(self, metamodel: Dict):
        """Save current state of metamodel to file with better error handling."""
        try:
            # Update internal state
            self.metamodel_data.update(metamodel)
            
            # Get filename
            filename = self._get_metamodel_filename()
            
            # Create temp file first
            temp_filename = filename + '.tmp'
            with open(temp_filename, 'w', encoding='utf-8') as f:
                json.dump(self.metamodel_data, f, indent=2, ensure_ascii=False)
                f.write('\n')
            
            # Rename temp file to final file
            if os.path.exists(filename):
                os.replace(temp_filename, filename)
            else:
                os.rename(temp_filename, filename)
            
            logger.debug(f"Saved metamodel to {filename}")
            
        except Exception as e:
            logger.error(f"Error saving metamodel: {str(e)}")

    def _process_response(self, response_text: str) -> Union[Dict, List[Dict]]:
        """Process and validate response text into JSON."""
        try:
            # Clean up response text
            response_text = response_text.strip()
            
            # Extract JSON if wrapped in markdown
            if "```json" in response_text:
                response_text = response_text.split("```json")[1].split("```")[0].strip()
            elif "```" in response_text:
                response_text = response_text.split("```")[1].split("```")[0].strip()

            # Remove any "Here is a JSON..." prefix text
            if "{" in response_text:
                response_text = response_text[response_text.find("{"):]
            elif "[" in response_text:
                response_text = response_text[response_text.find("["):]
            
            # Parse JSON
            return json.loads(response_text)
            
        except json.JSONDecodeError as e:
            logger.error(f"JSON parsing error: {str(e)}")
            logger.error(f"Problematic response text: {response_text}")
            return {} if "[" not in response_text else []

    def _build_multi_instance_prompt(self, prompt: Dict, is_multi_instance: bool) -> str:
        """Build system prompt with awareness of multiple instances."""
        base_prompt = f"""You are analyzing an organizational document for {prompt['type']}.

Task: {prompt['task']}

Definition: {prompt['definition']['text']}

Extract information according to these attributes:
{json.dumps(prompt['extractionAndOutput']['attributes'], indent=2)}

Guidelines:
{json.dumps(prompt['guidelines'], indent=2)}"""

        if is_multi_instance:
            base_prompt += """

Special Instructions:
1. Return a LIST of JSON objects, one for each distinct instance found.
2. Each instance should contain all the specified attributes.
3. If no instances are found in this section, return an empty list [].
4. Avoid duplicating instances that refer to the same entity.
5. Preserve specific details for each instance."""
        else:
            base_prompt += """

Special Instructions:
1. Return a SINGLE JSON object with the specified attributes.
2. Use "N/A" for attributes where no information is found.
3. Be thorough in extracting information - look for both explicit and implicit mentions."""

        return base_prompt

    def _process_chunk_with_instances(
        self, 
        chunk: str, 
        prompt: Dict, 
        system_prompt: str,
        previous_results: Optional[Dict],
        is_multi_instance: bool
    ) -> Union[Dict, List[Dict]]:
        """Process a document chunk with support for multiple instances."""
        previous_context = ""
        if previous_results:
            previous_context = f"\n\nReference previous analysis if relevant:\n{json.dumps(previous_results, indent=2)}"

        user_message = f"""Analyze this document section and extract the requested information.{previous_context}

Document section:
{chunk}

Return {"a LIST of JSON objects for each instance found" if is_multi_instance else "a SINGLE JSON object"}."""

        max_retries = 3
        base_delay = 2
        
        for attempt in range(max_retries):
            try:
                response = self.client.messages.create(
                    model="claude-3-sonnet-20240229",
                    max_tokens=4096,
                    temperature=0,
                    system=system_prompt,
                    messages=[{"role": "user", "content": user_message}]
                )
                
                result = self._process_response(response.content[0].text)
                
                # Ensure result is in the correct format
                if is_multi_instance and not isinstance(result, list):
                    result = [result] if result else []
                elif not is_multi_instance and isinstance(result, list):
                    result = result[0] if result else {}
                    
                return result
                
            except anthropic.RateLimitError:
                if attempt < max_retries - 1:
                    delay = base_delay * (2 ** attempt)
                    logger.debug(f"Rate limit hit, waiting {delay} seconds...")
                    print(f"  Rate limit reached. Waiting {delay} seconds...", end="\r")
                    time.sleep(delay)
                    print("                                                ", end="\r")
                else:
                    raise

    def _merge_instances(self, existing_results: List[Dict], new_results: List[Dict]):
        """Merge new instances while avoiding duplicates."""
        for new_instance in new_results:
            # Skip empty or invalid instances
            if not new_instance or all(v == "N/A" for v in new_instance.values()):
                continue
                
            # Check if this instance is unique
            is_unique = True
            for existing in existing_results:
                if self._are_instances_similar(existing, new_instance):
                    # Merge any new information into existing instance
                    self._update_instance(existing, new_instance)
                    is_unique = False
                    break
                    
            if is_unique:
                existing_results.append(new_instance)

    def _are_instances_similar(self, instance1: Dict, instance2: Dict) -> bool:
        """Determine if two instances likely refer to the same entity."""
        # Compare title/name fields first if they exist
        title_fields = ['Title', 'Name', 'ID']
        for field in title_fields:
            if field in instance1 and field in instance2:
                if instance1[field] != "N/A" and instance2[field] != "N/A":
                    return instance1[field].lower() == instance2[field].lower()
        
        # Fall back to comparing significant fields
        significant_fields = set(instance1.keys()) & set(instance2.keys())
        matches = 0
        total_fields = 0
        
        for field in significant_fields:
            if instance1[field] != "N/A" and instance2[field] != "N/A":
                total_fields += 1
                if instance1[field] == instance2[field]:
                    matches += 1
        
        # Consider similar if high percentage of matching fields
        return total_fields > 0 and (matches / total_fields) > 0.8

    def _update_instance(self, existing: Dict, new_instance: Dict):
        """Update existing instance with new information."""
        for key, new_value in new_instance.items():
            if key in existing:
                if new_value != "N/A" and new_value != existing[key]:
                    if existing[key] == "N/A":
                        existing[key] = new_value
                    else:
                        # Combine unique information
                        existing[key] = '; '.join(set(filter(None, [
                            existing[key],
                            new_value
                        ])))

    def _merge_single_instance(self, existing_results: Dict, new_results: Dict):
        """Merge new results into existing single instance results."""
        for key, new_value in new_results.items():
            if key in existing_results:
                if new_value != "N/A" and new_value != existing_results[key]:
                    if existing_results[key] == "N/A":
                        existing_results[key] = new_value
                    else:
                        # Combine unique information
                        existing_results[key] = '; '.join(set(filter(None, [
                            existing_results[key],
                            new_value
                        ])))

    def analyze_domain(self, document_content: str, prompt: Dict, previous_results: Optional[Dict] = None) -> Dict:
        """Analyze document for a specific domain with support for multiple instances."""
        logger.debug(f"Processing domain: {prompt['type']}")
        print(f"\nAnalyzing {prompt['type']}...")
        
        # Check if this domain should collect multiple instances
        is_multi_instance = "instance" in prompt['extractionAndOutput']['instructions'].lower()
        
        if is_multi_instance:
            # Initialize as a list if we're collecting multiple instances
            domain_results = []
            
            # If we have existing results, start with those
            if prompt['type'] in self.metamodel_data:
                existing_data = self.metamodel_data[prompt['type']]
                if isinstance(existing_data, list):
                    domain_results = existing_data
                else:
                    # Convert existing single instance to list
                    domain_results = [existing_data] if any(v != "N/A" for v in existing_data.values()) else []
        else:
            # Single instance initialization
            domain_results = {attr: "N/A" for attr in prompt['extractionAndOutput']['attributes'].keys()}
            if prompt['type'] in self.metamodel_data:
                domain_results.update(self.metamodel_data[prompt['type']])

        # Build system prompt with multi-instance awareness
        system_prompt = self._build_multi_instance_prompt(prompt, is_multi_instance)

        chunks = self._chunk_document(document_content)
        logger.debug(f"Split document into {len(chunks)} chunks for {prompt['type']}")

        for i, chunk in enumerate(chunks, 1):
            logger.debug(f"Processing chunk {i}/{len(chunks)} for {prompt['type']}")
            print(f"  Processing part {i} of {len(chunks)}...", end="\r")
            
            try:
                chunk_results = self._process_chunk_with_instances(
                    chunk, 
                    prompt, 
                    system_prompt, 
                    previous_results,
                    is_multi_instance
                )
                
                if is_multi_instance:
                    # Merge new instances with existing ones
                    self._merge_instances(domain_results, chunk_results)
                else:
                    # Update single instance
                    self._merge_single_instance(domain_results, chunk_results)
                    
            except Exception as e:
                logger.error(f"Error processing chunk {i} for {prompt['type']}: {str(e)}")
                continue

        # Save results
        self._save_metamodel({prompt['type']: domain_results})
        
        print(f"  Completed {prompt['type']}                ")
        return domain_results

    def process_all_domains(self, document_path: str, prompts_path: str) -> Dict:
        """Process all domains sequentially with improved metamodel handling."""
        try:
            # Load document and prompts
            with open(document_path, 'r', encoding='utf-8') as f:
                document_content = f.read()
            
            with open(prompts_path, 'r', encoding='utf-8') as f:
                prompts_data = json.load(f)
            
            # Process each domain in sequence
            previous_results = self.metamodel_data.copy()  # Start with existing data
            
            for prompt in prompts_data['prompts']:
                logger.debug(f"Starting analysis for domain: {prompt['type']}")
                
                try:
                    domain_results = self.analyze_domain(
                        document_content=document_content,
                        prompt=prompt,
                        previous_results=previous_results
                    )
                    
                    # Update previous results for next iteration
                    previous_results[prompt['type']] = domain_results
                    
                    logger.debug(f"Completed analysis for domain: {prompt['type']}")
                    
                except Exception as e:
                    logger.error(f"Error processing domain {prompt['type']}: {str(e)}")
                    continue
            
            return self.metamodel_data
            
        except Exception as e:
            logger.error(f"Error in domain processing: {str(e)}")
            raise

def main():
    parser = argparse.ArgumentParser(description="Multi-domain organizational document analyzer")
    parser.add_argument('document', help='Path to the document to analyze')
    parser.add_argument('--prompts', default='All_domain_prompts_short.json',
                      help='Path to the prompts JSON file')
    parser.add_argument('--api-key', required=True,
                      help='Anthropic API key')

    args = parser.parse_args()

    try:
        analyzer = DomainAnalyzer(api_key=args.api_key)
        metamodel = analyzer.process_all_domains(args.document, args.prompts)
        
        print("\nAnalysis complete. Results saved to metamodel file.")
        
    except Exception as e:
        logger.error(f"Error during analysis: {str(e)}")
        raise

if __name__ == "__main__":
    main()