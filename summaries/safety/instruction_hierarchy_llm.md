# The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions
- **Published**: arXiv, 2024
- **Link**: [The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions](https://arxiv.org/abs/2404.13208)
- **Summary**: This paper from OpenAI introduces an instruction hierarchy to train LLMs to prioritize privileged instructions(system messages) over lower-level ones (user messages and third-party inputs), enhancing their robustness against adversaries.

### Problem
- Modern LLMs are vulnerable to prompt injections, jailbreaks, and other attacks that exploit the lack of instruction prioritization.

### Contributions
- The paper proposes an instruction hierarchy to teach LLMs to prioritize instructions from trusted sources (system messages) over those from less trusted sources (user messages and third-party inputs).

### Method
- The method involves synthetic data generation and context distillation to create training examples where LLMs learn to ignore lower-privileged, potentially harmful instructions.
- The approach includes generating aligned (compliant) and misaligned (non-compliant) instruction examples to fine-tune models like GPT-3.5 Turbo using supervised fine-tuning and reinforcement learning from human feedback (RLHF).

### Result
- The trained LLMs exhibit up to 63% improved robustness against various attacks 
- They generalize well to unseen attacks
  - though some over-refusal behavior is noted.

### Limitations and Assumptions
- The current method is focused on text inputs, and further research is needed to extend this hierarchy to other modalities like images or audio.

### Conclusion
- The instruction hierarchy boosts LLM safety against prompt injection attacks.
- Future work involves refining instructions and extending to multi-modal inputs.

### Reference
- Wallace, E., Xiao, K., Leike, R., Weng, L., Heidecke, J., & Beutel, A. (2024). The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions. arXiv preprint arXiv:2404.13208.
