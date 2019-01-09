"""
	<Author>	Airton Bordin Junior
	<Email>	airtonbjunior@gmail.com

	Udacity Deep Learn Course - https://classroom.udacity.com/courses/ud730/

	Assignment 1 - notMNIST database
"""

from aux import * # aux methods, as can be seen at https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/udacity/1_notmnist.ipynb

if __name__ == '__main__':
	train_filename = maybe_download('notMNIST_large.tar.gz', 247336696)
	test_filename  = maybe_download('notMNIST_small.tar.gz', 8458043)
	print("hey")