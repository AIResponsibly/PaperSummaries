# A Unified Approach to Interpreting Model Predictions
- **Published**: NIPS 2017
- **Link**: https://arxiv.org/abs/1705.07874
- **Summary**: Introduces SHAP (SHapley Additive exPlanations), a unified framework for interpreting model predictions by assigning each feature an importance value for a particular prediction, integrating six existing methods into a single, cohesive approach.

### Problem 
- Complex models often achieve high accuracy but are difficult to interpret
- Existing interpretation methods are diverse and it is unclear how they relate to each other or when to prefer one over another.

### Contributions
- **SHAP Framework**: A unified approach that identifies and integrates six existing methods into a class of additive feature attribution methods.
- **Theoretical results**:  Showing there is a unique solution in this class that satisfies local accuracy, missingness, and consistency.
- **New Methods**: Proposed new methods that improve computational performance and align better with human intuition compared to existing approaches.

### Method
- **Additive Feature Attribution**: Defines an explanation model as a linear function of binary variables, unifying six existing methods (LIME, DeepLIFT, Layer-Wise Relevance Propagation, Shapley Regression Values, Shapley Sampling Values, Quantitative Input Influence).

- **SHAP Values**: Derived from Shapley values in game theory, providing a unique measure of feature importance that satisfies the properties of local accuracy, missingness, and consistency.
- **Model-Agnostic Approximations**: Kernel SHAP combines weighted linear regression with Shapley values to improve sample efficiency.
- **Model-Specific Approximations**: Linear SHAP, Low-Order SHAP, Max SHAP, and Deep SHAP offer faster computations for specific model types.

### Result
- Demonstrated that SHAP values provide a more accurate and intuitive feature importance measure compared to LIME and other methods.
- Showed through computational experiments that Kernel SHAP requires fewer evaluations of the original model to achieve similar approximation accuracy.
- User studies confirmed that SHAP values are more consistent with human intuition than DeepLIFT and LIME.

### Limitations and Assumptions of this paper
- The computational complexity can be high for models with a large number of features.
- Approximation methods require assumptions such as feature independence or model linearity.

### Conclusion
- SHAP values provide a unified, theoretically sound framework for interpreting model predictions, integrating multiple existing methods.
- The approach ensures consistency and local accuracy, offering improved interpretability for complex models.

### Future work
- Develop faster model-type-specific estimation methods with fewer assumptions.
- Integrate interaction effects from game theory.
- Define new explanation model classes.

### Reference
- Scott M. Lundberg and Su-In Lee. 2017. A Unified Approach to Interpreting Model Predictions. In Proceedings of the 31st Conference on Neural Information Processing Systems (NIPS 2017). Long Beach, CA, USA. https://arxiv.org/abs/1705.07874
