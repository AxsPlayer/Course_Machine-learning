# Note of Course 16.(Adversarial Examples and Adversarial Training)

## Adversarial Examples.
- use optimization method adding matrix to images to fool the neural network.
- Not just for neural nets
	- Linear models
	- Decision trees
	- Nearest neighbors

## Reason.
- The first think is overfitting.
	- But every difference offset can be added into other examples, and become the adversarial examples, thus maybe it is system problem.
- The second thinking is underfitting.
	- modern deep nets are very piecewise linear.
	- the parameter and weight is not linear, but the input to output relation is linear.

## The Fast Gradient Sign Method.
- maxnorm constraint.

