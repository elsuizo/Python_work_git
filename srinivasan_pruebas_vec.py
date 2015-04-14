#! /usr/bin/env python

# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 18:09:39 2013

@author: elsuizo

Pruebas srinivasan vectorizado
"""

import numpy as np
import matplotlib.pyplot as plt
import time
import cv2
#from numba import autojit


start = time.time()#comenzamos a medir el tiempo

N = 500
lamda = 20
sigma = 10
A = np.empty((2,2),dtype='float32')
B = np.empty(2,dtype='float32')
imagen1 = np.empty((N,N),dtype='float32')
imagen2 = np.empty((N,N),dtype='float32')
imagen3 = np.empty((N,N),dtype='float32')
imagen4 = np.empty((N,N),dtype='float32')
imagen5 = np.empty((N,N),dtype='float32')
imagen6 = np.empty((N,N),dtype='float32')
mask = np.empty((N,N),dtype='float32')
f1 = np.empty((N,N),dtype='float32')
#gray=np.empty((N,N),dtype='float32')

X, Y = np.ogrid[0:N, 0:N ]

imagen1 = np.sin(2 * np.pi * X / lamda) * np.sin(2 * np.pi * Y / lamda)
imagen2 = np.sin(2 * np.pi * (X+2) / lamda) * np.sin(2 * np.pi * (Y) / lamda)
imagen3 = np.sin(2 * np.pi * (X-2) / lamda) * np.sin(2 * np.pi * Y / lamda)
imagen4 = np.sin(2 * np.pi * X / lamda) * np.sin(2 * np.pi * (Y+2) / lamda)
imagen5 = np.sin(2 * np.pi * X / lamda) * np.sin(2 * np.pi * (Y-2) / lamda)
imagen6 = np.sin(2 * np.pi * (X-1) / lamda) * np.sin(2 * np.pi * (Y-1) / lamda)

r_square = (X - N / 2) ** 2 + (Y - N / 2) ** 2
mask = np.exp(-r_square / (2 * sigma ** 2))



#suma = mask.sum()
#print suma
#mask=mask/suma

#Ahora resolvemos para las dos direcciones
a_1_1 = np.sum((imagen3 - imagen2) ** 2 * mask)
a_1_2 = np.sum((imagen5 - imagen4) * (imagen3 - imagen2) * mask)
a_2_2 = np.sum((imagen5 - imagen4) ** 2 * mask)
b_1 = np.sum((imagen1 - imagen6) * (imagen3 - imagen2) * mask)
b_2 = np.sum((imagen1 - imagen6) * (imagen5 - imagen4) * mask)


A[0, 0] = a_1_1
A[0,1] = a_1_2
A[1,0] = a_1_2
A[1,1] = a_2_2
#
B[0] = 2 * b_1
#
B[1] = 2 * b_2
#
##Resolvemos el sistema
x = np.linalg.solve(A, B)



#tiempo de procesamiento

print "Tiempo de procesamiento:",time.time() - start

print x

#gray=cv2.cvtColor(imagen1, cv2.COLOR_BGR2GRAY)

#Graficos
fig, axarr = plt.subplots(2, 4)
axarr[0, 0].imshow(imagen1)
axarr[0, 0].set_title('$f(x,y)$')
axarr[0, 1].imshow(imagen2)
axarr[0, 1].set_title('$f(x+2,y)$')
axarr[0, 2].imshow(imagen3)
axarr[0, 2].set_title('$f(x-2,y)$')
axarr[0, 3].imshow(imagen4)
axarr[0, 3].set_title('$f(x,y+2)$')
axarr[1, 0].imshow(imagen5)
axarr[1, 0].set_title('$f(x,y-2)$')
axarr[1, 1].imshow(imagen6)
axarr[1, 1].set_title('$f(x-1,y-1)$')
axarr[1, 2].imshow(mask)
axarr[1, 2].set_title('$mask(x,y)$')
arrow = plt.Arrow(N/2,N/2,x[0],x[1],width=19,lw=3)
#axarr[0,0].annotate('arrowstyle', xy=(x[0], x[1]),  xycoords='data',
#                xytext=(-50, 30), textcoords='offset points',
#                arrowprops=dict(arrowstyle="->")
#                )
#axarr[1,2].add_patch(arrow)
axarr[1, 3].set_title('$LaTeX$')
axarr[1, 3].imshow(f1)
axarr[1,3].add_patch(arrow)
plt.show()
