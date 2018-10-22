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
- Just make gaussian activations using normalizing formula.
- Usually inserted after Fully Connected or Convolutional Layers, and before nonlineartiy.
- The problem: maybe gaussian range is not good. The solution to this is to allow the network to squash the range using the parameters.
- Conclusion:
	- Improves gradient flow through the network.
	- Allows higher learning rates.
	- Reduces the strong dependence on initialization.
	- Acts as a form of regularization in a funny way, and slightly reduces the need for dropout, maybe. The reason is that tying the input X with other samples in the batch with empirical mean of the batch data.

## Process.
- Preprocess data.
- weight initialization.
- Build network.
- Double check that the loss is reasonable.
- set regularization to zero and then assign a number, then the loss will become larger.
- Start training. Make sure that you can overfit very small portion of the training data, taking the first 20 examples and turning off regularization, using simple vanilla 'sgd'. Then the loss will be very low, to sanity check your network function.
- start with small regularization and find learning rate that makes the loss go down. If the loss barely change, maybe the learning rate is too low. If the cost is nan, it mean the loss exploding, and the learning rate is too high.
- Ususally, the learning rate should be between [1e-3, 1e-5].

## Hyperparameter Optimization.
- Cross-validation strategy. Coarse -> fine.
- If the cost is ever > 3 * original cost, just break up it. Note to search in the log space.
- Random search vs. grid search.
- If the loss suddenly become very low, then it means that you have the bad initialization a prime suspect.
- Track the ratio of weight updates / weight magnitudes. Ratio between the updates and values: ~ 0.0002 / 0.02 = 0.01 (about okay) want this to be somewhere around 0.001 or so, then the update will not be too large or too small, for debugging.
