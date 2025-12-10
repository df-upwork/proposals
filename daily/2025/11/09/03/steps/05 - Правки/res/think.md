1.  Правка для устранения `𐒌(1)`.

Заменить предложение:

```markdown
The FDA requires Tool Qualification or Computer Software Assurance (CSA) for supporting tools.
```

На следующий текст:

```markdown
The FDA mandates the validation of computerized systems that create, modify, maintain, or transmit GxP data, as stipulated in 21 CFR 11.10(a) and relevant predicate rules.
When an iPaaS solution (e.g., Mulesoft, Boomi, or ADF) is used to handle GxP data, it is considered part of the GxP computerized system and requires appropriate validation, not merely qualification as a supporting tool.
The FDA’s guidance on Computer Software Assurance (CSA) provides a modern, risk-based framework to achieve this validation, but CSA itself is not the requirement.
```

2.  Правка для устранения `𐒌(2)`.

Заменить предложение:

```markdown
«The entire system must be validated... as well as interactions between software packages». This is an exact description of iPaaS.
```

На следующий текст:

```markdown
The regulatory principle that «The entire system must be validated... as well as interactions between software packages» directly applies to the implementation and use of iPaaS platforms within a GxP environment, as they are the technology used to realize these interactions.
```

3.  Правка для устранения `𐒌(3)`.

Заменить предложение:

```markdown
Any GxP system, including an integration platform, must undergo a full cycle of `IQ` / `OQ` / `PQ`.
```

На следующий текст:

```markdown
While GxP systems, including integration platforms, must be validated, the assertion that a «full cycle of `IQ` / `OQ` / `PQ`» must be executed solely by the regulated company is outdated for cloud-based (SaaS/PaaS) solutions.
Modern risk-based approaches, such as those outlined in GAMP 5 2nd Edition and the FDA's CSA guidance, emphasize leveraging the supplier's qualification activities.
The supplier typically provides evidence for the `IQ` of the infrastructure and a significant portion of the `OQ` for the platform, provided a proper supplier assessment has been conducted.
The regulated company then focuses its validation efforts on the intended use, configuration, and `PQ` (Performance Qualification), adopting a least-burdensome approach commensurate with the risk.
```