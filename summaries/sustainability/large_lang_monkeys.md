# Large Language Monkeys: Scaling Inference Compute with Repeated Sampling

- **Published**: ArXiv, July 2024
- **Link**: [ArXiv](https://arxiv.org/abs/2407.21787)
- **Summary**: This paper explores the concept of scaling inference compute by using repeated sampling from large language models (LLMs). It demonstrates that increasing the number of samples can significantly improve the model's ability to solve problems, particularly in coding and formal proof domains where solutions can be automatically verified.

## I. INTRODUCTION

- **Problem**: Traditional approaches limit LLMs to a single attempt at solving problems, which may not fully utilize the model's capabilities.
- **Objective**: Investigate the impact of repeated sampling on LLM performance across multiple tasks and models.
- **Key Findings**:
  - Coverage, or the fraction of problems solved, scales with the number of samples.
  - Repeated sampling can outperform single-attempt models, even when those models are stronger and more expensive.

### Contributions

- Demonstration of repeated sampling as an effective method for scaling inference compute.
- Identification of a log-linear relationship between coverage and the number of samples, suggesting potential scaling laws for inference.
- Highlighting the importance of improving methods for selecting the correct answer from multiple generated samples in domains without automatic verifiers.

## II. SCALING REPEATED SAMPLING

- **Tasks**: 
  - GSM8K, MATH, MiniF2F-MATH, CodeContests, SWE-bench Lite.
- **Key Metrics**: 
  - Coverage (fraction of problems solved by at least one generated sample).
  - Precision (ability to identify the correct solution from multiple samples).

## III. EXPERIMENTAL RESULTS

### 3.1 Repeated Sampling Across Tasks

- **Findings**:
  - Coverage improves smoothly as the number of samples increases across all tasks.
  - Weaker models, with enough samples, can outperform single attempts from stronger models.

### 3.2 Repeated Sampling Across Model Sizes and Families

- **Models**:
  - Llama-3, Gemma, Pythia (various sizes and configurations).
- **Findings**:
  - Smaller models show sharp coverage increases with repeated sampling.
  - Some models, like Pythia, may not benefit from repeated sampling on specific tasks due to limitations in their training data.

### 3.3 Cost-Effectiveness of Repeated Sampling

- **Analysis**:
  - Repeated sampling can be more cost-effective than using stronger, more expensive models.
  - FLOPs (Floating Point Operations) are used as a cost metric to evaluate efficiency.

## IV. PRECISION AND VERIFICATION

### 4.1 Common Verification Methods

- **Challenges**:
  - Methods like majority voting and reward model scoring do not scale effectively with the sample budget, plateauing in performance as sample numbers increase.

### 4.2 Verifiers in Software Tasks

- **Cautionary Examples**:
  - Flaky tests in SWE-bench Lite and false negatives in CodeContests highlight the limitations of current verification methods.
  
## V. DISCUSSION AND LIMITATIONS

- **Limitations**:
  - The study uses a simple version of repeated sampling without iterative improvements or learning from previous attempts.
  - Current sample diversity methods rely on token-level sampling, which could be enhanced by combining with other techniques.
  - Precision in identifying correct solutions remains a challenge, particularly in domains without automatic verifiers.

## VI. RELATED WORK

- **Topics Covered**:
  - Scaling inference compute, repeated sampling, scaling laws, and the impact of compute on LLM performance.

## VII. CONCLUSION

- **Summary**: Repeated sampling is an effective and cost-efficient method for scaling inference compute in LLMs, significantly improving task performance across a range of models and tasks.
- **Future Work**: Improve sample diversity, explore multi-turn interactions, and enhance verification methods to fully harness the benefits of repeated sampling.

## REFERENCES

Bradley Brown, Jordan Juravsky, Ryan Ehrlich, Ronald Clark, Quoc V. Le, Christopher Ré, Azalia Mirhoseini. "Large Language Monkeys: Scaling Inference Compute with Repeated Sampling," arXiv preprint arXiv:2407.21787, 2024.
