## A Survey on Knowledge Graphs: Representation, Acquisition, and Applications

- **Published**: IEEE Transactions on Neural Networks and Learning Systems, 2021
- **Link**: [IEEE Xplore](https://ieeexplore.ieee.org/document/9446554)
- **Summary**: A comprehensive review of knowledge graph representation learning, acquisition methods, and applications.


## I. INTRODUCTION

- Incorporating human knowledge in AI is essential for solving complex tasks.
- Knowledge graphs represent structured facts and are gaining research attention.
- Knowledge graphs consist of entities, relationships, and semantic descriptions.
- They can be viewed as graphs or knowledge bases for interpretation and inference.
- Examples include factual triples and graph representations of entities and relationships.

### Contributions

- Comprehensive review of knowledge graph origins and modern techniques.
- Full-view categorization of knowledge graph research and new taxonomies.
- Wide coverage on emerging advances like transformer-based encoding and GNNs.
- Summary and outlook on future research directions.

## II. OVERVIEW

### A. A Brief History of Knowledge Bases

- Knowledge representation dates back to the 1950s with semantic nets and symbolic logic.
- Early systems like MYCIN used rule-based expert systems for problem-solving.
- The Cyc project aimed at assembling human knowledge.
- Semantic Web standards like RDF and OWL were developed.
- Google's Knowledge Graph popularized the concept in 2012.

### B. Definitions and Notations

- No wide-accepted formal definition of knowledge graphs exists.
- Ehrlinger and Wöß define knowledge graphs with reasoning engines.
- Wang et al. define them as multi-relational graphs of entities and relations.
- Notations include sets of entities, relations, and facts, with various mathematical operations.

### C. Categorization of Research on Knowledge Graph

- Knowledge representation learning (KRL) involves learning low-dimensional embeddings.
- Knowledge acquisition includes tasks like knowledge graph completion and relation extraction.
- Temporal knowledge graphs incorporate temporal information for representation.
- Knowledge-aware applications use knowledge graphs in areas like NLU and recommendation systems.

## III. KNOWLEDGE REPRESENTATION LEARNING

### A. Representation Space

- Entities and relations are embedded in various spaces like Euclidean, complex vector, Gaussian distribution, and manifold.
- Point-wise space is widely used, but other spaces capture different properties.
- Complex space allows for symmetric and antisymmetric relations.
- Manifold space offers more expressive representation.

### B. Scoring Function

- Measures the plausibility of facts in knowledge graphs.
- Distance-based functions calculate distances between entities.
- Semantic similarity functions measure plausibility through matching.
- Translational models like TransE use distance-based scoring.

### C. Encoding Models

- Linear/bilinear models use linear operations for encoding interactions.
- Factorization models decompose relational data into low-rank matrices.
- Neural networks, CNNs, RNNs, and transformers encode relational interactions.
- Graph neural networks (GNNs) learn connectivity structures in graphs.

### D. Embedding with Auxiliary Information

- Textual descriptions provide supplementary semantic information.
- Type information incorporates hierarchical classes of entities.
- Visual information uses images to enrich embeddings.
- Uncertain information represents the likelihood of relational facts.

### E. Summary

- KRL involves choosing representation space, scoring function, encoding model, and auxiliary information.
- Popular spaces include Euclidean, complex, Gaussian, and manifold.
- Scoring functions can be distance-based or similarity-based.
- Encoding models vary from linear/bilinear to advanced neural networks and GNNs.

## IV. KNOWLEDGE ACQUISITION

### A. Knowledge Graph Completion (KGC)

- Expands existing knowledge graphs with new facts.
- Embedding-based ranking, path-based reasoning, rule-based reasoning, and meta relational learning are methods used.
- Triple classification and entity discovery tasks are included.

### B. Relation Extraction

- Identifies relations between entities from text.
- Uses neural paradigms like attention mechanisms, GCNs, and deep residual learning.
- Techniques include adversarial training and reinforcement learning.

### C. Entity Discovery

- Involves tasks like entity recognition, typing, disambiguation, and alignment.
- Methods use neural models to identify and categorize entities.

## V. TEMPORAL KNOWLEDGE GRAPHS

### A. Temporal Embedding

- Incorporates time information in embeddings.
- Techniques capture temporal dynamics of entities and relations.

### B. Entity Dynamics

- Models changes in entity attributes and relationships over time.
- Focuses on capturing temporal dependencies.

### C. Temporal Relational Dependency

- Explores how relations evolve over time.
- Models temporal logical reasoning and dependencies.

## VI. KNOWLEDGE-AWARE APPLICATIONS

### A. Natural Language Understanding (NLU)

- Uses knowledge graphs to enhance language understanding.
- Applications include question answering and dialogue systems.

### B. Recommender Systems

- Improves recommendations by integrating knowledge graphs.
- Addresses sparse and cold start problems.

### C. Miscellaneous Real-World Applications

- Applications in search engines, medical domains, mental healthcare, and more.
- Enhances tasks like zero-shot image classification and sentiment analysis.

## VII. FUTURE WORK

- Exploration of complex reasoning using GNNs and reinforcement learning.
- Development of unified frameworks for knowledge representation and reasoning.
- Emphasis on interpretability and scalability of KGE methods.
- Integration of dynamic and temporal aspects in knowledge graphs.

## VIII. CONCLUSION

- Knowledge graphs are vital for advancing AI with structured information.
- Significant progress has been made, but challenges remain in reasoning and scalability.
- Future research should address these challenges for full potential utilization.
