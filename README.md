# Responsible AI Paper Summaries

Welcome to the Responsible AI Paper Summaries repository! Here, you'll find concise 1-minute summaries of key papers in various areas of responsible AI.

## Overview

This repository provides brief summaries of AI/ML papers in the following areas:
- **Explainability and Interpretability**
- **Fairness and Biases**
- **Privacy**
- **Security**
- **Safety**
- **Accountability**
- **Human Control and Interaction**
- **Legal and Ethical Guidelines**

## Quick Links

- [Contribution Guidelines](CONTRIBUTING.md)
- [License](LICENSE)

## Summaries by Topic

<details>
  <summary>Explainability and Interpretability</summary>
  
  ### Explainability and Interpretability

  Explainable AI (XAI) and interpretability are two crucial concepts aimed at making AI systems more transparent. There is no consensus on the definitions of these two concepts, and they are sometimes used interchangeably, with some overlap. XAI focuses on providing clear and understandable explanations for the AI’s outputs (decisions or predictions), enhancing system trustworthiness. For example, in financial risk assessment, explainability allows stakeholders to understand how an AI model evaluates factors like credit history or fraud patterns to make decisions about loan approvals or fraud detection.

  Interpretability, on the other hand, involves understanding the internal mechanisms of AI models. Interpretable models often use simpler algorithms or feature engineering techniques that enable users to draw insights from the model's parameters or decision-making process. Examples include decision trees and linear regression models. For instance, in a decision tree to predict loan size based on age and income, the prediction path is clear through the nodes. In linear regression, the influence of each variable is directly observable from the coefficients. 

  1. **[SHAP: Explainable AI](summaries/explainability/SHAP.md)** - ICML 2020
     - **Summary**: Introduces SHAP values for explainable AI, providing a unified measure of feature importance.

  2. **[LIME: Local Interpretable Model-Agnostic Explanations](summaries/explainability/LIME.md)** - KDD 2016
     - **Summary**: Proposes LIME, a technique to explain the predictions of any classifier by approximating it locally with an interpretable model.

</details>

<details>
  <summary>Fairness and Biases</summary>
  
  ### Fairness and Biases

  Ensuring that AI systems do not discriminate against certain individuals or groups, and that they treat all users fairly. Biases extend beyond race or gender and include socioeconomic and other dimensions. Some measures and tools developed by the AI community to address these issues include AI Fairness 360 (AIF360) and Fairlearn.

  1. **[Fairness Through Awareness](summaries/fairness_bias/FairnessThroughAwareness.md)** - NIPS 2011
     - **Summary**: Discusses techniques to ensure fairness in machine learning models by making them aware of potential biases.

  <!-- Add more summaries here -->

</details>

<details>
  <summary>Privacy</summary>
  
  ### Privacy

  Protecting the personal data of users and ensuring that AI systems do not violate individuals' privacy. Privacy-enhancing technologies include differential privacy, which introduces noise to aggregated data to protect identities. Another method, homomorphic encryption, allows calculations on encrypted data to maintain privacy. Another method, zero-knowledge proofs (ZKP), allows for the validation of data without revealing the underlying information itself.

  1. **[Differential Privacy: A Primer](summaries/privacy/DifferentialPrivacy.md)** - Journal of Privacy 2019
     - **Summary**: Introduces differential privacy and its applications in ensuring data privacy.

  <!-- Add more summaries here -->

</details>

<details>
  <summary>Security</summary>
  
  ### Security

  Ensuring that AI systems are secure and protected from malicious actors or attacks, including data poisoning and adversarial attacks. Techniques like robust machine learning models that resist adversarial examples and comprehensive penetration testing are crucial. For example, adversarial training involves intentionally presenting adversarial inputs during training process to improve the model's resilience against attacks.

  <!-- Add summaries here -->

</details>

<details>
  <summary>Safety</summary>
  
  ### Safety

  Guarantees that systems operate without causing unintended harm. Techniques like rigorous safety testing and incorporating fail-safes allow for deactivation or safe-mode operation if something goes wrong. For instance, autonomous vehicles are tested under various conditions to ensure they react safely in unforeseen circumstances.

  <!-- Add summaries here -->

</details>

<details>
  <summary>Accountability</summary>
  
  ### Accountability

  Holding individuals and organizations responsible for the actions and decisions made by AI systems. It’s not sufficient to claim neutrality as merely a platform, drawing lessons from the early internet era​. Implementing frameworks like model cards for model transparency and audit trails helps track decisions made by AI systems. Similar to how financial audits track money flow, companies must keep detailed records of how AI decisions are made.

  <!-- Add summaries here -->

</details>

<details>
  <summary>Human Control and Interaction</summary>
  
  ### Human Control and Interaction

  Ensuring meaningful human oversight in AI involves techniques like "human-in-the-loop" (HITL), where humans make final critical decisions, not the AI systems. For example, in critical medical or judicial decision-making, AI assists human experts who make the ultimate decisions.

  <!-- Add summaries here -->

</details>

<details>
  <summary>Legal and Ethical Guidelines</summary>
  
  ### Legal and Ethical Guidelines

  Developing ethical guidelines and regulatory frameworks helps ensure AI technologies align with societal values and legal standards. National Institute of Standards and Technology (NIST) provides guidelines and frameworks that help in developing legal and ethical AI systems. NIST has developed the AI Risk Management Framework (AI RMF), which outlined best practices for incorporating trustworthiness in AI design, development, and use.

  <!-- Add summaries here -->

</details>

## Recent Summaries

Here are a few recent summaries:

1. **[SHAP: Explainable AI](summaries/explainability/SHAP.md)** - ICML 2020
2. **[Fairness Through Awareness](summaries/fairness_bias/FairnessThroughAwareness.md)** - NIPS 2011
3. **[Differential Privacy: A Primer](summaries/privacy/DifferentialPrivacy.md)** - Journal of Privacy 2019

## How to Use

Each summary is stored in the relevant subfolder within the `summaries/` directory. You can browse through the summaries to quickly understand the main points of various papers.

## Contributing

We welcome contributions! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) file for more details on how to contribute.

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
