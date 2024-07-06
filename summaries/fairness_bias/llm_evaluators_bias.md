# Benchmarking Cognitive Biases in Large Language Models as Evaluators

- **Published**: arXiv, 2023
- **Link**: [arXiv:2309.17012](https://arxiv.org/abs/2309.17012)
- **Summary**: This paper introduces COBBLER (COGNITIVE BIAS BENCHMARK FOR LLMS AS EVALUATORS), a benchmark for evaluating cognitive biases in LLMs used as evaluators.

### Problem

- LLMs are used as automatic evaluators.
- Potential biases in LLM evaluations are not well understood.
  - Egocentric bias: a model preference for its own responses.
  - Other biases: Order, Compassion, Salience, Bandwagon, Attentional.
- LLMs' evaluations often misalign with human preferences.

### Contributions

- Introduces COBBLER (COGNITIVE BIAS BENCHMARK FOR LLMS AS EVALUATORS) benchmark to evaluate cognitive biases in LLMs.
- Examines six cognitive biases in LLM evaluations.
- Evaluates 15 LLMs of various sizes for bias.
- Analyzes correlation between human and LLM preferences.

### Method

- 15 LLMs evaluated by other LLMs using pairwise preference ranking.
- Benchmarks from BIGBENCH and ELI5 datasets.
- COBBLER benchmark assesses six biases:
  - Egocentric, Order, Compassion, Salience, Bandwagon, Attentional.
- Ranks evaluated using Rank-Biased Overlap (RBO) for similarity to human preferences.
- [GitHub Implementation](https://minnesotanlp.github.io/cobbler)

### Result

- LLMs show strong biases in evaluations.
- Low alignment with human preferences (49.6% RBO).
- Larger models (100B+) less biased but still not unbiased.

### Limitations and Assumptions

- Focused on Q/A domain.
- Some models have low valid response rates.
- High computational cost.

### Future Work

- Explore de-biasing methods.
- Fine-tune models to reduce cognitive biases.

### Conclusion

- Most LLMs exhibit significant cognitive biases as evaluators.
- Current LLMs are not suitable for fair and reliable automatic evaluation.
- COBBLER provides a framework to measure and improve future LLM evaluators.

### Reference

- Koo, R., Lee, M., Raheja, V., Park, J. I., Kim, Z. M., & Kang, D. (2023). Benchmarking Cognitive Biases in Large Language Models as Evaluators. arXiv. <https://arxiv.org/abs/2309.17012>
