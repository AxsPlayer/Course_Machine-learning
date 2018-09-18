# Note of Course 16.

## Why?
- Can all NLP tasks be seen as question answering problems?
- Leads to invent the dynamic memory network.
- Goal: A joint model for general QA.

## Major Obstacle.
- First Major Obstacle: For NLP no single model architecture with consistent state of the art results across tasks.
	- QA: Strongly Supervised MemNN.
	- Sentiment Analysis: Tree-LSTMs.
	- Part of speech tagging: Bi-directional LSTM-CRF.
- Second Major Obstacle: Fully joint multitask learning(meaning same decoder or classifier and not only transfer learning) is hard.
	- Usually restricted to lower layers.
	- Usually helps only if tasks are related.
	- Often hurts performance if tasks are not related.
- Dynamic memory networks only tackle first obstacle.

## Dynamic Memory Network.
- Semantic Memory Module: Glove vectors.
- Input Module: GRU sequence model for input sentences as well as every word and output the hidden state for every word.
- Question Module: GRU sequence for question sentences in the same method above. Output the final one question vector for answer module.
- Episodic Memory Module: GRU sequence for input from hidden state of input module triggered by the output of the output hidden state from the question module. (Attention Model). There are two layers, the first layer is triggered by the question vector and then the second layer is triggered by the question vector as well as the final vector from the first layer, meaning to find the answer in sentences according to the question in two stages.
- Answer module: Another GRU with memory input and question input to produce the answers.(with softmax)

## Comparison to MemNets.
- Similarities:
	- MemNets and DMNs have input, scoring, attention and response mechanisms.
- Differences:
	- For input representations MemNets use bag of word, nonlinear or linear embeddings that explicitly encode position.
	- MemNets iteratively run functions for attention and response.
	- DMNs show that neural sequence models can be used for input representation, attention and response mechanisms, naturally captures position and temporality.
	- Enables broader range of applications.

## Eposide number of input.
- DNMs can be used for sentiment analysis.
- The eposid number of input is dependent on the task, for some tasks, it needs 5 times to review the input to get the better results, and for sentiment analysis, it may only need 2 times review.
- Should the weights in each iteration share? The answer may depend on the how much training data you have. If you have bunch of training data, the more parameters will have better result, thus separate weights for each iteration is necessary.
- Trick: If you change the sentences input into the image input, then the system will give answer related to images.
