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
- Leaky ReLU:
	- Does not saturate
	- Computationally efficient
	- Converges much faster than sigmoid/tanh
	- will not die
- PReLU: add the parameter to the Leaky ReLU.
- ELU: Exponential Linear Units
	- All benefits of ReLU
	- Colser to zero mean outputs
	- Negative saturation regime compared with Leaky ReLU
	- Adds some robustness to noise
	- Computation needs exp()
- Maxout Neuron: generalize ReLU and Leaky ReLU, but double the parameters.
- In practice:
	- Use ReLU. Be careful with your learning rates.
	- Try out Leaky ReLU/ Maxout/ELU
	- Try out tanh but don't expect much
	- don't use sigmoid

## Preprocess the data.
- zero-centered data:
- normalized data: All features in the same scale thus they contribute equally. But in the image case, normalized is not required for the pixel values are already in the same scale. 
- PCA or whitening: In image case, also not do this kind of complicated methods.
- Substract mean of each channel. 

## Weight initialization.
- Cannot initialize weight to zeros: for all the neurons will be the same state.
- First idea: small random numbers. But create some problems in deep neural networks, because all the activations will be zeros for tanh and weight are small numbers around zero. And also in the backprop, the weight will not update for x is small.
- Second idea: weights are big 1.0 rather than 0.01: the problem is that the neurons will be saturated, the weight would not be updated.
- Good initialization: Xavier initialization. The idea is to get the same weight variance at each layer. And the method is that when we meet small input, we should assign large weight, thus the output of the activation function will be large still. But it's suitable for sigmoid, not for ReLU, for ReLU there are half of units are zero gradient.
- The solution to above situation: Add additional /2 in the initialization formula, for half neurons will be dead.

## Batch Normalization.
- The aim is to keep activations in gaussian range.
- Just make gaussian activations using normalizing formual.
