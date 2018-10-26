# Note of Course 8.(Deep Learning Software)

## CPU vs. GPU.
- GPU can parallize well than CPU.

## Programming GPUs.
- CUDA(NVIDIA only)
	- write c-like code that runs directly on the GPU.
	- Higher-level APIs: cuBLAS, etc.
- For deep learning just use library.
- Communication: If you aren't careful, training can bottleneck on reading data and transferring to GPU.
	- Solutions:
		- Read all data into RAM.
		- Use SSD instead of HDD.
		- Use multiple CPU threads to prefetch data.

## Deep Learning Frameworks.
- Tensorflow/Pytorch
- copy data is expensive in GPU. Thus, we use variable for weights, which prevent the copying data from cpu to gpu.
- tf.layers automatically sets up weight and bias for us.
- Keras and TFLearn is the third party high-level API based on Tensorflow.
- tf.layers and TF-Slim and tf.contrib.learn are the ships with Tensorflow which are the different versions of Tensorflow API.
- Pretty Tensor is alsl from Google.
- Sonnet is from DeepMind.

## PyTorch
- Three Levels of abstraction.
	- Tensor: Imperative ndarray, but runs on GPU.
	- Variable: Node in a computational graph; stores data and gradient.
	- Module: A neural network layer; may store state or learnable weights, like the tf.layers, etc, high-level APIs.
- Tensorflow vs. PyTorch: static vs Dynamic Graphs, in PyTorch, every time nyou will build new tensor graph.

## Static vs Dynamic
- Static
	- with static graphs, framework can optimize the graph for you before it runs.
	- Once graph is built, can serialize it and run it without the code that built the graph.
- Dynamic
	- Graph building and execution are intertwined, so always need to keep code around.
	- makes your code a lot cleaner and easier.
	- In condition calculation, it's super easy
	- For loops condition, it's easy.
- TensorFlow Fold make dynamic graphs eahier in TensorFlow through dynamic batching.
- Applications:
	- Recurrent networks
	- Recursive networks
	- Modular Networks
- Tensorflow is both for research and production. But PyTorch is for research and the Caffe2 is more for production.
