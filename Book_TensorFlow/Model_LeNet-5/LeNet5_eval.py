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
# Import necessary packages.
import time
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# Import train and inference scripts.
import LeNet5_inference
import LeNet5_train

# Define some constants.
# Define time interval to evaluate model performance.
EVAL_INTERVAL_SECS = 10


def evaluate(mnist):
    """Evaluate model performance on test data set.

    :param mnist: The input data set.

    :return: Print the performance of model.
    """
    # Create graph to save evaluating structure for independent analysis.
    with tf.Graph().as_default() as g:
        # Define input and output format.
        x = tf.placeholder(tf.float32, [None, LeNet5_inference.IMAGE_SIZE,
                                        LeNet5_inference.IMAGE_SIZE, LeNet5_inference.NUM_CHANNELS],
                           name='x-input')
        y_ = tf.placeholder(tf.float32, [None, LeNet5_inference.NUM_LABELS], name='y-input')
        validate_feed = {x: mnist.validation.images,
                         y_: mnist.validation.labels}


