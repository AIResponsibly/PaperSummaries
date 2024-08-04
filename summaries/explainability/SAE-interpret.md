# Sparse Autoencoders Find Highly Interpretable Features in Language Models
- **Published**: arXiv, 2023
- **Link**: [arXiv:2309.08600](https://arxiv.org/abs/2309.08600)
- **Summary**: This paper uses sparse autoencoders to extract interpretable features from language models, addressing polysemanticity in neural networks.

### Problem
- Neural networks often have **polysemantic neurons**.
  - **Polysemantic neurons**: Neurons that respond to multiple unrelated concepts.
- **Superposition** causes overcomplete feature representation.
  - **Superposition**: A state where features overlap, making individual feature interpretation challenging.
- One hypothesised cause of polysemanticity is superposition.

### Contributions
- Propose **sparse autoencoders (SAE)** for extracting interpretable features.
  - **SAE**: A type of neural network that learns sparse representations.
- Demonstrate improved interpretability using autoencoders over other methods.
- Identify specific features influencing model behaviors.

### Method
- Use sparse autoencoders with a sparsity penalty to learn feature dictionaries.
- Apply the method to language models like Pythia-70M.
- **Features**: Specific learned patterns influencing model outputs.

### Result
- Improved feature interpretability.
- Finer localization of features influencing behaviors.
- Sparse features more monosemantic.

### Limitations and Assumptions
- Not all information captured; loss of information noted.

### Conclusion
- Sparse autoencoders can disentangle features, enhancing transparency and model understanding.

### Reference
- Cunningham, H., Ewart, A., Riggs, L., et al. "Sparse Autoencoders Find Highly Interpretable Features in Language Models." arXiv, 2023.
