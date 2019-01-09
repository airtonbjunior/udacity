"""
	<Author>	Airton Bordin Junior
	<Email>	airtonbjunior@gmail.com

	Udacity Deep Learn Course - https://classroom.udacity.com/courses/ud730/

	Assignment 1 - notMNIST database
"""

import imageio
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
import tarfile
from IPython.display import display, Image
from sklearn.linear_model import LogisticRegression
from six.moves.urllib.request import urlretrieve
from six.moves import cPickle as pickle

from aux import * # aux methods, as can be seen at https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/udacity/1_notmnist.ipynb

if __name__ == '__main__':
	train_filename = maybe_download('notMNIST_large.tar.gz', 247336696)
	test_filename  = maybe_download('notMNIST_small.tar.gz', 8458043)
	print("hey")