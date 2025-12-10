1) To diagnose past failures, Azure Data Factory provides the «Rerun» functionality on the «Monitor» tab.
This functionality allows to rerun the pipeline using the exact historical parameters and configuration (Snapshot) that were used during the failed run.
This is often the highest-priority method for verifying transient issues (e.g., network timeouts) or reproducing the failure.
I describe this step, along with log analysis, in Section 4 below.
However, if it is necessary to run the pipeline with new parameters (e.g., for testing fixes or processing new data), then it is necessary to understand its logic and input data requirements.
I describe this in Sections 7-10 below.
2) Your likely oversight is narrowing the scope of the failure investigation to the problematic pipeline.
In fact, a significant portion of pipeline failures is caused by external factors: infrastructure and security, especially in legacy environments.
In particular:
- Authentication and Authorization: expired credentials or keys in Linked Services, incorrect configuration of Managed Identity, lack of access to Azure Key Vault or target data stores.
- Network issues: configuration of firewalls (Azure Storage, SQL DB), VNet, Private Endpoints, blocking access.
- Integration Runtime (IR): issues with availability, configuration, or performance of Self-Hosted IR.

Ignoring external factors is a critical mistake when diagnosing failures in Azure Data Factory.
Analysis of external factors is the next highest-priority diagnostic step after log analysis.
I describe it in Section 5 below.

3) First and foremost, any such diagnosis must begin by determining the Source Control configuration and operational mode of Azure Data Factory.
Simply put, it is necessary to understand how code versions are managed and how the version on the «Author» canvas relates to the published version, which is used in production runs.
This is critically important for the correct diagnosis of historical failures (Section 3) and the analysis of the current logic (Section 5).
For this, it is necessary to check the Git configuration:
3.1) Navigate to the «Manage» tab on the left side panel.
3.2) Go to «Source control» → «Git configuration» or check for Git controls (e.g., the branch selector) on the top bar of ADF Studio.
3.3) Determine the ADF operating mode.
3.3.1) `Live Mode` (Authoring directly against the data factory service): If Git integration is not configured.
In this mode, changes on the «Author» canvas can be saved using the Save or Save all buttons.
These saved changes are available for «Debug» runs.
However, these changes are not activated for triggered runs until they are published directly to the Data Factory service using the «Publish all» button.
Only the published version is the version used in triggered runs.
3.3.2) `Git Mode` (e.g., Azure DevOps Git or GitHub): If the configuration points to a repository.
In this mode, changes on the «Author» canvas are saved to the selected Git branch (e.g., feature branch) using «Save» or «Save all».
These changes are not applied to the production service (and are not used in triggered runs) until they are published from the Collaboration branch.
4) Analysis of logs
4.1) Navigate to Azure Data Factory Studio.
4.2) Open the «Monitor» tab on the left side panel.
4.3) In the «Pipeline runs» section, review the list of previous runs of the target pipeline.
Use the filters by pipeline name («Pipeline name») and status (Status, e.g., «Failed») to find the runs of interest.
Ensure that triggered runs are analyzed.
Triggered» runs are production runs and always use the version of the pipeline that was published in the Azure Data Factory service at the time of the run.
This corresponds to the published version in `Live Mode` (point 3.3.1 above) or the version published from the Collaboration branch in `Git Mode` (point 3.3.2).
«Debug» runs use the current version of the pipeline on the «Author» canvas.
In `Git Mode` this is the version from the currently selected branch.
In `Live Mode` this is the current version on the canvas, which may contain unpublished changes.
4.4) Analyze the details of the failed run.
4.4.1) Click on the pipeline name in the list to navigate to the «Activity runs» list.
4.4.2) Identify the activity that failed.
4.4.3) Examine the detailed error message.
To do this, click on the icon in the «Error» column for this activity.
---
Due to Upwork's character limit for proposals, I have published the continuation of my analysis on my website: https://df.tips/t/2672
I have also attached the entire analysis here as a PDF document.
My GitHub profile: https://github.com/dmitrii-fediuk



