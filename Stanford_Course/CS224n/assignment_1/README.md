# Assignment 1.

## Address of assignment_1.
- web address: https://web.stanford.edu/class/cs224n/assignment1/index.html
- PDF version: The concrete content of assignment_1 is in assignment.pdf.

## How to finish assignment_1?
The first step: download assignment start code, as well as content of assignment_1.

## The solution to assignment_1.
1. Softmax.
(a) Prove softmax(x) = softmax(x + c).
According to definition formula of softmax, the added exp(c) in numerator would be illuminated by exp(c) in denominator.

(b) See in q1_softmax.py

2. Neural Network Basics.
(a) Derive the gradients of the sigmoid function.
The answer will be (1-σ(x))*σ(x).

(b) Derive the gradient with regard to the inputs of a softmax function when cross entropy loss is used for evaluation.
The answer is (yˆ- y).

(c) Derive the gradients with respect to the inputs x to an one-hidden-layer neural network.
The answer is (yˆ- y)*W2*σ′(xW1 + b1)*W1.

(d) How many parameters are there in this neural network.
The answer is (Dx+Dy+2)*H

(e) See in q2_sigmoid.py

(f) See in q2_gradcheck.py

(g) See in q2_neural.py

3. Word2vec.
(a) Derive the gradients with respect to vc.
The answer is U(yˆ-y).

(b) Derive gradients for the “output” word vectors uk’s.
The answer is vc(yˆ-y).

(c) The answer is because of negative sampling from several words instead of thousands words, the speed to calculate word vectors is decreased.

(d) See the answers of assignment_1.

4. Sentiment analysis.
(a) See in scripts.

(b) The reason why to introduce regularization term is that we don’t want our model to overfit training data. And the regularization term can decrease the search space to prevent it happening.

(c) See in scripts.

(d) For the GloVe utilizes the statistical information of training sentences, uses much more training data, and the data quality from wikipedia is better than our original dataset.

(e) The plots get down as regularization increase, and the difference between train accuracy and dev accuracy become lower as regularization increase.

(f) The model tends to predict score in the middle.

(g) Some bad case seems to have the problem that no or none is happening with other positive words, for the reason our sentence feature doesn’t take the word sequence into account, thus, no or none may confuse model. The improvement is to utilize the word sequence using RNN or LSTM.
