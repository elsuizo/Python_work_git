#! /usr/bin/env python

# -*- coding: utf-8 -*-
"""
Script de prueba srinivasan metodo
"""
#imports
#**************************************************************************

import numpy as np
import matplotlib.pyplot as plt
#import cv2
import time

#**************************************************************************

start = time.time()
N = 500
sigma = 10
lamda = 20

#prealocamos imagenes
imagen1 = np.empty((N,N),dtype='float32')
imagen2 = np.empty((N,N),dtype='float32')
imagen3 = np.empty((N,N),dtype='float32')
imagen4 = np.empty((N,N),dtype='float32')
imagen5 = np.empty((N,N),dtype='float32')
imagen6 = np.empty((N,N),dtype='float32')
imagen7 = np.empty((N,N),dtype='float32')
imagen8 = np.empty((N,N),dtype='float32')
mask = np.empty((N,N),dtype='float32')
A = np.empty((2,2),dtype='float32')
B = np.empty(2,dtype='float32')

for i in xrange(3, N-2):
    for j in xrange(3, N-2):
        imagen1[i,j] = np.sin(2 * np.pi * i / lamda) * np.sin( 2 * np.pi * j / lamda)

        #hacemos los corrimientos
        imagen2[i+2, j] = imagen1[i, j]
        imagen3[i-2, j] = imagen1[i, j]
        imagen4[i, j+2] = imagen1[i, j]
        imagen5[i, j-2] = imagen1[i, j]
        imagen6[i-1, j-1] = imagen1[i, j]

        r_square = (i - N/2) ** 2 + (j - N/2) ** 2

        mask[i, j] = np.exp(-r_square / (2 * sigma ** 2))

#Normalizamos la mascara
#suma = mask.sum()
#print suma
#mask=mask/suma

#Ahora resolvemos para las dos direcciones
a_1_1 = np.sum((imagen3 - imagen2) ** 2 * mask)
a_1_2 = np.sum((imagen5 - imagen4) * (imagen3 - imagen2) * mask)
a_2_2 = np.sum((imagen5 - imagen4) ** 2 * mask)
b_1 = np.sum((imagen1 - imagen6) * (imagen3 - imagen2) * mask)
b_2 = np.sum((imagen1 - imagen6) * (imagen5 - imagen4) * mask)


A[0,0] = a_1_1
A[0,1] = a_1_2
A[1,0] = a_1_2
A[1,1] = a_2_2

B[0] = 2 * b_1

B[1] = 2 * b_2

#Resolvemos el sistema
x = np.linalg.solve(A,B)

#tiempo de procesamiento
print "Tiempo de procesamiento:",time.time() - start

print '$\\delta$ x:', x[0]
print '$\\alpha$ y:', x[1]


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
axarr[1, 3].set_title('$\delta x / \delta y$')
axarr[1, 3].arrow(N/2, N/2, x[0], x[1])
axarr[1,3].add_patch(arrow)
plt.show()











