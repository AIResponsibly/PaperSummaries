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
- **Sustainability**
- **Human Control and Interaction**
- **Legal and Ethical Guidelines**

## Recent Summaries
 - **[Taxonomy of Risks Posed by Language Models - FAccT ’22](summaries/safety/risk_taxonomy_llms.md)**. This paper develops a comprehensive taxonomy of ethical and social risks associated with large-scale language models (LMs). It identifies twenty-one risks and categorizes them into six risk areas to guide responsible innovation and mitigation strategies.

 - **[LLMs’ Classification Performance is Overclaimed - arXiv, 2024](summaries/safety/llm_classification_performance.md)**. The paper reveals the limitations of LLMs in classification tasks without gold labels. This work provides a new testbed to evaluate LLMs' human-level discrimination intelligence, proposing a framework for future research to enhance LLMs' robustness and reliability.

 - **[The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions - arXiv, 2024](summaries/safety/instruction_hierarchy_llm.md)**. This paper from OpenAI introduces an instruction hierarchy to train LLMs to prioritize privileged instructions(system messages) over lower-level ones (user messages and third-party inputs), enhancing their robustness against adversaries.


## Summaries by Topic

<details open>
  <summary>Explainability and Interpretability</summary>
  <p>

  - [Understanding the Reasoning Ability of Language Models From the Perspective of Reasoning Paths Aggregation - 41st International Conference on Machine Learning (ICML) 2024](summaries/explainability/LLM_random_walk.md). The paper investigates how pre-trained language models (LMs) perform reasoning tasks by aggregating indirect reasoning paths seen during pre-training.

  - [Patchscopes: A Unifying Framework for Inspecting Hidden Representations of Language Models - International Conference on Machine Learning (ICML) 2024](summaries/explainability/Patchscopes.md). 

  - [Graph of Thoughts: Solving Elaborate Problems with Large Language Models - arXiv, 2024](summaries/explainability/GoT.md). This paper introduces the Graph of Thoughts (GoT) framework, enhancing the reasoning capabilities of large language models by structuring their thought processes as directed graphs.

  - [Why Should I Trust You? Explaining the Predictions of Any Classifier - KDD 2016](summaries/explainability/LIME.md). This paper introduces LIME (Local Interpretable Model-agnostic Explanations), a technique to explain the predictions of any classifier in a faithful and interpretable manner by learning an interpretable model locally around the prediction.

  - [Sparse Autoencoders Find Highly Interpretable Features in Language Models - arXiv, 2023](summaries/explainability/SAE-interpret.md). This paper uses sparse autoencoders to extract interpretable features from language models, addressing polysemanticity in neural networks.

  - [A Unified Approach to Interpreting Model Predictions - NIPS 2017](summaries/explainability/SHAP.md). Introduces SHAP (SHapley Additive exPlanations), a unified framework for interpreting model predictions by assigning each feature an importance value for a particular prediction, integrating six existing methods into a single, cohesive approach.

  - [#A Survey on Knowledge Graphs: Representation, Acquisition, and Applications - IEEE Transactions on Neural Networks and Learning Systems, 2021](summaries/explainability/knowlege_graphs_survey.md). A comprehensive review of knowledge graph representation learning, acquisition methods, and applications.

  - [A Nutritional Label for Rankings - SIGMOD’18](summaries/explainability/Nutritional_Label.md). Provides a web-based application called Ranking Facts that generates a "nutritional label" for rankings to enhance transparency, fairness, and stability.

  - [Tree of Thoughts: Deliberate Problem Solving with Large Language Models - NeurIPS 2023](summaries/explainability/ToT.md). The paper introduces the Tree of Thoughts (ToT) framework, enhancing the problem-solving abilities of large language models by enabling exploration and evaluation of multiple reasoning paths.

  - [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models - NeurIPS 2022](summaries/explainability/CoT.md). This paper demonstrates how chain-of-thought (CoT) prompting significantly enhances the reasoning abilities of large language models (LLMs).

  </p>
</details>

<details open>
  <summary>Fairness and Biases</summary>
  <p>

  - [Taxonomy of Risks Posed by Language Models - FAccT ’22](summaries/fairness_bias/risk_taxonomy_llms.md). This paper develops a comprehensive taxonomy of ethical and social risks associated with large-scale language models (LMs). It identifies twenty-one risks and categorizes them into six risk areas to guide responsible innovation and mitigation strategies.

  - [Benchmarking Cognitive Biases in Large Language Models as Evaluators - arXiv, 2023](summaries/fairness_bias/llm_evaluators_bias.md). This paper introduces COBBLER (COGNITIVE BIAS BENCHMARK FOR LLMS AS EVALUATORS), a benchmark for evaluating cognitive biases in LLMs used as evaluators.

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

  - [To Believe or Not to Believe Your LLM - arXiv, 2024](summaries/safety/believe_or_not.md). This paper explores uncertainty quantification in LLMs to detect hallucinations by distinguishing epistemic from aleatoric uncertainties using an information-theoretic metric.

  - [CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models - arXiv, 2024](summaries/safety/CARES.md). CARES evaluates the trustworthiness of medical vision language models (Med-LVLMs) across five dimensions: trustfulness, fairness, safety, privacy, and robustness.

  - [Taxonomy of Risks Posed by Language Models - FAccT ’22](summaries/safety/risk_taxonomy_llms.md). This paper develops a comprehensive taxonomy of ethical and social risks associated with large-scale language models (LMs). It identifies twenty-one risks and categorizes them into six risk areas to guide responsible innovation and mitigation strategies.

  - [REFCHECKER: Reference-based Fine-grained Hallucination Checker and Benchmark for Large Language Models - arXiv 2024](summaries/safety/RefChecker.md). REFCHECKER is a framework designed to detect fine-grained hallucinations in large language model responses using a novel claim-triplet analysis.

  - [LLMs’ Classification Performance is Overclaimed - arXiv, 2024](summaries/safety/llm_classification_performance.md). The paper reveals the limitations of LLMs in classification tasks without gold labels. This work provides a new testbed to evaluate LLMs' human-level discrimination intelligence, proposing a framework for future research to enhance LLMs' robustness and reliability.

  - [Air Gap: Protecting Privacy-Conscious Conversational Agents - arXiv 2024](summaries/safety/AirGap.md). A paper from Google proposes AirGapAgent to prevent data leakage from LLMs, ensuring privacy in adversarial contexts.

  - [Detecting Hallucinations in Large Language Models Using Semantic Entropy - Nature, 2024](summaries/safety/detecting_hallucinations.md). This paper proposes a method to detect hallucinations in large language models using semantic entropy.

  - [The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions - arXiv, 2024](summaries/safety/instruction_hierarchy_llm.md). This paper from OpenAI introduces an instruction hierarchy to train LLMs to prioritize privileged instructions(system messages) over lower-level ones (user messages and third-party inputs), enhancing their robustness against adversaries.

  - [A Grading Rubric for AI Safety Frameworks - ArXiv, September 2024](summaries/safety/Grading_Rubric_Frameworks.md). This paper proposes a comprehensive grading rubric for evaluating AI safety frameworks. It introduces seven evaluation criteria with 21 indicators, a six-tier grading system, and three methods for applying the rubric. The goal is to enable nuanced comparisons between frameworks, identify areas for improvement, and promote responsible AI development.

  - [An Adversarial Perspective on Machine Unlearning for AI Safety - ArXiv, September 2024](summaries/safety/machine_unlearning.md). This paper explores the robustness of machine unlearning methods designed to remove hazardous knowledge (machine unlearning) from large language models, arguing that these methods may be ineffective under adversarial scrutiny.

  - [SORRY-Bench: Systematically Evaluating Large Language Model Safety Refusal Behaviors - 2024 Arxiv](summaries/safety/SORRY_Bench.md). This paper introduces SORRY-Bench, a benchmark for evaluating LLM safety refusal behaviors.

  - [Characterizing Bugs in Python and R Data Analytics Programs - ](summaries/safety/R_vs_Paython_bugs.md). This paper provides a comprehensive study of bugs in Python and R data analytics programs. It uses data from Stack Overflow posts, GitHub bug fix commits, and issues in popular libraries to explore common bug types, root causes, and effects. The study also provides a dataset of manually verified bugs.

  - [Graph Retrieval-Augmented Generation: A Survey - [arXiv 2024]](summaries/safety/GraphRAG_survey.md). The paper surveys GraphRAG, a framework that enhances traditional RAG by incorporating graph-based retrieval for improved knowledge representation and generation.

  - [A Comprehensive Study of the Capabilities of Large Language Models for Vulnerability Detection - ](summaries/safety/LLM4Vulnerabilities.md). This paper investigates the effectiveness of Large Language Models (LLMs) in detecting software vulnerabilities. It evaluates 11 state-of-the-art LLMs using a variety of prompt designs and presents insights into the models' limitations in understanding code structures and reasoning about vulnerabilities.

  </p>
</details>

<details open>
  <summary>Accountability</summary>
  <p>

  </p>
</details>

<details open>
  <summary>Sustainability</summary>
  <p>

  - [Smaller, Weaker, Yet Better: Training LLM Reasoners via Compute-Optimal Sampling - ArXiv, August 2024](summaries/sustainability/smaller_better.md). 

  - [Large Language Monkeys: Scaling Inference Compute with Repeated Sampling - ArXiv, July 2024](summaries/sustainability/large_lang_monkeys.md). Repeated sampling is an effective and cost-efficient method for scaling inference compute in LLMs, significantly improving task performance across a range of models and tasks.

  </p>
</details>

<details open>
  <summary>Human Control and Interaction</summary>
  <p>

  - [Understanding the Capabilities and Limitations of Large Language Models for Cultural Commonsense - Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics](summaries/human_control_interaction/llm_limitations.md). This paper examines the capabilities and limitations of large language models (LLMs) in understanding cultural commonsense.

  - [Dimensions underlying the representational alignment of deep neural networks with humans - 2024 Conference on Computer Vision](summaries/human_control_interaction/DNN_Humans_Alignment.md). The paper analyzes representational alignment between humans and DNNs, highlighting divergent strategies.

  - [Towards a Science of Human-AI Decision Making: A Survey of Empirical Studies - FAccT '23](summaries/human_control_interaction/Survey_100Papers.md). This survey reviews over 100 empirical studies to understand and improve human-AI decision-making, emphasizing the need for unified research frameworks.

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
