# This script should run without errors whenever we update the
# kaggle/python container. It checks that all our most popular packages can
# be loaded and used without errors.

import numpy as np
print("Numpy imported ok")
print("Your lucky number is: " + str(np.random.randint(100)))

# Numpy must be linked to the MKL. (Occasionally, a third-party package will muck up the installation
# and numpy will be reinstalled with an OpenBLAS backing.)
from numpy.distutils.system_info import get_info
# This will throw an exception if the MKL is not linked correctly.
get_info("blas_mkl")

import pandas as pd
print("Pandas imported ok")

from sklearn import datasets
print("sklearn imported ok")
iris = datasets.load_iris()
X, y = iris.data, iris.target

from sklearn.ensemble import RandomForestClassifier
rf1 = RandomForestClassifier()
rf1.fit(X,y)
print("sklearn RandomForestClassifier: ok")

from sklearn.linear_model import LinearRegression
boston = datasets.load_boston()
X, y = boston.data, boston.target
lr1 = LinearRegression()
lr1.fit(X,y)
print("sklearn LinearRegression: ok")

from xgboost import XGBClassifier
xgb1 = XGBClassifier(n_estimators=3)
xgb1.fit(X[0:70],y[0:70])
print("xgboost XGBClassifier: ok")

import matplotlib.pyplot as plt
plt.plot(np.linspace(0,1,50), np.random.rand(50))
plt.savefig("plot1.png")
print("matplotlib.pyplot ok")

import plotly.plotly as py
import plotly.graph_objs as go
print("plotly ok")

from ggplot import *
print("ggplot ok")

from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.optimizers import SGD
print("keras ok")

import nltk
from nltk.stem import WordNetLemmatizer
print("nltk ok")

import tensorflow as tf
hello = tf.constant('TensorFlow ok')
sess = tf.Session()
print(sess.run(hello))

import cv2
img = cv2.imread('plot1.png',0)
print("OpenCV ok")

from skimage.io import imread
print("skimage ok")

