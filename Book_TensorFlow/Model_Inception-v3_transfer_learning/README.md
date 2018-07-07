# Motivation?
This project is created to learn how to use Tensorflow to build Inception-v3 model with transfer learning
method.
The project aims to classify what kind of flower one picture belongs to.

## What's the technology?
The technology used is Tensorflow-Slim based on Tensorflow, as well as transfer learning.

## Preparation.
Prepare data: 
		
	wget http://download.tensorflow.org/example_images/flower_photos.tgz
	tar xzf flower_photos.tgz

The download data is saved in ./flower_photos/.

Prepare model:

	wget http://download.tensorflow.org/models/inception_v3_2016_08_28.tar.gz
	tar xzf inception_v3_2016_08_28.tar.gz

The download model is saved in ./pre_model/.

## How to Use?
- Prepare training data.

	python data_preparation.py

The original data is saved in ./flower_photos/. And the processed data is saved in ./data/.

- Train the model.

	python train.py

The saved model checkpoints are saved in ./model/.
