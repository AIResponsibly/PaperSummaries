# Patchscopes: A Unifying Framework for Inspecting Hidden Representations of Language Models
- **Published**: International Conference on Machine Learning (ICML) 2024
- **Link**: [Patchscopes Framework](https://pair-code.github.io/interpretability/patchscopes)

### Problem
- Understanding hidden representations in Large Language Models (LLMs).
- limitations existing interpretability methods:
  - Limited expressivity and robustness across layers.
  - Difficulty in inspecting early layers of LLMs.
  - Reliance on training data for probing hidden states.

### Contributions
- Introduces **Patchscopes**, a modular framework for decoding information from LLMs' hidden representations.
- Many existing interpretability methods can be viewed as specific instances of Patchscopes.
- Introduces new configurations of Patchscopes that are:
  - More expressive.
  - Robust across layers.
  - Free from training data constraints.
- Provides novel applications, such as correcting multi-hop reasoning errors in LLMs.
  - Multi-hop reasoning errors happen when a model handles steps correctly but fails to combine them, leading to incorrect conclusions.


### Method
- **Patchscopes Framework**: Involves "patching" hidden representations into a separate inference pass to decode specific information.
  - patching involves:
     - taking a hidden representation (a snapshot of the model's internal state at a particular layer and token) from one model or prompt,
     - and inserting (or "patching") it into a different inference process.
  - Allows designing various inspection tools by configuring target prompts, models, and transformations.
  - Experiments conducted on multiple LLMs including LLaMA2, Vicuna, GPT-J, and Pythia.
- **Patching process**
  - **Source Model/Prompt**: The model is run on an initial input (the source prompt) to generate hidden states across different layers.

  - **Target Model/Prompt**: A separate model or prompt (the target prompt) is set up to encourage the LLM to "translate" or reveal the specific information encoded in the patched hidden state.

  - **Patching Process**: The hidden state from the source model at a specific layer and token position is patched into the target model or prompt, replacing the corresponding hidden state in the target.

  - **Decoding Information**: The patched model is then executed to observe how the hidden state influences the final output, revealing what information was encoded in that state.

- **Datasets Used**: 
  - Multiple commonsense and factual reasoning tasks.
  - WikiText-103 for contextual sentence sampling.

### Result
- Improved decoding of next-token predictions.
- Outperformed traditional probing methods in attribute extraction.
- Enhanced understanding of entity resolution in early layers.
- Achieved higher accuracy in correcting multi-hop reasoning errors.

### Future Work
- Explore effectiveness of different target prompts.
- Investigate cross-model patching across different architectures.
- Apply Patchscopes to different domains and modalities.

### Conclusion
- Patchscopes provides a powerful and flexible framework for inspecting LLMs.
- It unifies prior interpretability methods while introducing more effective tools and new possibilities.

### Reference
- Ghandeharioun, A., Caciularu, A., Pearce, A., Dixon, L., & Geva, M. (2024). Patchscopes: A Unifying Framework for Inspecting Hidden Representations of Language Models. *Proceedings of the 41st International Conference on Machine Learning*.
