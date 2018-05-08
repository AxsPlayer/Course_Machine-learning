# !/usr/bin/python
# -*- coding: utf-8 -*-
################################################################################
#
# 2018 Personal.
#
################################################################################
"""
TensorFlow code to train and predict using Neural Network with MNIST data set.

Authors: AxsPlayer
Date: 2018/05/06
"""
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# Define some constants or parameters necessary.
# ----------------------------------------------
# Dataset related constants.
INPUT_NODE = 784  # Node number of input layer.
OUTPUT_NODE = 10  # Node number of output layer.

# Parameters of Neural Network.
LAYER1_NODE = 500  # One latent layer Neural Network.
BATCH_SIZE = 100  # Number of training samples in one batch.
LEARNING_RATE_BASE = 0.8  # The initial learning rate.
LEARNING_RATE_DECAY = 0.99  # The decay rate of learning rate in each iteration.
REGULARIZATION_RATE = 0.0001  # The coefficient of regularization term in loss function.
TRAINING_STEPS = 3000  # How many batches in total training process.
MOVING_AVERAGE_DECAY = 0.99  # The Moving average decay for moving average model.


def inference(input_tensor, weights1, biases1, weights2, biases2, avg_class=None):
    """Infer output of Neural Network.

    According to input tensor, infer the corresponding output of Neural Network.

    :param input_tensor: The input tensor as data source.
    :param weights1: The weight-parameters of latent layer.
    :param biases1: The bias-parameters of latent layer.
    :param weights2: The weight-parameters of output layer.
    :param biases2: The bias-parameters of output layer.
    :param avg_class: The average values of parameters, which represent whether
                    calculate moving average value of parameters and moving average model.

    :return: The output of Neural Network, given the input.
    """
    # If avg_class is none, use parameters' values directly, or, using moving average values.
    if avg_class is None:
        # Calculate the first layer result, with ReLU activation function.
        layer1 = tf.nn.relu(tf.matmul(input_tensor, weights1) + biases1)

        # Don't add softmax activation function, for it's contained in loss function calculation.
        return tf.matmul(layer1, weights2) + biases2
    else:
        # Calculate output using moving average parameters.
        layer1 = tf.nn.relu(tf.matmul(input_tensor, avg_class.average(weights1)) + avg_class.average(biases1))

        return tf.matmul(layer1, avg_class.average(weights2)) + avg_class.average(biases2)


def train(mnist):
    """Train the Neural Network.

    Training the Neural Network with given data source.

    :param mnist: The data source of mnist.

    :return: None. Save the model in training process.
    """
    # Define the structure of Neural Network.
    # ---------------------------------------
    # Set the placeholder for input data.
    x = tf.placeholder(tf.float32, [None, INPUT_NODE], name='x-input')
    y_ = tf.placeholder(tf.float32, [None, OUTPUT_NODE], name='y-input')
    # Define the variables of weights and bias.
    weights1 = tf.Variable(tf.truncated_normal([INPUT_NODE, LAYER1_NODE], stddev=0.1))
    biases1 = tf.Variable(tf.constant(0.1, shape=[LAYER1_NODE]))
    weights2 = tf.Variable(tf.truncated_normal([LAYER1_NODE, OUTPUT_NODE], stddev=0.1))
    biases2 = tf.Variable(tf.constant(0.1, shape=[OUTPUT_NODE]))
    # Calculate the inference of Neural Network.
    y = inference(x, weights1, biases1, weights2, biases2, None)
    # Calculate the Neural Network loss using cross entropy.
    cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=y, labels=tf.arg_max(y_, 1))
    cross_entropy_mean = tf.reduce_mean(cross_entropy)
    # Calculate the L2 regularization term.
    regularizer = tf.contrib.layers.l2_regularizer(REGULARIZATION_RATE)
    regularization = regularizer(weights1) + regularizer(weights2)
    # Calculate the total loss.
    loss = cross_entropy_mean + regularization
    # Define the steps of training process.
    global_step = tf.Variable(0, trainable=False)  # Set the trainable to False, thus it cannot be trained.
    # Set the current learning rate.
    learning_rate = tf.train.exponential_decay(LEARNING_RATE_BASE, global_step,
                                               mnist.train.num_examples / BATCH_SIZE,
                                               LEARNING_RATE_DECAY)
    # Define the method of optimization.
    train_step = tf.train.GradientDescentOptimizer(learning_rate). \
        minimize(loss, global_step=global_step)

    # Define the additional structure of Neural Network.
    # --------------------------------------------------
    # Set moving average variables.
    variable_averages = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY, global_step)
    # Apply the moving average to all the variables.
    variables_averages_op = variable_averages.apply(tf.trainable_variables())
    # Calculate the inference after applying moving average variables.
    average_y = inference(x, weights1, biases1, weights2, biases2, variable_averages)
    # Group the training step with moving average parameters in back-forward training process.
    train_op = tf.group(train_step, variables_averages_op)

    # Define the metrics of Neural Network.
    # -------------------------------------
    # Define the correct accuracy.
    correct_prediction = tf.equal(tf.arg_max(average_y, 1), tf.arg_max(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    # Start session for training.
    # ---------------------------
    with tf.Session() as sess:
        # Initialize the variables.
        tf.global_variables_initializer().run()
        # Prepare the validation data, thus to stop in time.
        validate_feed = {x: mnist.validation.images,
                         y_: mnist.validation.labels}
        # Prepare the test data to test model's performance.
        test_feed = {x: mnist.test.images,
                     y_: mnist.test.labels}

        # Starting training Neural Network with given training steps.
        for i in xrange(TRAINING_STEPS):
            # Print the validation accuracy in every 1000 step's training.
            if i % 1000 == 0:
                validate_acc = sess.run(accuracy, feed_dict=validate_feed)
                print("After %d training step(s), validation accuracy"
                      "using average model is %g " % (i, validate_acc))
            # Fetch one batch training data and training the model.
            xs, ys = mnist.train.next_batch(BATCH_SIZE)
            sess.run(train_op, feed_dict={x: xs, y_: ys})

        # After the whole training process, calculate the final accuracy of Neural Network.
        test_acc = sess.run(accuracy, feed_dict=test_feed)
        print("After %d training step(s), test accuracy using average model is %g"
              % (TRAINING_STEPS, test_acc))


def main():
    """The main function to train the model.

    :return: The information of training process and final accuracy of model.
    """
    # Import or download the mnist data, from target file path.
    mnist = input_data.read_data_sets("Data/", one_hot=True)

    # Train and test model.
    train(mnist)


if __name__ == '__main__':
    # This function will run the main function above.
    tf.app.run()

