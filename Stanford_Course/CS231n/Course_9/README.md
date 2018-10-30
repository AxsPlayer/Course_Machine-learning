# Note of Course 9.(CNN Architectures)

## CNN Architectures.(Case Studies)
- LeNet-5: 5 filters, layers
- AlexNet: similar to LetNet but more layers at total. 
- VGGNet: Deep layer. 
	- why use smaller filters(3X3 conv)
	- Stack of three 3 X 3 conv layers has the same effective receptive filed as one 7X7 conv layer. 
- GoogleNet: 22 layers. 
	- Efficient Inception module: Stack all the inception modules.
	- No FC layers.
	- Only 5 million parameters.
	- But the problem is that the inception will increase the depth of the network output, then use the 1 by 1 conv to help manage our computational complexity to reduce the depth of the network.
	- multiple place for softmax output. To prevent gradient vanish in deep neural network.
- ResNet: 152 layers.
	- Very deep networks using residual connections.
	- The problem is the optimization problem, and the solution is that we can use transformation function and the x to sum up the result.
- Other networks: NiN. 
