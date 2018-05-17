# !/usr/bin/python
# -*- coding: utf-8 -*-
################################################################################
#
# 2018 Personal.
#
################################################################################
"""
TensorFlow code to train and predict using LeNet-5 Neural Network with MNIST data set.

Authors: AxsPlayer
Date: 2018/05/1
"""
import tensorflow as tf

# Define some constants or parameters necessary.
# ----------------------------------------------
# Data Info.
IMAGE_SIZE = 28
NUM_CHANNELS = 1
NUM_LABELS = 10
# The first convolution layer's parameters.
CONV1_DEEP = 32
CONV1_SIZE = 5
# The second convolution layer's parameters.
CONV2_DEEP = 64
CONV2_SIZE = 5
# The fully-connected layer's parameters.
FC_SIZE = 512


def inference(input_tensor, train, regularizer):
    """Define inference process of LeNet-5 Neural Network.

    Infer and fetch result of LeNet-5 with given input tensor.

    :param input_tensor: The input tensor which will be used to infer output of LeNet-5.
    :param train: The parameter which claims whether inference process is used in training or not.
    :param regularizer: The parameter to define regularization term or None with no regularization.

    :return: The inference output of LeNet-5 according to input tensor.
    """
    # Use variable scope to define Network Structures.
    # ------------------------------------------------
    # First convolution layer.
    with tf.variable_scope('layer1-conv1'):
        # Define the Layer1 parameter.
        conv1_weights = tf.get_variable("weight", [CONV1_SIZE, CONV1_SIZE, NUM_CHANNELS, CONV1_DEEP],
                                        initializer=tf.truncated_normal_initializer(stddev=0.1))
        conv1_biases = tf.get_variable("bias", [CONV1_DEEP], initializer=tf.constant_initializer(0.0))
        # Define the filters and output of layer1.
        conv1 = tf.nn.conv2d(input_tensor, conv1_weights, strides=[1, 1, 1, 1], padding='SAME')
        relu1 = tf.nn.relu(tf.nn.bias_add(conv1, conv1_biases))

    # Second max pooling layer.
    with tf.name_scope('layer2-pool1'):
        pool1 = tf.nn.max_pool(relu1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

    # Third convolution layer.
    with tf.variable_scope('layer3-conv2'):
        conv2_weights = tf.get_variable('weight', [CONV2_SIZE, CONV2_SIZE, CONV1_DEEP, CONV2_DEEP],
                                        initializer=tf.truncated_normal_initializer(stddev=0.1))
        conv2_biases = tf.get_variable('bias', [CONV2_DEEP], initializer=tf.constant_initializer(0.0))
        # Define the filters and output of layer3.
        conv2 = tf.nn.conv2d(pool1, conv2_weights, strides=[1, 1, 1, 1], padding='SAME')
        relu2 = tf.nn.relu(tf.nn.bias_add(conv2, conv2_biases))

    # Fourth max pooling layer.
    with tf.name_scope('layer4-pool2'):
        pool2 = tf.nn.max_pool(relu2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

    # Convert output into list for full-connected layer's input.
    pool_shape = pool2.get_shape().as_list()
    nodes = pool_shape[1] * pool_shape[2] * pool_shape[3]  # pool_shape[0] is the batch number.
    reshaped = tf.reshape(pool2, [pool_shape[0], nodes])

    # Fifth fully connected layer.
    with tf.variable_scope('layer5-fc1'):
        fc1_weights = tf.get_variable('weight', [nodes, FC_SIZE],
                                      initializer=tf.truncated_normal_initializer(stddev=0.1))
        # Add regularization term.
        if regularizer is not None:
            tf.add_to_collection('losses', regularizer(fc1_weights))
        fc1_biases = tf.get_variable('bias', [FC_SIZE], initializer=tf.constant_initializer(0.1))
        # Define the activation function and dropout.
        fc1 = tf.nn.relu(tf.matmul(reshaped, fc1_weights) + fc1_biases)
        if train:
            fc1 = tf.nn.dropout(fc1, 0.5)  # If training data, set dropout ratio.

    # Sixth fully connected layer.
    with tf.variable_scope('layer6-fc2'):
        fc2_weights = tf.get_variable('weight', [FC_SIZE, NUM_LABELS],
                                      initializer=tf.truncated_normal_initializer(stddev=0.1))
        # Add regularization term.
        if regularizer is not None:
            tf.add_to_collection('losses', regularizer(fc2_weights))
        fc2_biases = tf.get_variable('bias', [NUM_LABELS], initializer=tf.constant_initializer(0.1))
        # Define the activation function and dropout.
        logit = tf.nn.relu(tf.matmul(fc1, fc2_weights) + fc2_biases)

    return logit
