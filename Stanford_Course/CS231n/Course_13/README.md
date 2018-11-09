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
- encoder latent features, and sample from probabilistic generation of data.(data likelihood)
- Generate data: use decoder network, sample z from prior.
- Probabilistic spin to traditional autoencoders -> allows generating data.
Define intractable density function with latent z.
- pros: principled approach to generative models. And allows inference of q, can be useful feature representation.
- cons: not accurate as pixelCNN.

## GANs.
- don't work with any explicit density function, but use game theory.
- Problem: want to sample from complex, high-dimensional trainingng distribution. No direct way to this. Solution: sample from a simple distribution, e.g. random noise. Learn transformation to training distribution.
- training GANs: two-player game.
	- generator network: try to fool the discriminator by generating real-looking images.
	- Discriminator network: try to distinguish between real and fake images.
- Train jointly in minimax game. Alternate between: Gradient ascent on discriminator and gradient descent on generator. In practice, optimizing this generator objective does not work well.  To solve this problem, instead of minimizing likelihood of discriminatory being correct, now maximize likelihood of discriminator being wrong. Same objective of fooling discriminator, but now higher gradient signal for bad samples => works much better! Standard in practice. (For the loss gradient is flat in the beginning at first. Thus convert the direction.) Thus, in the bad sample distribution, the model learns faster.
- Interpretable vectors math.
- Pros: state of art
- Cons: trickier / more unstable to train, and; t solve inference queries such as px and.
- Conditional GANs, GANs for all kinds of application.


