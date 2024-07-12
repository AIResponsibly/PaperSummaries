# Tree of Thoughts: Deliberate Problem Solving with Large Language Models

- **Published**: NeurIPS 2023
- **Link**: [GitHub Repository](https://github.com/princeton-nlp/tree-of-thought-llm)
- **Summary**: The paper introduces the Tree of Thoughts (ToT) framework, enhancing the problem-solving abilities of large language models by enabling exploration and evaluation of multiple reasoning paths.

### Problem

- Existing language models are limited to token-level, left-to-right decision-making.
- They struggle with tasks requiring exploration, strategic lookahead, or significant initial decisions.
- Need for a more deliberate and flexible problem-solving process.

### Contributions

- Introduces the Tree of Thoughts (ToT) framework for language model inference.
- Generalizes over the Chain of Thought approach to enable exploration of multiple reasoning paths.
- Allows language models to perform deliberate decision-making with self-evaluation and backtracking.
- Demonstrates significant performance improvements on tasks requiring planning and search.

### Method

- **Framework**: ToT frames problem-solving as a tree search where nodes represent partial solutions.
- **Steps**: Thought decomposition, generation of potential thoughts, heuristic evaluation of states, and selection of a search algorithm.
- **Tasks**: Tested on Game of 24, Creative Writing, and Mini Crosswords.
- **Implementation**: Used breadth-first search (BFS) and depth-first search (DFS) for systematic exploration.

### Result

- **Game of 24**: 74% success rate with ToT vs. 4% with Chain of Thought.
- **Creative Writing**: Higher coherency scores with ToT compared to baseline methods.
- **Mini Crosswords**: Significant improvement in solving ability with ToT.

### Limitations and Assumptions

- Deliberate search like ToT might be unnecessary for many tasks where GPT-4 already performs well.
- This work explores only three relatively simple tasks challenging GPT-4.
- ToT requires more resources (e.g., GPT-4 API cost) than sampling methods to improve task performance.
- The focus is on using an off-the-shelf LM, not fine-tuning.
  
### Future Directions

- Fine-tune LMs using ToT-style high-level counterfactual decision-making to enhance problem-solving capabilities.
- Reduce resource costs through ongoing open-source efforts.
- Explore more advanced search algorithms like A* and MCTS.

### Conclusion

- Calls for a better search and planning abilities incorporated with LMs.
- ToT  improves the interpretability of model decisions and the opportunity for human alignment
  - as the resulting representations are readable, high-level language reasoning instead of implicit, low-level token values.

- ToT significantly enhances the problem-solving capabilities of large language models by introducing a flexible, deliberative reasoning process.
- It demonstrates substantial improvements in tasks requiring planning and systematic search.

### Reference

- Yao, S., Yu, D., Zhao, J., Shafran, I., Griffiths, T. L., Cao, Y., & Narasimhan, K. (2023). Tree of Thoughts: Deliberate Problem Solving with Large Language Models. *NeurIPS 2023*.
