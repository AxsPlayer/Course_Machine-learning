# Note of Course 18. 
(Tackling the Limits of Deep Learning for NLP)

## The baseline model for PA4.
- Question -> LSTM -> q
- input -> LSTM -> x_i at each word
- classify_with_neural_net(q, x_i) to predict start
- classify_with_neural_net(1, x_i) to predict end

## The Limits of Single Task Learning.
- Great performance improvements.
- Projects start from random.
- Single unsupervised task can’t fix it.
- How to express different tasks in the same framework. (Dynamic memory network)
- Multitask learning: Just share word2vec (low layer) rather than LSTM layer.
- Joint Training model for multitasks improve for small data for transfer learning.
- Tackling Obstacle by predicting unseen words: Using pointer models and copy the input word to output word in machine translation model.
- Multi-question is independent: Contention Encoder. 
- RNNs are Slow: Take the best and parallelizable parts of RNNs and CNNs.
	- Quasi-Recurrent Neural Network: Combines best of both model families.
	Convolutions for parallelism across time. Element-wise gated recurrence for parallelism across channels.
- Architecture Search is Slow: Use AI to find the complex neural networkk and architecture for any problem. (Reinforcement Learning)

## Research Highlight.
- Neural Turing Machine: Read and write with outside memory module with attention mechanism.