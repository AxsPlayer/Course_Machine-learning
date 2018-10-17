# Note of Course 6.(Training Neural Networks)

## Activation Function.
- Sigmoid: 
	- If the input is too positive or too negative, the gradient would be near to zero.
	- Sigmoid outputs are not zero-centered
	- Exp() is a bit compute expensive
- The input should not always be positive or negative, or the gradient will be always in the same direction and can not converge quickly.
- tanh:
	- Squashes numbers to range [-1, 1]
	- zero centered(nice)
	- still kills gradients when saturated
	- a bit better than sigmoid but also has a lot of problems
- ReLU(Rectified Linear Unit):
	- often used in Neural Network.
	- does not saturate (in positive region)
	- very computationally effiecient
	- converges much faster
	- more biology plausible than sigmoid
	- but also not zero-centered output
	- but also an annoyance

	- The ReLU unit will be dead if the weight initialization is not good at first time or the learning rate is set too high that after overupdating the weight.