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
import matplotlib.image as mpimg
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
from PIL import Image 

#img = mpimg.imread('CriticalTc41_11_xDensityCrossed_loop_1_StopEvaporation_0.1.png')

im = Image.open("41K_Average_4.5.png")
region = im.crop((220-180, 50,220+180+120, 450))
region.save("Cropped_phaseSeparation41K.png")

img = mpimg.imread('Cropped_phaseSeparation41K.png')
  

#Greiner map
greiner_data = {
'red': ((0., 1, 1,), (.2, 0, 0), (.48, 0, 0), (.728, 1, 1),
(0.912, 1, 1), (1, .5, .5)),
'green': ((0., 1, 1), (.2, 0, 0), (.3, 0, 0), (.5, 1, 1),
(.712, 1, 1), (.928, 0, 0), (1, 0, 0)),
'blue': ((0., 1, 1), (.2, .5, .5), (.288, 1, 1), (.472, 1, 1),
(.72, 0, 0), (1, 0, 0))}

greiner = LinearSegmentedColormap('greiner',greiner_data)
cmap=greiner
levels = MaxNLocator(nbins=15).tick_values(0.055,0.5)
norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)

imgplot = plt.imshow(img,cmap=cmap,norm=norm)
plt.savefig('Tc_41_BEC.pdf')
plt.show()


fig=plt.plot(img[:,250])
plt.ylim(0, 0.7)
plt.grid()
plt.savefig('Tc_41_BECcut.pdf')

plt.show()


