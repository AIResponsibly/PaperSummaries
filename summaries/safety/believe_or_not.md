# To Believe or Not to Believe Your LLM
- **Published**: arXiv, 2024
- **Link**: [https://arxiv.org/abs/2406.02543](https://arxiv.org/abs/2406.02543)
- **Summary**: This paper explores uncertainty quantification in LLMs to detect hallucinations by distinguishing epistemic from aleatoric uncertainties using an information-theoretic metric.

### Problem
- Identifying unreliable LLM responses.
- Differentiating between epistemic and aleatoric uncertainties.
  - Epistemic uncertainty: Arises from lack of knowledge about the ground truth.
  - Aleatoric uncertainty: Stems from inherent randomness in the prediction.
- Improving hallucination detection in LLMs.

### Contributions
- Derived an information-theoretic metric for epistemic uncertainty.
- Developed a method using iterative prompting.
- Demonstrated detection of hallucinations in LLM responses.
- Shed light on how probabilities can be amplified through iterative prompting.

### Method
- Utilizes iterative prompting based on previous responses.
- Computes epistemic uncertainty separately from aleatoric.
- Detects hallucinations using a mutual information-based metric.

### Result
- Effective detection of hallucinations in single and multi-answer scenarios.
- Outperforms traditional uncertainty quantification methods.
- Validated through extensive experiments.

### Limitations and Assumptions
- "We make the following assumption about the ground truth, which states that multiple responses to the same question drawn according to the ground truth are independent from each other: Assumption 4.1 (Ground truth independence assumption)."


### Conclusion
- Provides a robust technique for quantifying uncertainty in LLMs.
- Enhances reliability by identifying high epistemic uncertainty.

### Reference
- Yasin Abbasi Yadkori, Ilja Kuzborskij, András György, Csaba Szepesvári. "To Believe or Not to Believe Your LLM," arXiv preprint arXiv:2406.02543, 2024.
