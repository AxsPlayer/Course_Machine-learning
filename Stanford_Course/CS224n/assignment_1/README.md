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

(g) See in q2_.py

