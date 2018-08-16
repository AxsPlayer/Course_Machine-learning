# Note of Course 4.

## How to do NER(Named Entity Recognition) or sentiment analysis?
Use the simplest way with context window and concatenated word vectors, and apply soft max or shallow neural network to classify center word into predefined classes.

## Cross Entropy Loss.
The aim of cross entropy loss is to minimize the negative log probability of truth label. And if multiplying truth vector, it’s simple notation.

## Max-Margin Objective Function.
The aim of max-margin objective function is to maximize the margin of decision boundary, using formula: J = max(0, 1 - s + sc), where s is notation for softmax value of positive data, and sc is notation for softmax value of corrupt negative data. Here, the 1 is enough for the maximum of two probabilities is 1. But without softmax, just original score, the one is also efficient enough.
The another advantage of this objective function is that in the later process of training, it will lead to neglect of correct classification and more focus on wrong cases.
And the max-margin loss is always better than cross entropy for the reason that max-margin will maximize the margin of decision boundary to all the points, thus more robust.

 

