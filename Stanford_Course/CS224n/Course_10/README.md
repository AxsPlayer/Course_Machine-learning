# Note of Course 10.

## History.
- Traditional neural machine translation(NMT): The neural network consists of encoder and decoder in the same huge neural network.
- Modern sequence model for neural machine translation(NMT): The RNN consists of encoder and decoder.
	- conditional recurrent language model: produce Y using source language and translate into target language using Y.
- Improvement: In decoder, feed the Y into every time step.

## Four big wins of Neural MT.
- End-to-end training. All parameters are optimized at the same time.
- Distributed representations share strength. Better exploitation of word and phrase similarities.
- Better exploitation of context. NMT can use a much bigger context, without sparse data problem.
- More fluent text generation. Deep learning text generation is much higher quality.

## What was not on the list of win of Neural MT.
- First: There is no black box component models for reordering, transliteration, etc.
- Second: Don’t use any of syntactic or semantic structures.
- Third: Don’t use any of discourse structure, anaphora, etc.

## Multilingual NMT system.
- Simplicity: single model
- Low-resource language improvements
- Zero-shot translation: Need no more training data for another pair of language translation.

## Introduce attention model.
- Reason: Because the initial NMT is based on the last hidden state of encoder to decode to another kind of language, thus it seems to be good on short sentences translation. But on long sentences, the performance is not good.
- Solution: Random access memory of pool of source states.
	- Retrieve the information as needed, pointing out which part would be translated next.
	- method: 
	1. Compare target and source hidden states and score each hidden state for attention model.
	2. Normalize and combine the memory hidden state according to their attention scores to create context vectors for predicting.
	3. Score function: the interaction of ht and hs to get the score. (ht*W*hs)
	4. Global vs. Local: Avoid focusing on everything at each time. Focus on the subset of source states（reinforcement learning）, especially would be good for long sequences. (RNN can handle short sentences, and LSTM can handle much longer to 30 words sentences, and the LSTM with attention can handle even more than 60 words sentences.)
	5. Entending attention with linguistic ideas previously in alignment models
		- NMT model with coverage-based attention.
		- More substantive models of attention using: position(IBM2) + Markov(HMM) + fertility(IBM3-5) + alignment symmetry(BerkeleyAligner)
	6. Decoding: Cannot try all the possible combinations, and one way is to use ancestral sampling, but the disadvantage is that it’s not stable and will give you different results every try. (pros: efficient and unbiased. cons: high variance, and pretty inefficient.) The second method is using greedy search. (pros: super-efficient, in terms of both computation and memory. cons: heavily suboptimal.)
The third way is to use beam search.
	The state of art is using beam search with small beam number.