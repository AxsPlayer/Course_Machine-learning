# Note of Course 10.

## History.
- Traditional neural machine translation(NMT): The neural network consists of encoder and decoder in the same huge neural network.
- Modern sequence model for neural machine translation(NMT): The RNN consists of encoder and decoder.
	- conditional recurrent language model: produce Y using source language and translate into target language using Y.
- Improvement: In decoder, feed the Y into every time step.