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

 - **[The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions - arXiv, 2024](summaries/safety/instruction_hierarchy_llm.md)**. This paper from OpenAI introduces an instruction hierarchy to train LLMs to prioritize privileged instructions(system messages) over lower-level ones (user messages and third-party inputs), enhancing their robustness against adversaries.

 - **[Taxonomy of Risks Posed by Language Models - FAccT ’22](summaries/safety/risk_taxonomy_llms.md)**. This paper develops a comprehensive taxonomy of ethical and social risks associated with large-scale language models (LMs). It identifies twenty-one risks and categorizes them into six risk areas to guide responsible innovation and mitigation strategies.


## Summaries by Topic

<details open>
  <summary>Explainability and Interpretability</summary>
  <p>

  - [Graph of Thoughts: Solving Elaborate Problems with Large Language Models - arXiv, 2024](summaries/explainability/GoT.md). This paper introduces the Graph of Thoughts (GoT) framework, enhancing the reasoning capabilities of large language models by structuring their thought processes as directed graphs.

  - [A Unified Approach to Interpreting Model Predictions - NIPS 2017](summaries/explainability/SHAP.md). Introduces SHAP (SHapley Additive exPlanations), a unified framework for interpreting model predictions by assigning each feature an importance value for a particular prediction, integrating six existing methods into a single, cohesive approach.

  - [#A Survey on Knowledge Graphs: Representation, Acquisition, and Applications - IEEE Transactions on Neural Networks and Learning Systems, 2021](summaries/explainability/knowlege_graphs_survey.md). A comprehensive review of knowledge graph representation learning, acquisition methods, and applications.

  - [Tree of Thoughts: Deliberate Problem Solving with Large Language Models - NeurIPS 2023](summaries/explainability/ToT.md). The paper introduces the Tree of Thoughts (ToT) framework, enhancing the problem-solving abilities of large language models by enabling exploration and evaluation of multiple reasoning paths.

  - [Why Should I Trust You? Explaining the Predictions of Any Classifier - KDD 2016](summaries/explainability/LIME.md). This paper introduces LIME (Local Interpretable Model-agnostic Explanations), a technique to explain the predictions of any classifier in a faithful and interpretable manner by learning an interpretable model locally around the prediction.

  - [A Nutritional Label for Rankings - SIGMOD’18](summaries/explainability/Nutritional_Label.md). Provides a web-based application called Ranking Facts that generates a "nutritional label" for rankings to enhance transparency, fairness, and stability.

  - [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models - NeurIPS 2022](summaries/explainability/CoT.md). This paper demonstrates how chain-of-thought (CoT) prompting significantly enhances the reasoning abilities of large language models (LLMs).

  - [Understanding the Reasoning Ability of Language Models From the Perspective of Reasoning Paths Aggregation - 41st International Conference on Machine Learning (ICML) 2024](summaries/explainability/LLM_random_walk.md). The paper investigates how pre-trained language models (LMs) perform reasoning tasks by aggregating indirect reasoning paths seen during pre-training.

  - [Sparse Autoencoders Find Highly Interpretable Features in Language Models - arXiv, 2023](summaries/explainability/SAE-interpret.md). This paper uses sparse autoencoders to extract interpretable features from language models, addressing polysemanticity in neural networks.

  </p>
</details>

<details open>
  <summary>Fairness and Biases</summary>
  <p>

  - [Benchmarking Cognitive Biases in Large Language Models as Evaluators - arXiv, 2023](summaries/fairness_bias/llm_evaluators_bias.md). This paper introduces COBBLER (COGNITIVE BIAS BENCHMARK FOR LLMS AS EVALUATORS), a benchmark for evaluating cognitive biases in LLMs used as evaluators.

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

  - [Detecting Hallucinations in Large Language Models Using Semantic Entropy - Nature, 2024](summaries/safety/detecting_hallucinations.md). This paper proposes a method to detect hallucinations in large language models using semantic entropy.

  - [LLMs’ Classification Performance is Overclaimed - arXiv, 2024](summaries/safety/llm_classification_performance.md). The paper reveals the limitations of LLMs in classification tasks without gold labels. This work provides a new testbed to evaluate LLMs' human-level discrimination intelligence, proposing a framework for future research to enhance LLMs' robustness and reliability.

  - [The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions - arXiv, 2024](summaries/safety/instruction_hierarchy_llm.md). This paper from OpenAI introduces an instruction hierarchy to train LLMs to prioritize privileged instructions(system messages) over lower-level ones (user messages and third-party inputs), enhancing their robustness against adversaries.

  - [To Believe or Not to Believe Your LLM - arXiv, 2024](summaries/safety/believe_or_not.md). This paper explores uncertainty quantification in LLMs to detect hallucinations by distinguishing epistemic from aleatoric uncertainties using an information-theoretic metric.

  - [Air Gap: Protecting Privacy-Conscious Conversational Agents - arXiv 2024](summaries/safety/AirGap.md). A paper from Google proposes AirGapAgent to prevent data leakage from LLMs, ensuring privacy in adversarial contexts.

  - [SORRY-Bench: Systematically Evaluating Large Language Model Safety Refusal Behaviors - 2024 Arxiv](summaries/safety/SORRY_Bench.md). This paper introduces SORRY-Bench, a benchmark for evaluating LLM safety refusal behaviors.

  - [Taxonomy of Risks Posed by Language Models - FAccT ’22](summaries/safety/risk_taxonomy_llms.md). This paper develops a comprehensive taxonomy of ethical and social risks associated with large-scale language models (LMs). It identifies twenty-one risks and categorizes them into six risk areas to guide responsible innovation and mitigation strategies.

  - [CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models - arXiv, 2024](summaries/safety/CARES.md). CARES evaluates the trustworthiness of medical vision language models (Med-LVLMs) across five dimensions: trustfulness, fairness, safety, privacy, and robustness.

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

  - [Understanding the Capabilities and Limitations of Large Language Models for Cultural Commonsense - Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics](summaries/human_control_interaction/llm_limitations.md). This paper examines the capabilities and limitations of large language models (LLMs) in understanding cultural commonsense.

  - [Towards a Science of Human-AI Decision Making: A Survey of Empirical Studies - FAccT '23](summaries/human_control_interaction/Survey_100Papers.md). This survey reviews over 100 empirical studies to understand and improve human-AI decision-making, emphasizing the need for unified research frameworks.

  - [Dimensions underlying the representational alignment of deep neural networks with humans - 2024 Conference on Computer Vision](summaries/human_control_interaction/DNN_Humans_Alignment.md). The paper analyzes representational alignment between humans and DNNs, highlighting divergent strategies.

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
