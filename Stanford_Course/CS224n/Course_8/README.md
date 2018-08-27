# Note of Course 8.

## The history of Language model.
- Traditional language model: The next word is based on the previous words appearing in the sentence. And the simple version is that probability is conditioned on a window of n previous words. And the probability is count-based.
- Recurrent Neural Network Language Model: 
	- In each single time step, it’s the same that concatenate ht-1 and x to just adding them up and times weight. The result will be the same.
	- Problem with gradient: The signal of gradients will become too strong or too weak after long sequence. One is vanishing gradient problem, and the other is exploding gradient problem. The source of this gradient problem is that after long sequence of applying chain-rule gradient to hidden values, and according to upper boundary of gradient, the gradient will vanish or explode, depending on the norm of weight matrix.