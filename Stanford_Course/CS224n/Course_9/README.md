# Note of Course 9.

## The history of Machine Translation System.
- Traditional statistical machine translation system: Utilize Bayes rule, firstly build the translation model on parallel corpus and then build the language model just on one kind of language, then build the decoder of machine translation system on top of these two kind of language models.
	- Step 1: for training translation model-Alignment. To see which word in one language will translate to which word in another language, there are some kind of alignments, one is one-to-one, and another is many-to-one and so on, resulting in large search space after many steps.
	- Decode: Search for best of many hypotheses, called beam search.
	- The problem is that because the systems are independently trained on machine learning problems, thus it’s very complex and inefficient system. What the problem deep learning method deal with is that it applies end-to-end trainable model.

- Deep learning model system: 
	- Structure: One single RNN, consisting of encoder and decoder. After no input in RNN, the decoder output the translation results.
	- Improvement: 1. Each input of hidden vector has its own linear transformation. 2. Compute every hidden state in decoder from previous hidden state, last hidden vectors of encoder, and previous predicted output word. 3. Train stacked/deep RNNs with multiple layers. 4. Potentially train bidirectional encoder.(not very common) 5. If you don’t do step 4, you can train input sequence in reverse order for simpler optimization problem, as more training data. The reason why the reverse direction works is that the RNN doesn’t need grammar information and it only considers correlations.

## Break time.
Improve language modeling:
- Better Inputs: word(glove) -> sub word(morpheme/BPE) -> char(char-level embedding)
- Better regularization/Preprocessing
	- regularization: 1. use dropout 2. use stochastic feedforward depth 3. use norm stabilization
	- preprocessing: 1. randomly replacing words in a sentence with other words 2. or use bigram statistics to generate Kneser-Ney inspired replacement.
- Better Model(and all above)
	The method is similar to the method in computer vision as data augmentation, which means to replace word with some kind of rules such as draw word from a proposal distribution. The improved result is that you will get a smoothing representation of word.

## Main Improvement: Better Units. (Gated Recurrent Units(GRU))
- Main ideas: 1. keep around memories to capture long distance dependencies. 2. allow error messages to flow at different strengths depending on the inputs.
- GRU units: 1. update gate and reset gate, calculation using the hidden state, as well as the input word vector, the same form as in simple RNN, but with the different weight matrix. Another thing is that the activation function of gates is sigmoid, thus every elements in gates is between 0 and 1. 
	- reset gate: If reset gate unit is ~0, then this ignores previous memory and only stores the new word information.
	- update gate: Update gate decides when to update and how much to update the information.
	- The advantage of GRU, compared to simple RNN: The GRU could decide when and how much to reset and update previous information in neural network. In RNN, the previous information is averaged and washed as words go on.
	- Why we should set two kinds of gates: The one reason is that when we use reset gate, we can filter the importance of x information out of the combination of x information and ht-1(previous state) information.

## LSTM.
- Gates unit: Input gate to decide whether to input current cell. Forget gate to decide whether to forget past information. Output gate to decide how much cell is exposed.
- Gradient vanishing problem: LSTM also has some kind of vanishing problem, but much less. It helps the information collection problem but not with engineering problem.
- Sentence vector representation: Extract the hidden state of last encoder output.

# Some variant of LSTM.
- Pointer for previous word to predict unseen word in the training stage.

