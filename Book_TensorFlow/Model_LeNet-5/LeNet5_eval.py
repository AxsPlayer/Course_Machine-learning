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

        # Calculate inference result, as well as accuracy of model.
        y = LeNet5_inference.inference(x, False, None)
        correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

        # Set mode of rename to load model, so as to deal with moving average variable problems.
        variable_averages = tf.train.ExponentialMovingAverage(LeNet5_train.MOVING_AVERAGE_DECAY)
        variable_to_restore = variable_averages.variables_to_restore()
        saver = tf.train.Saver(variable_to_restore)

        # Evaluate performance of model in fixed interval.
        while True:
            with tf.Session() as sess:
                # Find latest model file and load model.
                ckpt = tf.train.get_checkpoint_state(LeNet5_train.MODEL_SAVE_PATH)
                if ckpt and ckpt.model_checkpoint_path:
                    # Load model.
                    saver.restore(sess, ckpt.model_checkpoint_path)
                    # Fetch global steps in file name.
                    global_step = ckpt.model_checkpoint_path.split('/')[-1].split('-')[-1]
                    accuracy_score = sess.run(accuracy, feed_dict=validate_feed)
                    # Print the accuracy result.
                    print("After %s training step(s), validation accuracy = %g" % (global_step, accuracy_score))
                else:
                    print('No checkpoint file found.')
                    return
            # Set interval sleep time.
            time.sleep(EVAL_INTERVAL_SECS)


def main():
    mnist = input_data.read_data_sets("/path/to/mnist_data", one_hot=True)
    evaluate(mnist)


if __name__ == '__main__':
    tf.app.run()



