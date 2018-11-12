# Note of Course 14.(Efficient Methods and Hardware for Deep Learning)

## Model problems.
- The first challenge: Model Size.
- The second challenge: speed.
- The third challenge: Energy Efficiency.
- algorithm and hardware co-designed.

## Solutions.
- Number representation.

## Algorithms for efficient inference.
- Pruning
	- prune the network weights
	- 90% parameters are not useful for accuracy
- Weight Sharing
	- class the weights and represent centroid.
	- huffman coding.
	- SqueezeNet: compress the convolutional layer.
- Quantization
	- convert float into 8-bit integer.
- Low Rank Approximation
	- SVD, conv layer into two layers.
- Binary / Ternary Net
	- multiple weights into three weights
- Winograd Transformation

## Hardware for Efficient Inference.
- Google TPU.

## Algorithms for efficient training.
- Parallelization
	- data-parallel
	- model-parallel
- mixed precision with FP16 and FP32
	- input is FP16
- Model Distillation.
	-  student model
- Dense Sparse Dense Training.
	- prune the network and train again.
	- regularization.

## 

