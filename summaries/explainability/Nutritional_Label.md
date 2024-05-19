# A Nutritional Label for Rankings
- Published SIGMOD’18
- link: https://arxiv.org/abs/1804.07890


<!-- 

### Abstract
> Algorithmic decisions often result in scoring and ranking individuals to determine credit worthiness, qualifications for college admissions and employment, and compatibility as dating partners. While automatic and seemingly objective, ranking algorithms can discriminate against individuals and protected groups, and exhibit low diversity. Furthermore, ranked results are often unstable — small changes in the input data or in the ranking methodology may lead to drastic changes in the output, making the result uninformative and easy to manipulate. Similar concerns apply in cases where items other than individuals are ranked, including colleges, academic departments, or products.
>
> In this demonstration we present Ranking Facts, a Web-based application that generates a “nutritional label” for rankings. Ranking Facts is made up of a collection of visual widgets that implement our latest research results on fairness, stability, and transparency for rankings, and that communicate details of the ranking methodology, or of the output, to the end user. We will showcase Ranking Facts on real datasets from different domains, including college rankings, criminal risk assessment, and financial services.
-->

### Problem 
- Algorithmic ranking systems can discriminate against individuals and protected groups, lack diversity, and produce unstable rankings that are easily manipulated.
- Lack of transparency, fairness, and stability in the ranking systems.

### Contributions
- **Ranking Facts**: A web-based application that generates a "nutritional label" for rankings.
   - url is not working: http://demo.dataresponsibly.com/rankingfacts/
   - the github repo has a local version: https://github.com/DataResponsibly/RankingFacts
- **Fairness and Stability**: Incorporation of the latest research on fairness, stability, and transparency for rankings.
- **Visualization**: A collection of visual widgets that explain the ranking methodology and output to end users.

### Method
- The Ranking Facts tool is implemented in Python and uses visual widgets to explain different aspects of the ranking process, including:
  - **Recipe and Ingredients**: Describes the ranking algorithm and attributes most influential to the outcome.
  - **Stability**: Reports a stability score to indicate how small changes in data or methodology can impact the ranking.
  - **Fairness**: Quantifies statistical parity concerning sensitive attributes.
  - **Diversity**: Shows the representation of different demographic categories in the ranked output.


### Result
- Demonstrated the utility of Ranking Facts using real-world datasets, including CS department rankings, criminal risk assessment, and credit/loan datasets.
- The tool explained the ranking process and outcomes, highlighting issues related to fairness, stability, and diversity.

### Limitations and Assumptions of this paper
- The diversity measures are still being defined
- currently limited to binary attributes.

### Conclusion
- Ranking Facts provides an innovative solution for explaining algorithmic rankings, enhancing transparency, fairness, and stability.
- The tool is modular, extensible, and available for public use.

### Future work

### Reference
- Ke Yang, Julia Stoyanovich, Abolfazl Asudeh, Bill Howe, HV Jagadish, and Gerome Miklau. 2018. A Nutritional Label for Rankings. In Proceedings of 2018 International Conference on Management of Data (SIGMOD’18). ACM, New York, NY, USA, 4 pages. https://doi.org/10.1145/3183713.3193568
