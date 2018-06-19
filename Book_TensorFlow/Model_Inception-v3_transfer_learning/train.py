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





