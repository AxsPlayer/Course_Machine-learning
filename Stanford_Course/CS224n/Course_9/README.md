# Note of Course 9.

## The history of Machine Translation System.
- Traditional statistical machine translation system: Utilize Bayes rule, firstly build the translation model on parallel corpus and then build the language model just on one kind of language, then build the decoder of machine translation system on top of these two kind of language models.
	- Step 1: for training translation model-Alignment. To see which word in one language will translate to which word in another language, there are some kind of alignments, one is one-to-one, and another is many-to-one and so on, resulting in large search space after many steps.
	- Decode: Search for best of many hypotheses, called beam search.
	- The problem is that because the systems are independently trained on machine learning problems, thus it’s very complex and inefficient system. What the problem deep learning method deal with is that it applies end-to-end trainable model.

- Deep learning model system: 
	- Structure: One single RNN, consisting of encoder and decoder. After no input in RNN, the decoder output the translation results.