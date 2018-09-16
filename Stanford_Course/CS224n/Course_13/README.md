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
- Multiple filters: Every filter will catch one pattern of 
 