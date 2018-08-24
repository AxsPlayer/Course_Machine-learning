# Note of Course 7.

## Tensorflow introduction.
- Node in computation graph: Every node in graph is operation, and every edge in graph is tensor.

## How to train Tensorflow?
The train_op with equation to optimization is also a node in computation graph. And when run this operation, the gradients of each node and variable is automatically computed and the variables are automatically updated with corresponding gradients.

## How to share variables in multiple GPUs?
The initial naive thinking is that we can build dictionary on top of code to define key as variable name and value. However, the shortcoming of this method is that it will be too large.
The method in Tensorflow is that it will define the variable scope for all the variables. And you can create or fetch certain variables using function ‘get_variable’.