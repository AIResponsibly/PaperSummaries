# Understanding the Reasoning Ability of Language Models From the Perspective of Reasoning Paths Aggregation
- **Published**: 41st International Conference on Machine Learning (ICML) 2024
- **Link**: [https://github.com/WANGXinyiLinda/LM_random_walk](https://github.com/WANGXinyiLinda/LM_random_walk)
- **Summary**: The paper investigates how pre-trained language models (LMs) perform reasoning tasks by aggregating indirect reasoning paths seen during pre-training.

### Problem
- Address how pre-training contributes to reasoning capability in LMs.
  - Reasoning tasks include logic reasoning on Knowlege Graphs (KGs) and chain-of-thought (CoT) reasoning.
- Investigate the aggregation of indirect reasoning paths as a potential explanation for LLM's reasoning capabilities. 

### Contributions
- Propose the hypothesis that LMs reason by aggregating indirect reasoning paths.
- Formalize reasoning paths as random walk paths on knowledge/reasoning graphs.
- Demonstrate that augmenting pre-training with random walk paths can improve multi-step reasoning performance.

### Method
- **Overview**: The method involves analyzing the contribution of pre-training data to LM reasoning, formalized as random walks on knowledge graphs.
  - **Related work on explianing LM's reasoning**
     - understanding Transformers’ reasoning capability by construction
     - post-hoc mechanistic explanations, i.e. explainability research after model was trained.
  - **GitHub**: [LM_random_walk](https://github.com/WANGXinyiLinda/LM_random_walk)
- **Datasets**:
  - Knowledge Graphs: Countries, UMLS, Kinship, NELL-995, FB15K-237
  - Chain-of-Thought: GSM8K, AQUA, SVAMP, StrategyQA, LogicalDeduction
- Evaluation
  - Evaluation was conducted on five datasets: GSM8K, AQUA, SVAMP, StrategyQA, and LogicalDeduction.
  - For each dataset, models were pre-trained on random walk data and then supervised fine-tuned.
  - Performance was compared to a supervised fine-tuning (SFT) baseline.
  - The effect of random walk path length was analyzed by plotting accuracy against path lengths.
  - Optimal path lengths varied by dataset, with AQUA and GSM8K peaking at length 10, and SVAMP peaking at length 5.
  - Ablation studies were performed on two hyperparameters:
      - the number of training steps on random walk paths (M)
      - and the number of clusters/nodes (K).
      - Optimal values were found to be 500 steps and 100 clusters for the datasets used.

### Result
- Improved reasoning accuracy with augmented pre-training
- Optimal random walk path lengths identified
- Effective utilization of unlabeled reasoning paths

### Limitations and Assumptions
- Noise in reasoning paths when the path length is too long
- Dependence on random walk path lengths for optimal performance

### Conclusion
- Aggregating reasoning paths from pre-training data is a valid explanation for LM reasoning abilities.
- The method shows potential for enhancing LM reasoning performance with pre-training data augmentation.

### Reference
- Wang, X., Amayuelas, A., Zhang, K., Pan, L., Chen, W., Wang, W. "Understanding the Reasoning Ability of Language Models From the Perspective of Reasoning Paths Aggregation." Proceedings of the 41st International Conference on Machine Learning, Vienna, Austria, 2024.
