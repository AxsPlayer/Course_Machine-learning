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
Date: 2018/05/16
"""
import numpy as np
import os

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

import LeNet5_inference

# Define some constants or parameters necessary.
# ----------------------------------------------
# Parameters of Neural Network.
LAYER1_NODE = 500  # One latent layer Neural Network.
BATCH_SIZE = 100  # Number of training samples in one batch.
LEARNING_RATE_BASE = 0.8  # The initial learning rate.
LEARNING_RATE_DECAY = 0.99  # The decay rate of learning rate in each iteration.
REGULARIZATION_RATE = 0.0001  # The coefficient of regularization term in loss function.
TRAINING_STEPS = 3000  # How many batches in total training process.
MOVING_AVERAGE_DECAY = 0.99  # The Moving average decay for moving average model.
# The parameter to save model.
MODEL_SAVE_PATH = "/path/to/model/"
MODEL_NAME = "model.ckpt"


def train(mnist):
    """Train the Neural Network.

    Training the Neural Network with given data source.

    :param mnist: The data source of mnist.

    :return: None. Save the model in training process.
    """
    # Define the structure of Neural Network.
    # ---------------------------------------
    # Set the placeholder for input data.
    x = tf.placeholder(tf.float32,
                       [BATCH_SIZE, LeNet5_inference.IMAGE_SIZE,
                        LeNet5_inference.IMAGE_SIZE, LeNet5_inference.NUM_CHANNELS], name='x-input')
    y_ = tf.placeholder(tf.float32, [None, LeNet5_inference.NUM_LABELS], name='y-input')

    # Calculate the L2 regularization term.
    regularizer = tf.contrib.layers.l2_regularizer(REGULARIZATION_RATE)
    # Calculate the inference of Neural Network.
    y = LeNet5_inference.inference(x, True, regularizer)
    # Calculate the Neural Network loss using cross entropy.
    cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=y, labels=tf.arg_max(y_, 1))
    cross_entropy_mean = tf.reduce_mean(cross_entropy)
    # Calculate the total loss.
    loss = cross_entropy_mean + tf.add_n(tf.get_collection('losses'))
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

    # Group the training step with moving average parameters in back-forward training process.
    with tf.control_dependencies([train_step, variables_averages_op]):
        train_op = tf.no_op(name='train')

    # Initialize the model saver.
    saver = tf.train.Saver()

    # Start session for training.
    # ---------------------------
    with tf.Session() as sess:
        # Initialize the variables.
        tf.global_variables_initializer().run()

        # Starting training Neural Network with given training steps.
        for i in xrange(TRAINING_STEPS):
            # Prepare the training data.
            xs, ys = mnist.train.next_batch(BATCH_SIZE)
            # Reshape training data into suitable dimensions.
            reshaped_xs = np.reshape(xs, (BATCH_SIZE, LeNet5_inference.IMAGE_SIZE,
                                          LeNet5_inference.IMAGE_SIZE, LeNet5_inference.NUM_CHANNELS))

            # Train the Network.
            _, loss_value, step = sess.run([train_op, loss, global_step],
                                           feed_dict={x: reshaped_xs, y_: ys})

            # Print the validation accuracy in every 1000 step's training.
            if i % 1000 == 0:
                print("After %d training step(s), validation accuracy"
                      "using average model is %g " % (step, loss_value))
            # Save the model.
            saver.save(sess, os.path.join(MODEL_SAVE_PATH, MODEL_NAME),
                       global_step=global_step)


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
