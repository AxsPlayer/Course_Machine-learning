# Note of Course 10.(Recurrent Neural Networks)

## Batch normalization.
- The VGG and google-net with deep layers should use some tricks to deal with the gradient problem. VGG train layer by layer, and google-net train with several classifiers.
- After invention of batch normalization, they are not needed.

## ResNet.
- If you use L2 regularization, then the parameters would be drilled to zero, thus, the neural network can choose which layers to be used.

## Recurrent Neural Network.
- Many-to-many case: first sum up all the loss from each time step to the final loss, and then flow the gradient back to each layer's weights, and sum the weight graident up to upgrade the weight at final.
- Machine translation is the combination of many-to-one and one-to-many.
- In the output layer, use sampling rather than the argmax will produce more diversity.
- To deal with the problem with too long sequence:
	- truncated backpropagation through time: means to train the backpro part by part, every part contains hundred length.
- image caption.