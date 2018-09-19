# Note of Course 17. (Issues in NLP and Possible Architectures for NLP)

## What has been lost from old NLP work?
- An earlier era of work had lofty goals, but modest realities.

## History of NLP.
- The unified theory of inference: System had 6 general forms of inference; 2 pairs, so 4 basic types.
	- Elaboration: Filling a slot to connect two entities.
	- Reference Resolution.
	- View Application.
	- Concretization: Infer more specific.
- Improvement: What do we still need?
	- BiLSTMs with attention seem to be taking over the field and improving our ability to do everything.
	- Problems:
	1. We still have very primitive methods for building and accessing memories or knowledge.
	2. Current models have almost nothing for developing and executing goals and plans.
	3. We still have quite inadequate abilities for understanding and using inter-sentential relationships.
	4. We still can’t, at a large scale, do elaborations from a situation using common sense knowledge.

## TreeRNN.
- Disadvantage: TreeRNN cannot parallelize for different sentences have different structures.
- Solution: To deal with the above problem, there are several models.
	- The Shift-reduce Parser-Interpreter NN(SPINN): It can train on batch .
	- NLI with Tree-RNN sentence rep’s: Use TreeRNN to represent sentence using vectors.

## Brief Interlude.
- Models of copying/pointer networks: The network to copy or point the same word in the output sequence(like some rare name, the network just want to copy word rather than translating). In NMT or text summarization, it’s a attachment too NMT or main model.

## Models below the word level.
- Reasons:
	- Need to handle large, open vocabulary.
	- Word embeddings can be composed from character embeddings. Generates embeddings for unknown words, similar spellings share similar embeddings, solves OOV problem.
	- Character-level model for word2vec.
- Byte pair encoding:
	- add most frequent ngram pair into character dictionary. (new ngram)

## Hybrid NMT.
- A best-of-both-worlds architecture.
	- Translate mostly at the word level.
	- Only go to the character level when needed.
	- The disadvantage is it’s slow.
- Using word-level LSTM, if the input or output word is unknown, then take character-level LSTM to produce the word.