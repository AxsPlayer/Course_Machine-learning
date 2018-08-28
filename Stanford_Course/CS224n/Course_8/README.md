# Note of Course 8.

## The history of Language model.
- Traditional language model: The next word is based on the previous words appearing in the sentence. And the simple version is that probability is conditioned on a window of n previous words. And the probability is count-based.
- Recurrent Neural Network Language Model: 
	- In each single time step, it’s the same that concatenate ht-1 and x to just adding them up and times weight. The result will be the same.
	- Problem with gradient: The signal of gradients will become too strong or too weak after long sequence. One is vanishing gradient problem, and the other is exploding gradient problem. The source of this gradient problem is that after long sequence of applying chain-rule gradient to hidden values, and according to upper boundary of gradient, the gradient will vanish or explode, depending on the norm of weight matrix.
	- The result of gradient problem: Thus, the sequence as input to predict next word in RNN cannot be too long, which would lead to the problem that RNN could not catch as much information as needed to predict the next word, especially in language model situation.
	- The ways to deal with gradient problem:
		- Exploding gradient: Use cut-edge method to set maximum value, if gradient exceeds this maximum value, then set it to maximum value. The idea is inspired by the visualization of parameter space of optimization of simple RNN.
		- Vanishing gradient: Cannot use the above same method, for it would leads to assign too much importance to words far away from target word. Thus, the solution to this kind of situation is to initialize weight matrix to identity matrix and use reLU as activation function. The reasoning behind the first solution is when we don’t known the situation of projection, we just average word vectors, then update.

## NLP metric.
- Perplexity: One kind of measure method about the number of possible words to be selected.

## Softmax to predict next word is slow in terms of speed.
- Class-based method to deal with this problem. The concrete steps are, firstly, predict next word’s class based on the history and predict the word based on the class. The more classes used, the more precise prediction but slower speed.

## Problem about back-propagation.
- The efficient method is to apply back-propagation one time through all the sequence, not applying at each time step.

## Usage of RNN.
- The Named Entity Recognition using RNN.
- Opinion mining using RNN, such as DSEs(direct subjective expressions) and ESEs(expressive subjective expressions). Entity of long sequence.

## Optimization of RNN.
- Use bi-directional RNN, to utilize the information not only from the left sequence, but also from the right sequence.