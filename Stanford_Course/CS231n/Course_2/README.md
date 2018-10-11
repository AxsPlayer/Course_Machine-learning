# Note of Course 2.

## Image classification.
- The most common problem in computer vision. 
- The challenges is: 
	- One is the viewpoint variation, meaning if image changes a little, the pixels matrix will be totally different.
	- Another one is the illumination, light will be different.
	- Another one is the deformation, the different pose of animal, for example.
	- Background Clutter.
	- Intraclass.

## Classifier.
- First classifier: Nearest Neighbor. It's the easiest method to try at first and you can try different kind of distance. Different distance means different boundary. One of the disadvantage is that when testing, it's slow. Another one is L2 distance is not a good representation for the true distance, and also involve the curse of dimension problem.
- Linear classification: LR is one of the important component to the convolutional neural network. We can use the weight matrix learned from model to see what kind of patterns are learned from the data. The weight matrix will capture the pattern which to match every single image.