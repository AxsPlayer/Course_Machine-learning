# Note of Course 11.(Detection and Segmentation)

## Semantic Segmentation.
- predict classification for every pixels.
- doesn't differentiate the instances.
	- sliding windows
	- fully convolutional network. (Super expensive) change to downsampling ans upsampling inside the network.
	- upsampling:
		- unpooling: nearest neighbor and bed of nails and max unpooling
		- learnable upsampling: Transpose Convolution.

## Classification + Localization.
- only single object(fix number)
- apply two tasks in the same time
	- classification
	- boundary prediction(regression)
	- weighted sum up the two losses and backprop.
	- using transfer learning.
	- other usage: human pose estimation.
 
## Object detection.
- varying number of output in the images.
- tries:
	- sliding window：The problem is you need to apply CNN to huge number of locations and scales, very computationally expensive.
	- region proposals(R-CNN)
		- find 'blobby' image regions that are likely to contain objects
		- relatively fast.
		- The region proposals algorithm are fixed and not learned using the traditional algorithm.
		- The proposal classification algorithm uses neural network to learn.
		- it's slow because there are too many proposals.
	- Fast R-CNN:
		- run the image through convolutional network, get high resolution convolutional feature map.
		- selective search on feature map(reuse the low layers)
		- reshaping the proposals using ROI pooling layer.
	- Faster R-CNN:
		- making the network to predict its own region proposals.
	- YOLO(you only look once) / SSD(single shot detection) (not region-based proposal methods)
		- split the image into several grid, and set windows in each grid, then use classification and regression network to predict the results of these windows.
	- Takeaways:
		- Faster R-CNN is slower but more accurate
		- SSD is much faster but not as accurate
	- Object Detection + captioning = Dense captioning

## Instance segmentation.
- like the hybrid of object detection and semantic segmentation.
- Mask R-CNN: similar like the faster R-CNN.
	