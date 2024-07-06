# Responsible AI Paper Summaries

Subscribe to the [Responsible AI newsletter](https://airesponsibly.substack.com/) for weekly updates on new papers and more.

## Overview

Welcome to the Responsible AI Paper Summaries repository! Here, you'll find concise summaries of key papers in various areas of responsible AI.

This repository provides brief summaries of AI/ML papers in the following areas:
- **Explainability and Interpretability**
- **Fairness and Biases**
- **Privacy**
- **Security**
- **Safety**
- **Accountability**
- **Human Control and Interaction**
- **Legal and Ethical Guidelines**

## Recent Summaries
 - **[LLMs’ Classification Performance is Overclaimed - arXiv, 2024](summaries/safety/llm_classification_performance.md)**. The paper reveals the limitations of LLMs in classification tasks without gold labels. This work provides a new testbed to evaluate LLMs' human-level discrimination intelligence, proposing a framework for future research to enhance LLMs' robustness and reliability.

 - **[Taxonomy of Risks Posed by Language Models - FAccT ’22](summaries/safety/risk_taxonomy_llms.md)**. This paper develops a comprehensive taxonomy of ethical and social risks associated with large-scale language models (LMs). It identifies twenty-one risks and categorizes them into six risk areas to guide responsible innovation and mitigation strategies.

 - **[The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions - arXiv, 2024](summaries/safety/instruction_hierarchy_llm.md)**. This paper from OpenAI introduces an instruction hierarchy to train LLMs to prioritize privileged instructions(system messages) over lower-level ones (user messages and third-party inputs), enhancing their robustness against adversaries.


## Summaries by Topic

<details open>
  <summary>Explainability and Interpretability</summary>
  <p>

  - [A Nutritional Label for Rankings - SIGMOD’18](summaries/explainability/Nutritional_Label.md). Provides a web-based application called Ranking Facts that generates a "nutritional label" for rankings to enhance transparency, fairness, and stability.

  - [Why Should I Trust You? Explaining the Predictions of Any Classifier - KDD 2016](summaries/explainability/LIME.md). This paper introduces LIME (Local Interpretable Model-agnostic Explanations), a technique to explain the predictions of any classifier in a faithful and interpretable manner by learning an interpretable model locally around the prediction.

  - [A Unified Approach to Interpreting Model Predictions - NIPS 2017](summaries/explainability/SHAP.md). Introduces SHAP (SHapley Additive exPlanations), a unified framework for interpreting model predictions by assigning each feature an importance value for a particular prediction, integrating six existing methods into a single, cohesive approach.

  </p>
</details>

<details open>
  <summary>Fairness and Biases</summary>
  <p>

  - [Taxonomy of Risks Posed by Language Models - FAccT ’22](summaries/fairness_bias/risk_taxonomy_llms.md). This paper develops a comprehensive taxonomy of ethical and social risks associated with large-scale language models (LMs). It identifies twenty-one risks and categorizes them into six risk areas to guide responsible innovation and mitigation strategies.

  </p>
</details>

<details open>
  <summary>Privacy</summary>
  <p>

  </p>
</details>

<details open>
  <summary>Security</summary>
  <p>

  </p>
</details>

<details open>
  <summary>Safety</summary>
  <p>

  - [LLMs’ Classification Performance is Overclaimed - arXiv, 2024](summaries/safety/llm_classification_performance.md). The paper reveals the limitations of LLMs in classification tasks without gold labels. This work provides a new testbed to evaluate LLMs' human-level discrimination intelligence, proposing a framework for future research to enhance LLMs' robustness and reliability.

  - [Detecting Hallucinations in Large Language Models Using Semantic Entropy - Nature, 2024](summaries/safety/detecting_hallucinations.md). This paper proposes a method to detect hallucinations in large language models using semantic entropy.

  - [To Believe or Not to Believe Your LLM - arXiv, 2024](summaries/safety/believe_or_not.md). This paper explores uncertainty quantification in LLMs to detect hallucinations by distinguishing epistemic from aleatoric uncertainties using an information-theoretic metric.

  - [CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models - arXiv, 2024](summaries/safety/CARES.md). CARES evaluates the trustworthiness of medical vision language models (Med-LVLMs) across five dimensions: trustfulness, fairness, safety, privacy, and robustness.

  - [Air Gap: Protecting Privacy-Conscious Conversational Agents - arXiv 2024](summaries/safety/AirGap.md). A paper from Google proposes AirGapAgent to prevent data leakage from LLMs, ensuring privacy in adversarial contexts.

  - [Taxonomy of Risks Posed by Language Models - FAccT ’22](summaries/safety/risk_taxonomy_llms.md). This paper develops a comprehensive taxonomy of ethical and social risks associated with large-scale language models (LMs). It identifies twenty-one risks and categorizes them into six risk areas to guide responsible innovation and mitigation strategies.

  - [SORRY-Bench: Systematically Evaluating Large Language Model Safety Refusal Behaviors - 2024 Arxiv](summaries/safety/SORRY_Bench.md). This paper introduces SORRY-Bench, a benchmark for evaluating LLM safety refusal behaviors.

  - [The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions - arXiv, 2024](summaries/safety/instruction_hierarchy_llm.md). This paper from OpenAI introduces an instruction hierarchy to train LLMs to prioritize privileged instructions(system messages) over lower-level ones (user messages and third-party inputs), enhancing their robustness against adversaries.

  </p>
</details>

<details open>
  <summary>Accountability</summary>
  <p>

  </p>
</details>

<details open>
  <summary>Human Control and Interaction</summary>
  <p>

  - [Towards a Science of Human-AI Decision Making: A Survey of Empirical Studies - FAccT '23](summaries/human_control_interaction/Survey_100Papers.md). This survey reviews over 100 empirical studies to understand and improve human-AI decision-making, emphasizing the need for unified research frameworks.

  - [Dimensions underlying the representational alignment of deep neural networks with humans - 2024 Conference on Computer Vision](summaries/human_control_interaction/DNN_Humans_Alignment.md). The paper analyzes representational alignment between humans and DNNs, highlighting divergent strategies.

  - [Understanding the Capabilities and Limitations of Large Language Models for Cultural Commonsense - Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics](summaries/human_control_interaction/llm_limitations.md). This paper examines the capabilities and limitations of large language models (LLMs) in understanding cultural commonsense.

  </p>
</details>

<details open>
  <summary>Legal and Ethical Guidelines</summary>
  <p>

  </p>
</details>

## How to Use

Each summary is stored in the relevant subfolder within the `summaries/` directory. You can browse through the summaries to quickly understand the main points of various papers.

## Contributing

We welcome contributions! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) file for more details on how to contribute.
