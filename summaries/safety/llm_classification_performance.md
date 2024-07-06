# LLMs’ Classification Performance is Overclaimed

- **Published**: arXiv, 2024
- **Link**: [arXiv:2406.16203](https://arxiv.org/abs/2406.16203)
- **Summary**: The paper reveals the limitations of LLMs in classification tasks without gold labels. This work provides a new testbed to evaluate LLMs' human-level discrimination intelligence, proposing a framework for future research to enhance LLMs' robustness and reliability.

### Problem

- LLMs show high performance in classification tasks when correct labels are present.
- When gold labels are intentionally excluded, LLMs still choose from available options.
  - Raises concerns about LLMs’ true understanding and intelligence.
- Traditional classifiers lack flexibility with open label sets.
- Existing benchmarks may overstate LLMs' usefulness.

### Contributions

- Identifies the limitations of LLMs in classification tasks without gold labels (CLASSIFY-W/O-GOLD).
- Introduces the KNOW-NO benchmark with three tasks:
  - BANK77 (intent classification),
  - MC-TEST (multiple-choice QA),
  - and EQUINFER (equation inference).
- Proposes OMNIACCURACY, a metric to evaluate LLMs’ performance with and without correct labels.

### Method

- Three benchmarks: BANK77 (intent classification), MC-TEST (multiple-choice QA), and EQUINFER (equation inference).
- KNOW-NO benchmark assesses classification with varying label sizes and scopes.
- OMNIACCURACY combines performance metrics when gold labels are present and absent.

### Result

- LLMs' performance drops without gold labels.
- Humans outperform LLMs in recognizing absent correct answers.
- OMNIACCURACY offers comprehensive evaluation.

### Limitations and Assumptions

- Only tested three prompts in the absence of gold labels.
- EQUINFER dataset requires many input tokens, making it costly for proprietary models.

### Conclusion

- LLMs struggle in CLASSIFY-W/O-GOLD tasks.
- KNOW-NO benchmark and OMNIACCURACY metric provide a more accurate evaluation of LLMs’ classification abilities.
- "This work establishes a new testbed for assessing LLMs’ human-level discrimination intelligence, offering a framework for future research aimed at improving the robustness and reliability of LLMs."

### Reference

- Xu, H., Lou, R., Du, J., Mahzoon, V., Talebianaraki, E., Zhou, Z., Garrison, E., Vucetic, S., & Yin, W. (2024). LLMs’ Classification Performance is Overclaimed. arXiv. <https://arxiv.org/abs/2406.16203>
