# Note of Course 3.

## The history of NLP.
First Version(Count Based): Moving windows with word co-occurance matrix as original matrix and condense word vectors using SVD.
First Version Plus: Optimization on count-based model for stop word, and so on so forth.
Second Version(Direct Prediction): Moving windows with Skip-gram deep learning method, also named word2vec.
Third Version(GloVe-which combining the best of both worlds above): Utilize co-occurance matrix as well as objective function. And the next step is to sum column word vector and row word vector. The advantages of GloVe are: 1. Fast training; 2. Scalable to huge corpora; 3. Good performance even with small corpus, and small vectors.

## Evaluation methods.
- Intrinsic: Evaluate NLP vectors using specific/intermediate subtask. The advantages are it’s fast to compute and it helps to understand how system works.
- Extrinsic: Evaluate NLP vectors using real task. The advantages are it can truly calculate the improvement of result.

## Tricks.
- Symmetric context works better than Asymmetric context.
- Word2vec may not always useful initialization step for down streaming machine learning tasks. For example, it’s not useful to sentiment analysis, for word vectors contains the context information but sentiment doesn’t care about context. Thus, initialize word vectors randomly is more helpful.

