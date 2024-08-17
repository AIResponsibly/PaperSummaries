# REFCHECKER: Reference-based Fine-grained Hallucination Checker and Benchmark for Large Language Models
- **Published**: arXiv 2024
- **Link**: [Paper Link](https://arxiv.org/abs/2405.14486)
- **Summary**: REFCHECKER is a framework designed to detect fine-grained hallucinations in large language model responses using a novel claim-triplet analysis.

### Problem 
- LLMs often generate hallucinated content.
- Challenges in detecting hallucinations accurately, especially in long and complex responses.
- three different settings:
   - **Zero Context**: LLM responds using only its internal knowledge.
  - **Noisy Context**: LLM uses external information that may include noise.
  - **Accurate Context**: LLM responds based on clear, noise-free input.
- Need for appropriate granularity in checking units.

### Contributions
- **Claim-triplet formulation**: 
  - More granular and accurate detection of hallucinations.
  - Outperforms existing methods by up to 9 points in accuracy.
- **Comprehensive benchmark**:
  - Diverse tasks and domains.
  - 11,000 manually annotated claim-triplets across 7 LLMs.
- **Automatic checking framework**:
  - Supports both proprietary and open-source models.
  - Improves consistency by 19-26 points over prior methods.

### Methodf
- **Overview**:
  - Framework consists of an extractor and a checker.
  - Extracts claim-triplets from LLM responses and checks against references.
- **Datasets**:
  - Curated a benchmark with Zero, Noisy, and Accurate Contexts.
  - Includes data from tasks like QA, summarization, and information extraction.
- Process to detect hallucination in each context:
  - **Zero Context**
    - **Context**: LLM uses only its internal knowledge.
    - **Hallucination Detection**:
      - Compare the response to a trusted reference (e.g., Wikipedia).
      - Identify contradictions or unsupported details.
      - Flag these as hallucinations.
  
  - **Noisy Context**
    - **Context**: LLM uses external information, which may include noise e.g. from the RAG.
    - **Hallucination Detection**:
      - Compare the response to the provided noisy context.
      - Check for contradictions in the information.
      - Flag unsupported details as hallucinations.
  
  - **Accurate Context**
    - **Context**: LLM uses clear and accurate input.
    - **Hallucination Detection**:
      - Compare the response to the accurate input.
      - Identify deviations from the input.
      - Flag any incorrect or unsupported information as hallucinations.
  
- **Github**: [https://github.com/amazon-science/RefChecker](https://github.com/amazon-science/RefChecker)

### Result
- **Performance**:
  - REFCHECKER shows a 4-9 point improvement in hallucination detection over other methods.
  - Strong alignment with human judgments.
- **Checker Configurations**:
  - Best performance with a combination of proprietary and open-source models.
  
### Limitations and Assumptions
- **Claim-triplet approach**:
  - May be restrictive and not cover all important semantics.
  - Primarily focuses on plain text, with potential future extensions to other formats.
  
### Future Work
- Explore enhancements for claim-triplet flexibility.
- Improve checkers for better accuracy in diverse contexts.
- Develop better source attribution for explainability.

### Conclusion
- **REFCHECKER**:
  - Provides a more granular and effective approach to hallucination detection.
  - Outperforms prior methods and closely aligns with human evaluations.

### Reference
- Xiangkun Hu et al., "REFCHECKER: Reference-based Fine-grained Hallucination Checker and Benchmark for Large Language Models", arXiv 2024.
