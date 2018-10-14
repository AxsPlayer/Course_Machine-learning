# Note of Course 3.

## Loss function.
- Hinge loss function: If the score or the probability is large than the other class over a soft margin, then the loss is zero, or the loss would be the difference.
- Multiple-classification case: The score of ground truth class over the summed score of the other classes.
- The value of loss would not influence the result for it's just rescaling.
- The loss function is the metric you want to tell the algorithm what kind of error is bad as well as which is not so bad.

- Another popular loss function: Softmax loss function for multinomial logistic regression. 

## Regularization.
- The regularization is to decrease the weight and thus to prevent overfitting problem in machine learning.
- Common regularization:
	- L2 regularization.
	- L1 regularization.
	- Elastic net (L1 + L2)
	- Max norm regularization.
	- Dropout
	- Fancier: Batch normalization, stochastic depth.

## Optimization.
- Random search.
- 
