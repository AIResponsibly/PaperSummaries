# Why Should I Trust You? Explaining the Predictions of Any Classifier
- **Published**: KDD 2016
- **Link**: http://dx.doi.org/10.1145/2939672.2939778
- **Summary**: This paper introduces LIME (Local Interpretable Model-agnostic Explanations), a technique to explain the predictions of any classifier in a faithful and interpretable manner by learning an interpretable model locally around the prediction.

### Problem 
- Machine learning models are often seen as black boxes, making it difficult to understand and trust their predictions.
- Users need to trust individual predictions and the model as a whole, especially when these predictions are used for decision making in critical applications.

### Contributions
- **LIME**: An algorithm that explains the predictions of any classifier by approximating it locally with an interpretable model.
- **SP-LIME**: A method to select a set of representative instances with explanations to address the “trusting the model” problem, using submodular optimization.
- **Comprehensive Evaluation**: Evaluation of LIME with simulated and human subjects, demonstrating its effectiveness in various scenarios requiring trust.

### Method
- **Interpretable Data Representations**: Use of interpretable representations (e.g., presence/absence of words in text or super-pixels in images) to explain model predictions.
- **Local Fidelity**: Ensuring the explanation is locally faithful to the classifier's behavior around the instance being explained.
- **Sparse Linear Explanations**: Using sparse linear models to provide simple and interpretable explanations.
- **Sampling for Local Exploration**: Sampling instances around the instance being explained to learn the local behavior of the model.
- **Submodular Pick (SP)**: Selecting a diverse and representative set of explanations to provide a global understanding of the model.

### Result
- **Utility of Explanations**: Demonstrated that LIME helps users understand and trust individual predictions and the model as a whole.
- **Simulated and Human Experiments**: Showed that explanations improve users' ability to select better models, trust predictions, and improve untrustworthy classifiers.

### Limitations and Assumptions of this paper
- The choice of interpretable representations and models (e.g., sparse linear models) may not be powerful enough for certain complex behaviors.
- The approach focuses on local fidelity, which may not capture the global behavior of highly non-linear models.

### Conclusion
- LIME provides a flexible and effective solution for explaining model predictions, enhancing trust in machine learning models.
- The method is model-agnostic and can be applied to any classifier, making it suitable for various applications.

### Future work
- Explore different families of explanations, such as decision trees.
- Address the pick step for image data.
- Investigate applications in other domains like speech, video, and medical fields.
- Explore theoretical properties and computational optimizations for real-time explanations.

### Reference
- Marco Tulio Ribeiro, Sameer Singh, and Carlos Guestrin. 2016. Why Should I Trust You? Explaining the Predictions of Any Classifier. In Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD '16). ACM, New York, NY, USA, 1135-1144. http://dx.doi.org/10.1145/2939672.2939778
