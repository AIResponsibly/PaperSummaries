# Characterizing Bugs in Python and R Data Analytics Programs
- **Authors**: Shibbir Ahmed, Mohammad Wardat, Hamid Bagheri, Breno Dantas Cruz, Hridesh Rajan
- **Link**: [Paper Link](https://arxiv.org/abs/2306.08632)
- **Summary**: This paper provides a comprehensive study of bugs in Python and R data analytics programs. It uses data from Stack Overflow posts, GitHub bug fix commits, and issues in popular libraries to explore common bug types, root causes, and effects. The study also provides a dataset of manually verified bugs.

### Introduction
- **Languages**: R and Python are popular in data analytics.
- **Problem**: Lack of comprehensive studies on the bugs in these languages.
- **Objective**: Understand common bug types, root causes, and how to mitigate them.
- **Methodology**: Analyzed manually 5,068 Stack Overflow posts, 1,800 GitHub commits, and several GitHub issues.

### Research Questions
1. What are the common bug types in data analytics programs?
2. What are the frequent root causes of these bugs?
3. How are bugs, root causes, and effects related?
4. What are the persistent effects of bugs?
5. Do different libraries have common bugs?

### Methodology
- **Data Collection**: Selected posts and bug fixes from Stack Overflow and GitHub related to 11 R and 7 Python libraries.
- **Manual Analysis**: Verified posts and commits for bugs, filtering out non-bug-related content.
- **Balanced Dataset**: Used Shannon Entropy to ensure balance.

### Key Findings
- **Logic Bugs**: Most frequent bug type in both languages.
- **Data Bugs**: More common in Python, particularly related to data preprocessing.
- **Data Flow Bugs**: More prevalent in R due to implicit intermediate results.
- **Interface, Integration, and System (IIS) Bugs**: Slightly more common in R.
- **Initialization Bugs**: More frequent in R, especially due to implicit outputs.

### Root Causes
- **Confusion with Data Analysis (CDA)**: Most frequent cause of bugs in both languages.
- **Incorrect Data Analysis Parameters (IDAP)**: Common in both languages.
- **API Changes (APIC)**: More frequent in R.
- **Package/Library Mis-selection and Conflicts (PLMC)**: More frequent in Python.

### Bug-Root Cause-Effect Relationships
- **Logic Bugs**: Often caused by Confusion with Data Analysis (CDA), lead to performance issues.
- **Data Bugs**: Linked to shape/type mismatches in APIs, more frequent in Python.
- **API Changes**: Cause significant issues, especially in R.
- **Crash**: The most frequent effect, often due to misuse of parameters or API changes.

### Correlation Between Libraries
- Strong correlations between similar libraries in both languages for visualization and machine learning tasks.
- Similar bug detection and repair strategies can be applied across both languages.

### Lessons Learned
- **Bugs in Data Analytics Programs**: Bugs in data analytics differ from traditional software bugs because they often require reasoning about both the code and the data quality.
- **Python vs. R**: Python is generally better than R for data analytics in terms of fewer bugs, especially in categories like Data Bugs, Data Flow Bugs, IIS Bugs, and Initialization Bugs.
- **Suggestions for Researchers**:
  - Utilize the dataset to identify bug-fix patterns in data analytics programs and feed this information into automated repair tools.
  - Improve abstract representations of data pipelines to avoid common bugs like shape mismatches and enhance reusability.
  - Develop profiling tools to address performance-related bugs.
  - Design bug detection and localization approaches leveraging crashes as a key indicator of bugs in data analytics software.
- **Suggestions for Practitioners**:
  - Incorporate more software engineering concepts into data analytics education to help data scientists avoid common mistakes.
  - Develop automated testing tools and better strategies for handling library deprecations.
  - Increase awareness of incorrect data analysis parameters as a significant source of bugs.
  - Investigate the correlation of bugs and root causes in R and Python to apply cross-language mitigation strategies.

### Implications
- Researchers can use the dataset in this study for bug-fix pattern identification and tool development.
- Practitioners should incorporate SE concepts into data analytics programs to improve robustness.

### Conclusion
- **Contribution**: The study provides a deep understanding of bugs in Python and R, highlighting commonalities and differences. It also contributes a large dataset of manually verified R and Python
bugs.
- **Future Work**: Develop better bug detection tools and improve automatic repair systems.

### Reference
- Ahmed, S., Wardat, M., Bagheri, H., Cruz, B. D., & Rajan, H., "Characterizing Bugs in Python and R Data Analytics Programs", arXiv, 2023.

