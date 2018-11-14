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
- All the grid classification boundary is nearly linear.
- also can make Reinforcement learning fail.

## Solution.
- RBFs behave more intuitively.
- Other attach technology: cross-technology transferability attack
	- using other models to create adversarial examples
- Enhancing Transfer with Ensembles
	- if attack ensemble models, then any model outside is attacked.
- Train on adversarial examples will prevent overfitting and do better on the original task.


