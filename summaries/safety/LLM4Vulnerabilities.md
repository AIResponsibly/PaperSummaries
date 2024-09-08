# A Comprehensive Study of the Capabilities of Large Language Models for Vulnerability Detection
- **Authors**: Benjamin Steenhoek, Mirza Sanjida Alam, Md Mahbubur Rahman, Earl T. Barr, Monoshi Kumar Roy, Wei Le
- **Link**: [Paper Link](https://arxiv.org/abs/2403.17218)
- **Summary**: This paper investigates the effectiveness of Large Language Models (LLMs) in detecting software vulnerabilities. It evaluates 11 state-of-the-art LLMs using a variety of prompt designs and presents insights into the models' limitations in understanding code structures and reasoning about vulnerabilities.

### Problem
- LLMs have potential for tasks like code generation and vulnerability detection.
- Vulnerability detection requires precise code reasoning, which may challenge LLMs.
- Types of Vulnerabilities Discussed
  - **Buffer Overflows**: Data exceeds buffer space, causing memory corruption or crashes.
  - **NULL Pointer Dereference**: Accessing an uninitialized pointer, leading to crashes.
  - **Integer Overflows/Underflows**: Arithmetic exceeds integer limits, causing errors.
  - **Resource Leaks**: Failure to release resources, leading to performance issues.
  - **Infinite Loops**: Code runs indefinitely, causing denial of service.
  - **Incorrect Bounds/Range Checks**: Failing to validate input ranges, causing unsafe operations.

- Existing work on LLMs lacks detailed analysis of their capability for vulnerability detection and error types.

### Contributions
- **Prompting Techniques**: Evaluated multiple existing prompting methods and introduced three new techniques.
- **LLM Evaluation**: Assessed 11 LLMs on vulnerability detection, including analyzing their ability to explain identified vulnerabilities.
- **Error Analysis**: Categorized errors in LLM-generated explanations into four types: Code Understanding, Logic Errors, Hallucinations, and Common Knowledge Errors.
- **Comparison with Humans**: Compared LLMs’ performance against human experts on fault localization.

### Method
- **Dataset**: Used the SVEN dataset with C/C++ functions containing real-world vulnerabilities and bug-fixing commits. 
- **Models**: Selected 11 LLMs including GPT-4, GPT-3.5, Code LLAMA, and others. Evaluated using five distinct prompt methods.
- **Error Categorization**: Manually analyzed 287 LLM-generated vulnerability explanations, categorizing errors into four major types.

### Key Findings
- **Vulnerability Detection Performance**: 
  - Models achieved 0.5-0.63 Balanced Accuracy, close to random guessing.
  - LLMs failed to distinguish between buggy and fixed versions of code 76% of the time.
- **Error Types**:
  - **Code Understanding**: 41% of responses contained errors, particularly with bounds or NULL checks.
  - **Logic Errors**: Incorrect logical implications were observed in 9% of responses.
  - **Hallucinations**: 11% of responses contained hallucinated or repeated information.
  - **Common Knowledge**: 3% of errors were due to incorrect assumptions about code or application context.
- **Human Comparison**: LLMs correctly located 6 out of 27 bugs in DbgBench, while human developers correctly located all bugs.

### Conclusion
-  "These findings highlight LLMs’ limitations in vulnerability detection"
-  "Our dataset of LLM errors provides guidance for future improvement of LLM-based vulnerability detection." 
- Dataset, code and analysis for this paper: https://figshare.com/s/78fe02e56e09ec49300b
