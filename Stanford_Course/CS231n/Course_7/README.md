# Note of Course 7.(Training Neural Networks)

## Data Normalization.
- Before normalization: classification loss very sensitive to changes in weight matrix, hard to optimize.
- After normalization: less sensitive to small changes in weights, easier to optimize.

## SGD problem.
- Condition number: If the condition number is too large, then the SGD optimization will be bad performed in this kind of situation.
- Local minima or saddle point: SGD will get stuck. 
- When the parameter space is large, the saddle point problem will be serve than local minima for the local minima requires that all the parameters are in the local minima.
- Solution: SGD + Momentum. The idea is that take the weighted average of velocity and the gradient, thus to point at the less noisy direction.
- AdaGrad: Added element-wise scaling of the gradient based on the historical sum of squares in each dimension. The problem is that the square scaling will be larger and larger as the training process. Then we introduce the RMSProp, which add the decay rate to square scaling number.
- In general, we tend not to use AdaGrad. 
- Adam: Mix momentum and RMSProp. It's default. 
- The problem: if the map is rotated, then Adam cannot deal with it for it only solve the problem along the axis.
- The learning rate decay is common in algorithm with momentum, but not common with  Adam.

## Second-order optimization.
- not need learning rate.
- But calculation is bad.(Hession matrix)
- In practice
	- Adam is common
	- If you can hold full batch train data, then try second-order.

## Model Ensembles.
- Train multiple independent models.
- At test time average their results.
- Tips and tricks: use multiple snalshots of single model during training.
- Instead of using actual parameter vector, keep a moving average of the parameter vector and use that at test time.

## Regularization.
- Add term to loss. (L1 + L2) But L2 loss may not make a lot sense in nueral network.
- Dropout: 0.5 is common. One interpretation is that the network cast the importance to all the features to prevent overfitting. Another interpretation is that the dropout is ensemble of models.

