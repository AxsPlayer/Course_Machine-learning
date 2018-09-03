# Note of Mid-term review.

## word2vec.
- GloVe: Using the two word vectors multiply results minus co-occurance as the cost function, utilizing the co-occurance matrix.

## Activation function.
- ReLu: The problem is that if the input of ReLu unit is negative, thus the gradient will be zero always. Thus, how to set the initialization of weights is important as well.

## Regularization.
- Drop-out: The drop out method is actually an ensemble method.

## Training tips and tricks.
- Learning rate:
	- If loss curve seems to be unstable, decrease learning rate.
	- If loss curve appears to be ‘linear’, increase learning rate.
- Regularization: 
If the gap between train and dev accuracies is large(overfitting), increase the regularization constant.

## Gradient of different parts.
- Gradient of activation function is element-wise multiplication.
- Gradient of matrix multiplication is the same.

