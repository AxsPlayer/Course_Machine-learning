# Note of Course 12.(Visualizing and Understanding)

## First Layer: Visualize Filters.
- but visualize the higher layers weights is difficult and not that interesting.

## Last Layer.
- visualize the last feature vector.

## Visualize activation maps out of convolutional layer.
- every grid may search for some patterns.
- Maximally activating patches.

## Occlusion experiments.
- exclude some part of images, if the prob of classification score cahnges a log, thus this part will be important.

## Saliency Maps.
- How to tell which pixels matter for classification.
- Compute gradient of class score with respect to image pixels, take absolute value and max over RGB.
- Also use it to perform semantic segmentation, without labeled data.

## Intermediate features via (guided) backprop.
- compute gradient of neuron value with respect to image pixels.

## Visualizing CNN features: Gradient ascent
- fix the weight of network, and change the image to maximize the score of network.

## Fooling images / Adversarial examples.
- steps:
	1. Start from an arbitrary image.
	2. Pick an arbitrary class
	3. Modify the image to maximize the class
	4. Repeat until network is fooled.

## DeepDream: Amplify existing features.
- Just to look for features the layer look for.
- set the gradient to the chosen layer's activation function value.

## Feature Inversion.
- run the image through the network.
- take some layer's representation of that image.
- reconstruct the image from the feature vector.

## Texture synthesis.
- Given a sample patch of some texture, build larger texture.
- Gram Matrix.

## Neural style transfer.
- Combine above two usage.
- it's slow: the solution is to use fast style transfer, try another network.

## Summary.
- activations:
- gradients:
- Fun: