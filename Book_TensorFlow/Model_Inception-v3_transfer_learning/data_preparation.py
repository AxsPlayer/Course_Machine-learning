#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
To fetch data, execute following scripts.
wget http://download.tensorflow.org/example_images/flower_photos.tgz
tar xzf flower_photos.tgz
This file is to convert original data into suitable format for model input.
"""
# Import necessary packages.
import glob
import os.path
import numpy as np
import tensorflow as tf
from tensorflow.python.platform import gfile

# Set global constants.
# File path constants.
INPUT_DATA = '/path/to/flower_photos'  # The input file path.
OUTPUT_FILE = '/path/to/flower_processed_data.npy'  # Save in numpy mode.
# Data related information.
VALIDATION_PERCENTAGE = 10  # The ratio of validation data.
TEST_PERCENTAGE = 10  # The ratio of test data.


def create_image_lists(sess, testing_percentage, validation_percentage):
    sub_dirs = [x[0] for x in os.walk(INPUT_DATA)]
    is_root_dir = True

    # Initialize data set.
    training_images = []
    training_labels = []
    testing_images = []
    testing_labels = []
    validation_images = []
    validation_labels = []
    current_label = 0

    # Read in all the directories.
    for sub_dir in sub_dirs:
        if is_root_dir:
            is_root_dir = False
            continue

        # Fetch all the pictures in directories.
        extensions = ['jpg', 'jpeg', 'JPG', 'JPEG']
        file_list = []
        dir_name = os.path.basename(sub_dir)
        for extension in extensions:
            file_glob = os.path.join(INPUT_DATA, dir_name, '*.' + extension)
            file_list.extend(glob.glob(file_glob))
            if not file_list:
                continue

            # Process pics.
            for file_name in file_list:
                # Read data and convert size of pics into 299*299 for modeling.
                image_raw_data = gfile.FastGFile(file_name, 'rb').read()
                image = tf.image.decode_jpeg(image_raw_data)
                if image.dtype != tf.float32:
                    image = tf.image.convert_image_dtype(image, dtype=tf.float32)
                image = tf.image.resize_images(image, [299, 299])
                image_value = sess.run(image)

                # Split data set randomly.
                chance = np.random.randint(100)
                if chance < validation_percentage:
                    validation_images.append(image_value)
                    validation_labels.append(current_label)
                elif chance < (testing_percentage + validation_percentage):
                    testing_images.append(image_value)
                    testing_labels.append(current_label)
                else:
                    training_images.append(image_value)
                    training_labels.append(current_label)
            current_label += 1

        # Shuffle data for better training result.
        state = np.random.get_state()
        np.random.shuffle(training_images)
        np.random.set_state(state)
        np.random.shuffle(training_labels)

        return np.asarray([training_images, training_labels,
                           validation_images, validation_labels,
                           testing_images, testing_labels])


def main():
    with tf.Session() as sess:
        processed_data = create_image_lists(sess, TEST_PERCENTAGE, VALIDATION_PERCENTAGE)
        # Save processed data.
        np.save(OUTPUT_FILE, processed_data)


if __name__ == '__main__':
    main()
