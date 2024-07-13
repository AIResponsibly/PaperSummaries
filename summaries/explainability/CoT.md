# Chain-of-Thought Prompting Elicits Reasoning in Large Language Models

- **Published**: NeurIPS 2022
- **Link**: https://arxiv.org/abs/2201.11903
- **Summary**: This paper demonstrates how chain-of-thought (CoT) prompting significantly enhances the reasoning abilities of large language models (LLMs).

### Problem

- LLMs struggle with complex reasoning tasks.
- Only scaling up model size is not enough to address complex tasks such as arithmetic, commonsense, and symbolic reasoning.
- Traditional few-shot prompting methods struggle with reasoning tasks
- Fine-tuning is costly.

### Contributions

- Introduces chain-of-thought (CoT) prompting to improve reasoning in LLMs.
  - prompt that consists of triples: ⟨input, chain of thought, output⟩.
- Demonstrates the emergence of reasoning abilities at large model scales.
- Provides empirical evidence across arithmetic, commonsense, and symbolic reasoning tasks.
- Shows that CoT prompting can be effective without finetuning.

### Method

- CoT prompting involves providing a few examples with intermediate reasoning steps.
- Utilizes large models like PaLM 540B and GPT-3.
- Datasets: GSM8K, ASDiv, AQuA, and others.
- Implementation: No finetuning, just few-shot prompting with CoT examples.

### Result

- State-of-the-art on GSM8K benchmark.
- Significant improvements in commonsense reasoning.
- Consistent gains across different model sizes and datasets.

### Limitations and Assumptions

- costly for real-world applications.
- CoT emulates human thought but true "reasoning" remains unverified.
- Chain of thought does not guarantee correct reasoning paths.
- Manual annotation is costly.

### Future Work

- improving factual generations of language models
- Investigate automatic generation of CoT annotations via LLMs.
- Explore methods to induce reasoning in smaller models.
- apply CoT to other tasks e.g. translation.
- For multiple choice or binary classification,it is likely that models could arrive at the correct answer via an incorrect reasoning path
  - This is a limitation
  - "future work should perform an analysis of the factuality of such chains of thought"

### Conclusion

- CoT prompting effectively enhances LLM reasoning abilities.
- Benefits are most pronounced in large models and multi-step tasks.
- This approach highlights the potential for broader reasoning capabilities in LLMs.

### Reference

- Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed H. Chi, Quoc V. Le, Denny Zhou, "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models," 36th Conference on Neural Information Processing Systems (NeurIPS 2022). [arXiv:2201.11903](https://arxiv.org/abs/2201.11903).
