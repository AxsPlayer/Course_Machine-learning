#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Import necessary packages.
import glob
import os.path
import numpy as np

import tensorflow as tf
from tensorflow.python.platform import gfile
import tensorflow.contrib.slim as slim
# Import pre-defined inception_v3 model structure.
import tensorflow.contrib.slim.python.slim.nets.inception_v3 as inception_v3

# Set global constants.
# ---------------------
# Set file paths.
INPUT_DATA = 'data/flower_processed_data.npy'  # The path to save processed data.
TRAIN_FILE = 'model/'  # The path to save trained model. First train fully-connected layer, then all the network.
CKPT_FILE = 'pre_model/inception_v3.ckpt'  # The file path to save pre-trained model from Google.
# Set global constants.
LEARNING_RATE = 0.0001
STEPS = 300
BATCH = 32
N_CLASSES = 5
# Set variables related to pre-trained model.
CHECKPOINT_EXCLUDE_SCOPES = 'InceptionV3/Logits,InceptionV3/AuxLogits'  # Exclude untrained FC parameters.
TRAINABLE_SCOPES = 'InceptionV3/Logits,InceptionV3/AuxLogits'  # The FC parameters which should be fine-tuned.


def get_tuned_variables():
    """Fetch tuned variables from pre-trained model.

    Fetch tuned variables, except for excluded parameters.

    :return: Tuned variables from pre-trained model.
    """
    # Parse exclusion parameters from global setting into list.
    exclusions = [scope.strip() for scope in CHECKPOINT_EXCLUDE_SCOPES.split(',')]

    # Fetch tuned variables from model.
    variables_to_restore = []
    for var in slim.get_model_variables():
        excluded = False
        for exclusion in exclusions:
            if var.op.name.startswith(exclusion):
                excluded = True
                break
        if not excluded:
            variables_to_restore.append(var)

    return variables_to_restore


def get_trainable_variables():
    """Fetch

    :return:
    """
    scopes = [scope.strip() for scope in TRAINABLE_SCOPES.split(',')]
    variable_to_train = []

    # List all the trainable variables, and add them into list.
    for scope in scopes:
        variables = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope)
        variable_to_train.extend(variables)

    return variable_to_train


def main():
    # Load preprocessed data.
    processed_data = np.load(INPUT_DATA)
    training_images = processed_data[0]
    n_training_example = len(training_images)
    training_labels = processed_data[1]
    validation_images = processed_data[2]
    validation_labels = processed_data[3]
    testing_images = processed_data[4]
    testing_labels = processed_data[5]
    print("%d training examples, %d validation examples and %d testing examples." %
          (n_training_example, len(validation_labels), len(testing_labels)))

    # Define the input of Inception-v3.
    images = tf.placeholder(tf.float32, [None, 299, 299, 3],
                            name='input_images')
    labels = tf.placeholder(tf.int64, [None], name='labels')

    # Define Inception model structure.
    with slim.arg_scope(inception_v3.inception_v3_arg_scope()):
        logits, _ = inception_v3.inception_v3(images, num_classes=N_CLASSES)
    # Fetch trainable variables.
    trainable_variables = get_trainable_variables()
    # Define loss function.
    tf.losses.softmax_cross_entropy(tf.one_hot(labels, N_CLASSES), logits, weights=1.0)
    # Define the training process.
    train_step = tf.train.RMSPropOptimizer(LEARNING_RATE).minimize(tf.losses.get_total_loss())

    # Calculate accuracy.
    with tf.name_scope('evaluation'):
        correct_prediction = tf.equal(tf.argmax(logits, 1), labels)
        evaluation_step = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    # Define the function to load the pre-trained model.
    load_fn = slim.assign_from_checkpoint_fn(CKPT_FILE, get_tuned_variables(), ignore_missing_vars=True)

    # Define the saver for newly trained model.
    saver = tf.train.Saver()
    with tf.Session() as sess:
        # Initialize the not assigned variables before loading the model.
        init = tf.global_variables_initializer()
        sess.run(init)

        # Load the model.
        print('Loading tuned variables from %s' % CKPT_FILE)
        load_fn(sess)

        # Start training.
        start = 0
        end = BATCH
        for i in range(STEPS):
            # Update pointed variables but not all the variables.
            sess.run(train_step, feed_dict={
                images: training_images[start: end],
                labels: training_labels[start: end]
            })

            # Output log.
            if i % 30 == 0 or i + 1 == STEPS:
                saver.save(sess, TRAIN_FILE, global_step=i)
                validation_accuracy = sess.run(evaluation_step, feed_dict={
                    images: validation_images,
                    labels: validation_labels
                })
                print('Step %d: Validation accuracy = %.1f%%' % (i, validation_accuracy * 100.0))

            # Update batch variables.
            start = end
            if start == n_training_example:
                start = 0
            end = start + BATCH
            if end > n_training_example:
                end = n_training_example

            # Test accuracy in test data.
            test_accuracy = sess.run(evaluation_step, feed_dict={
                images: testing_images,
                labels: testing_labels
            })
            print('Final test accuracy = %.1f%%' % (test_accuracy * 100))


if __name__ == '__main__':
    tf.app.run()






