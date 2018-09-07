# Assignment 2.

## The solution to assignment_2.
1. Tensorflow Softmax.
(c) The placeholder variables and feed dictionaries leave space for input data, thus you can change the batch number when you train your network.  

(e) When train_op is called, all the variables to get the result will be updated according to the gradient.
- Attention: There are some errors with none as the loss results, and the reason is the softmax formula is wrong.

2. Neural Transition-Based Dependency Parsing.
(b) 2n, n for shift and n for transition.

(f) γ is 1/(1-pdrop).

(g)(i) Because it minimizes the influence of current gradient. 
	Because it will not in local minimum and the method seems like to do average over all the dataset.
(ii) The parameters with smallest average gradient will update largest. For the reason it will force the parameter with small gradient to leave the local minimum.