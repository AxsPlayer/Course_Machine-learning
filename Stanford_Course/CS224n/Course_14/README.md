# Note of Course 14.

## Tree recursive neural networks.
- Tree RNNs, the different part is tree parsing structure.

## Semantic interpretation of language- Not just word vectors.
- How can we know when larger units are similar in meaning?
semantic compositionally, thus can put together smaller pieces into larger pieces.
- Convert long phrases into vectors and calculate their similarity.
- The reason why you should put phrase vectors into the same space of word vectors is that the word vectors can represent much meanings as phrase vectors do.
- You can not store phrase vectors for every phrase for infinite numbers of phrases. But you should start from word vectors and use principle of compositionality.

## Is recursion useful?
- Helpful for some tasks to refer to specific phrases.
- Works better for some tasks to use grammatical tree structure. It’s a powerful prior for language structure.

## Recursive vs. recurrent neural networks.
- Recursive neural nets require a parser to get tree structure. That’s the main problem and it’s GPU unfriendly and more complex model structure.
- Recurrent neural nets cannot capture phrases without prefix context and often capture too much of last words in final vector.

## Relationship between RNNs and CNNs.
- RNN: Get compositional vectors for grammatical phrases only.
- CNN: Computes vectors for every possible phrase. Regardless of whether each is grammatical- many don’t make sense. Don’t need parser. But maybe not very linguistically or cognitively plau.

## How to parsing a sentence.
- Using Neural network to predict the pair-wise word combination score in greedy manner to create the sentence structure. And the Neural network will produce the combination of two child vectors into one phrase vector to represent the whole phrase meaning.

## Backpropagation through structure.
- Three differences resulting from the recursion and tree structure.
	- sum derivatives of W from all nodes (like RNN)
	- split derivatives at each node (for tree)
	- add error messages from parent + node itself

## Research highlight.
- maximum probability is not good target to produce a good response in Q&A.
- reinforcement learning maybe more useful in some area.

## History of treeRNN.
- Simple RNN: There is no real interaction between the input words, for the weight matrix is the same.
- Syntactically-United RNN
	- Compositional Vector Grammars: Problem is speed. Every candidate score in beam search needs a matrix-vector product. Solution is to compute score only for a subset of trees coming from a simpler, faster model(PCFG).
- Compositionally through recursive matrix-vector spaces: (Before the problem is that two word will not have any combination or interaction). One way to make the composition function more powerful was by untying the weights W. Thus, proposal is a new composition function, which means every word or phrase has its own matrix and vector representation, individually. 
- Trick: The simple RNN does well in many cases, and combine syntax and matrix-vector may do better.

