# Graph of Thoughts: Solving Elaborate Problems with Large Language Models

- **Published**: arXiv, 2024
- **Link**: [https://arxiv.org/abs/2308.09687](https://arxiv.org/abs/2308.09687)
- **Summary**: This paper introduces the Graph of Thoughts (GoT) framework, enhancing the reasoning capabilities of large language models by structuring their thought processes as directed graphs.

### Problem

- Enhancing reasoning capabilities of large language models (LLMs).
- Limitations of existing prompting techniques like Chain-of-Thought (CoT) and Tree-of-Thought (ToT).
- Need for more complex and interconnected reasoning patterns.

### Contributions

- Propose Graph of Thoughts (GoT) for networked reasoning.
- Design a modular architecture for implementing GoT.
- Illustrate use cases and evaluate the effectiveness of GoT.
- Compare GoT's performance with existing prompting techniques.

### Method

- **GoT Framework**:
  - **Reasoning Process**: Modeled as a directed graph \( G = (V, E) \) where vertices \( V \) are LLM thoughts and edges \( E \) represent dependencies.
  - **Thought Transformations**: Includes aggregation (combining thoughts), generation (producing new thoughts from existing ones), and refinement (enhancing thoughts).
  - **Scoring & Ranking**: Thoughts are evaluated using a scoring function \( E(v, G, p_\theta) \) and ranked using a ranking function \( R(G, p_\theta, h) \).
  - **System Architecture**:
    - **Prompter**: Prepares messages for the LLM.
    - **Parser**: Extracts information from LLM thoughts.
    - **Scoring Module**: Validates and scores thoughts.
    - **Controller**: Manages the reasoning process, applying transformations and deciding the next steps.
    - **Graph of Operations (GoO)**: Specifies the graph decomposition and transformations.
    - **Graph Reasoning State (GRS)**: Maintains the history and state of thoughts.
- **Implementation**: Provided for various use cases such as sorting, keyword counting, set operations, and document merging.
- **Dataset**: Experiments primarily conducted using GPT-3.5, with some comparisons to LLaMA-2.

### Result

- **Sorting**: 62% higher quality, 31% cost reduction over ToT.
- **Set Operations**: Consistent quality improvement.
- **Keyword Counting**: Improved aggregation of results.
- **Document Merging**: Effective handling of complex merging tasks.

### Limitations and Assumptions

- Assumes the effectiveness of graph-based transformations in reasoning tasks.
- Primarily focused on GPT-3.5 due to budget constraints.

### Future Work

- Extend GoT with new thought transformations.
- Experiment with other LLM models like GPT-4.

### Conclusion

- GoT framework effectively enhances LLM reasoning by modeling thoughts as a graph.
- Demonstrates significant improvements over CoT and ToT in various tasks.
- Promising step towards more advanced and human-like LLM reasoning processes.

### Reference

- Maciej Besta, Nils Blach, Ales Kubicek, Robert Gerstenberger, Michał Podstawski, Lukas Gianinazzi, Joanna Gajda, Tomasz Lehmann, Hubert Niewiadomski, Piotr Nyczyk, Torsten Hoefler. "Graph of Thoughts: Solving Elaborate Problems with Large Language Models." arXiv preprint arXiv:2308.09687 (2024).
