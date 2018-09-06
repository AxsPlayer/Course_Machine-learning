# Note of Course 11.

## GRU pros.
- Problem: The simple RNN has the problem that vanishing gradient is super-problematic. (When vanishing gradient, we cannot tell whether no dependency between t and t+n in data, or wrong configuration of parameters(the vanishing gradient condition)). The main cause is the naive transition function.
- The improvement of GRU: It implies that the error must back propagate through all the intermediate nodes. Perhaps we can create shortcut connections between each pair of nodes. Thus use update gate, and use reset gate to forget some unnecessary info.
- Why: The reason is that the relation between ht and ht-1 is linear, thus the gradient flows perfectly through time line.
- LSTM: Why the name is long-short term memory neural network, the realson is that the LSTM can store or remember length of 100 time steps.

## Advice for training a gated RNN.
- 1. Use an LSTM or GRU.
- 2. Initialize recurrent matrices to be orthogonal.
- 3. Initialize other matrices with a sensible(small) scale.
- 4. Initialize forget gate bias to 1: default to remembering.
- 5. Use adaptive learning rate algorithms: Adam
- 6. Clip the norm of the gradient: 1-5 seems to be a reasonable threshold when used together with Adam.
- 7. Either only dropout vertically or learn how to do it right.
- 8. Be patient.
- 9. Ensembles: Train 8-10 nets and average their predictions.

## Research highlight.
- Curriculum learning: Slowly increase the length of training sequences, and converges training faster, decreases overfitting.
- Scheduled Sampling: Randomly sample from previous prediction instead of ground truth during training, and makes training scenario more similar to testing.

## MT Evaluation.
- Manual: Adequacy and fluency.(best way till now)
- Testing in an application that uses MT as one sub-component.
- Automatic metric:
	- WER(word error rate) - why problematic?
	- BLEU(Bilingual Evaluation Understudy)

## BLEU.
- N-gram precision(score is between 0&1)
	- What percent of machine n-grams can be found in the reference translation.
- method: counts n-grams <= length k =4.

## The word generation problem.
- Word vocabulary is large and a lot of cost is on calculating softmax.
	- one way is to decrease the size of vocabulary.
	- one way is to use tree-structured vocabulary.
