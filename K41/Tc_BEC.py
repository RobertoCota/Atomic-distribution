#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 10:46:19 2020

@author: cesarcc
"""

import glob
from scipy import misc
from numpy import sin
from numpy import arctan
from scipy import special
from matplotlib import *
import math
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import scipy.optimize as opt
from matplotlib import *
from matplotlib.colors import LinearSegmentedColormap


img = mpimg.imread('../../doc/_static/stinkbug.png')
print(img)

#Greiner map
greiner_data = {
'red': ((0., 1, 1,), (.2, 0, 0), (.48, 0, 0), (.728, 1, 1),
(0.912, 1, 1), (1, .5, .5)),
'green': ((0., 1, 1), (.2, 0, 0), (.3, 0, 0), (.5, 1, 1),
(.712, 1, 1), (.928, 0, 0), (1, 0, 0)),
'blue': ((0., 1, 1), (.2, .5, .5), (.288, 1, 1), (.472, 1, 1),
(.72, 0, 0), (1, 0, 0))}
greiner = LinearSegmentedColormap('greiner',greiner_data)