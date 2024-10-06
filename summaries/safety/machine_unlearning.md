# An Adversarial Perspective on Machine Unlearning for AI Safety

- **Published**: ArXiv, September 2024
- **Authors**: Jakub Łucki, Boyi Wei, Yangsibo Huang, Peter Henderson, Florian Tramèr, Javier Rando
- **Affiliation**: ETH Zurich, Princeton University
- **Link**: [ArXiv](https://arxiv.org/abs/2409.18025)
- **Summary**: This paper explores the robustness of machine unlearning methods designed to remove hazardous knowledge (machine unlearning) from large language models, arguing that these methods may be ineffective under adversarial scrutiny. 

## I. INTRODUCTION

- **Problem**: "Large language models are finetuned to refuse questions about hazardous knowl- edge, but these protections can often be bypassed."
  - Machine unlearning is a proposed solution but its effectiveness is questionable.
- **Objective**: Investigate whether unlearning methods genuinely remove hazardous knowledge or merely obscure it.

### 1.1 Background
- - "Machine unlearning aims to update the weights of a model to remove specific knowledge so that it cannot be accessed in any form"
- **Large Language Models (LLMs)**: Trained on massive datasets, making it nearly impossible to filter all harmful information.
- **Safety Fine-tuning**: LLMs are trained to refuse harmful queries, but adversaries can jailbreak these systems.

### 1.2 Machine Unlearning
- **Definition**: Aims to erase specific knowledge from LLMs entirely, unlike safety training which blocks access without removing knowledge.
- **State-of-the-art**: RMU (Representation Misdirection for Unlearning) shows promise but might not remove knowledge completely.

## II. RELATED WORK

- **Safety Training**: Methods like DPO (Direct Preference Optimization) and circuit breakers aim to prevent harmful outputs but have known weaknesses.
- **Jailbreaks**: These techniques exploit the vulnerabilities in safety fine-tuning, allowing adversaries to access forbidden knowledge.
- **Unlearning**: Methods like RMU aim to prevent retrieval of hazardous information, but recovery attacks have shown success in reversing unlearning effects.

## III. EXPERIMENTAL SETUP

### 3.1 Threat Model
- Assumes **white-box access**, allowing adversaries to manipulate model weights and activations to recover knowledge.
- This contrasts with RMU's assumed black-box access, where attackers can only interact with the model through queries.

### 3.2 Unlearning Methods
RMU (Representation Misdirection for Unlearning)
- Concept: 
  - Modifies activations to block harmful knowledge.
  - Introduces controlled noise in the model’s lower layers.
  - Obfuscates dangerous knowledge, directing outputs to benign responses.
- How it works:
  - Detects harmful prompts and distorts internal representations.
  - Leaves benign knowledge unchanged.
- Robustness: 
  - Effective against basic attacks.
  - Vulnerable to adversarial techniques like orthogonalization and finetuning.
  - Can restore unlearned knowledge in some cases.

NPO (Negative Preference Optimization)
- Concept: 
  - Targets harmful knowledge for removal.
  - Balances removal with the preservation of useful knowledge.
- How it works:
  - Fine-tunes on unwanted knowledge (negative set).
  - Adds auxiliary training to maintain general knowledge.
- Application:
  - More robust than RMU in adversarial settings.
  - Still vulnerable to targeted recovery attacks and minor finetuning.

DPO (Direct Preference Optimization)
- Concept:
  - Focuses on refusing harmful queries, not removing knowledge.
  - Acts as a safety training baseline.
- How it works:
  - Fine-tunes the model to prefer refusing harmful prompts.
  - Uses preference optimization to control responses.
- Baseline for comparison:
  - Compared against RMU and NPO.
  - Vulnerable to jailbreak attacks that bypass refusals.


### 3.3 Models and Datasets
- **Zephyr-7B-β**: The baseline model used for finetuning.
- **WMDP Benchmark**: Evaluates model performance on hazardous topics in biology and cybersecurity.
- **MMLU Benchmark**: Tests general model utility post-unlearning.

## IV.  Our Methods To Recover Hazardous Capabilities

"We use a wide range of methods to uncover hazardous capabilities in the target models, ranging from representation engineering to prompt-based jailbreaks."

### 4.1 Finetuning
- Even with unrelated datasets, finetuning can recover unlearned knowledge, suggesting that unlearning may be superficial.

### 4.2 Orthogonalization
- Ablating certain activation directions restores hazardous capabilities in unlearned models.

### 4.3 Logit Lens
- A technique projecting internal activations back to vocabulary shows that unlearning methods may still store hazardous knowledge.

### 4.4 Enhanced GCG (Generative Counterfactual Generation)
- Crafted adversarial prompts recover unlearned knowledge with high accuracy, indicating weaknesses in unlearning methods.

### 4.5 Set Difference Pruning
- Identifies neurons critical to knowledge retention and prunes them to test the effectiveness of unlearning.

## V. RESULTS

- **Finetuning**: Recovers hazardous capabilities even with unrelated data.
- **Orthogonalization**: Recovers hazardous knowledge by removing directions in the activation space.
- **Logit Lens**: Reveals that unlearning fails to erase knowledge from deeper model layers.
- **Enhanced GCG**: Increases model accuracy on hazardous knowledge benchmarks by manipulating inputs.

## VI. DISCUSSION

- **Key Insight**: Unlearning methods, like RMU and NPO, obscure rather than erase knowledge, similar to safety training.
- **Evaluation Gaps**: Current black-box evaluations are inadequate; future assessments should focus on model internals.
- **Unlearning Vulnerabilities**: Universal adversarial prefixes and critical neurons undermine the robustness of unlearning.

## VII. CONCLUSION

- **Main Contribution**: Demonstrates the limitations of current unlearning methods and the need for more robust evaluations.
- **Implications**: Questions the practical benefit of unlearning over safety training.
