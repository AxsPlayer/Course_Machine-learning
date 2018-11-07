# Note of Course 13.(Generative Models)

## Unsupervised learning.
- Autoencoders: feature representation, through reconstructing input data.
- density estimation.
- Generative models
	- Given training data, generate new samples from same distribution.
	- Addresses density estimation, a core problem in unsupervised learning.
	- Explicit density estimation: explicityly define and solve for p
	- or implicit density estimation: learn model that can sample from p  without explicitly define the p.

## PixelRNN and PixelCNN
- fully visible belief network: explicit density model.
- chain rule of likelyhood.
- PixelRNN:
	- generate image pixels and dependency on previous pixels modeled using an RNN.
	- drawback: sequenctial generation is slow.
- PixelzCNN
	- denpendency on previous pixels now odeled using a CNN over context region.
	- sensitive to initial pixel and distribution.
- pros
	- can explicitly compute likelihood px
	- explicit likelihood of training data gives good evaluation metric
	- good samples
- Con:
	- sequential generation is slow.

## variational autoencoder.
- cannot optimize directly, define low bound.
- CNN autoencoder: use features to initialize a supervised model. When we have small data.
- probabilistic spin on autoencoders - will let us sample from the model to generate data.

