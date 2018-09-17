# Note of Course 13.

## The disadvantage of RNN.
- Recurrent neural nets cannot capture phrases without prefix context, and often capture too much of last words in final vector. (If you just wanna keep track of several certain words, but RNN would go through all the sentence and mix all the context information with target phrases.)
- That’s why use CNN to resolve the problem.

## Main CNN idea.
- What if we compute vectors for every possible phrase? Regardless of whether phrase is grammatical or not very linguistically or cognitively plausible.
- Advantage: compute parallel.

## History of CNN in NLP.
- Single layer CNN: The filter is a vector to sum up several word vectors to CNN layer.

## The problems.
- The center word will get much more attention? A: The filter will take care of that with the weights in filter.
- What if the lengths of sentences differ? A: Add some pooling layers will deal with this problem.

## Structure of CNN.
- The advantage of CNN with pooling layer: This combination would handle variant length of sentences.
- Multiple filters: Every filter will catch one pattern of sentence patterns, maybe bigram, maybe trigram, and so on so forth. The filters are initialized with different values, and even if the initial value is the same, because the max pooling layer, in the different stage, the filters will become different.
- Why to use max pooling rather than the min pooling?
The reason is that if use min pooling, in reLu, the gradient will always be zero. The filter reasoning is that it wants to fire for particular patterns, thus though there is not beautiful math reason, but the max pooling method will fire for particular similarity pattern. Thus, using average pooling is also not a good idea to catch some particular pattern.
- Initialization is very important for weight matrix, or the model will learn nothing.

## Multi-channel idea.
- Initialize with pre-trained word vectors.
- Start with two copies.
- Backdrop into only one set, keep other “static”.
- Both channels are added to ci before max-pooling.
- Reasons:
	- One reason is that the word vectors will change in the supervised tasks. Thus, use original vectors is to keep similarity metric.
Double the neural network size, but not back-propagation for original part word vectors.

## Research highlight.
- character-level neural network: use CNN + LSTM for character-level prediction. 
- it’s about trade-off of time versus accuracy(2%-5%).

## Tricks to make it work better
- Dropout: Randomly mask to 0 some of the feature weights z. Reasoning: prevents co-adaptation(overfitting to seeing specific feature constellations). And when test time, the feature vectors are larger, thus, we should scale final vector by Bernoulli probability p, which means times p. There are two kind of dropout, one is weight dropout for weight matrix, and the other is activation dropout for node dropout.
- Ensemble: The same hyper-parameters will get to different local-opt thus to the different models. Then you can average the performance of top 5 best model during your training process.
- average weight rather than predictions, for size of neural network.

## Tricks.
- Always we should use train and dev dataset to retrain model after training process to choose the best set of hyper-parameters, especially for convex problem. But for non-convex problem like neural network, we may not train again for it may lead to the local optimum point.

## Tree-LSTMs is a good choice.

## CNN application: Translation.
= Uses CNN for encoding and RNN for decoding, for Neural machine translation.