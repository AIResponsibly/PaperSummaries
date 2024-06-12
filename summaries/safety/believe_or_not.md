# To Believe or Not to Believe Your LLM
- **Published**: arXiv, 2024
- **Link**: [https://arxiv.org/abs/2406.02543](https://arxiv.org/abs/2406.02543)
- **Summary**: This paper explores uncertainty quantification in LLMs to detect hallucinations by distinguishing epistemic from aleatoric uncertainties using an information-theoretic metric.

### Problem
- Identifying unreliable LLM responses.
- Differentiating between epistemic and aleatoric uncertainties.
  - Epistemic uncertainty: Arises from lack of knowledge about the ground truth.
  - Aleatoric uncertainty: Stems from inherent randomness in the prediction.
- Existing uncertainty quantification methods fall short in multi-answer scenarios.

### Contributions
- Derived an information-theoretic metric for epistemic uncertainty.
- Developed a method using iterative prompting.
- Demonstrates advantages through a series of experiments.

### Method
- Utilizes iterative prompting based on previous responses.
- Computes epistemic uncertainty separately from aleatoric.
- Detects hallucinations using a mutual information-based metric.

### Result
- Effective detection of hallucinations in single and multi-answer scenarios.
- Outperforms traditional uncertainty quantification methods.
- Validated through extensive experiments.

### Limitations and Assumptions
- Assumption of ground truth independence.

### Conclusion
- Provides a robust technique for quantifying uncertainty in LLMs.
- Enhances reliability by identifying high epistemic uncertainty.

### Reference
- Yasin Abbasi Yadkori, Ilja Kuzborskij, András György, Csaba Szepesvári. "To Believe or Not to Believe Your LLM," arXiv preprint arXiv:2406.02543, 2024.
