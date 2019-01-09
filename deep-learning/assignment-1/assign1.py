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

from aux import *

if __name__ == '__main__':
	print("hey")