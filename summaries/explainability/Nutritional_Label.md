# A Nutritional Label for Rankings
- **Published**: SIGMOD’18
- **Link**: https://arxiv.org/abs/1804.07890
- **Summary**:  Provides a web-based application called Ranking Facts that generates a "nutritional label" for rankings to enhance transparency, fairness, and stability.

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
