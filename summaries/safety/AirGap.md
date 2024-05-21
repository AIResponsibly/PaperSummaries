# Air Gap: Protecting Privacy-Conscious Conversational Agents
- **Published**: arXiv 2024
- **Link**: [Air Gap: Protecting Privacy-Conscious Conversational Agents](https://arxiv.org/abs/2405.05175)
- **Summary**: Proposes AirGapAgent to prevent data leakage from LLMs, ensuring privacy in adversarial contexts.

### Problem 
- Privacy concerns with LLM-based conversational agents managing sensitive data.

### Contributions
- Introduces AirGapAgent to minimize data access.
    - "by restricting the agent’s access to only the data necessary for a specific task"
- Demonstrates effectiveness against context hijacking attacks.

### Method
- Utilizes two LLMs: a data minimizer and a conversational model.
- Minimized data access based on user-defined context.

### Result
- AirGapAgent achieves up to 97% privacy protection.
- Maintains core functionality of agents.

### Limitations and Assumptions
- Evaluated on synthetic data, real-world applicability needs verification.

## Conclusions
- Proposed threat model and context hijacking attack inspired by contextual integrity.
- Introduced air gap-based mitigation separating user data from adversaries.
- Evaluation: on synthetic profiles, achieving ~90% utility and privacy.

## Future Work
- Improve agent performance across diverse tasks, models, and datasets.
- Explore smaller, dedicated models for minimizer to enhance efficiency and privacy.
- Develop benchmarks to measure alignment with real user expectations.


### Reference
- Bagdasaryan, E., Yi, R., Ghalebikesabi, S., Kairouz, P., Gruteser, M., Oh, S., Balle, B., & Ramage, D. (2024). Air Gap: Protecting Privacy-Conscious Conversational Agents. arXiv preprint arXiv:2405.05175.
