#! /usr/bin/env python
# -*- coding utf-8 -*-

#*************************************************************************
# imports
#*************************************************************************
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
#*************************************************************************
def f(X, t):
    """Doc"""
    x1, x2 = X
    return [x2, -np.sin(x1) + np.cos(x2)]

x1 = np.linspace(-2.0, 8.0, 20)
x2 = np.linspace(-2.0, 2.0, 20)

X1, X2 = np.meshgrid(x1, x2)

t = 0

u, v = np.zeros(X1.shape), np.zeros(X2.shape)
NI, NJ = X1.shape

for i in range(NI):
    for j in range(NJ):
        x = X1[i, j]
        y = X2[i, j]
        yprime = f([x,y], t)
        u[i, j] = yprime[0]
        v[i, j] = yprime[1]

    
fig, ax = plt.subplots()

plt.quiver(X1, X2, u, v, color='r')

plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.xlim([-2, 8])
plt.ylim([-2, 2])


def on_button_press(event):
    
    t_sim = np.linspace(0,50,200)
    x, y = event.xdata, event.ydata

    x0 = [x,y]
    ys = odeint(f, x0, t_sim)
    plt.plot(ys[:,0], ys[:,1], 'k-') # path
    plt.plot([ys[0,0]], [ys[0,1]], 'o') # start
    plt.plot([ys[-1,0]], [ys[-1,1]], 's') # end

    fig.canvas.draw()
    
    #plt.savefig('phase_portrait.png')
    
fig.canvas.mpl_connect('button_press_event', on_button_press)

plt.show()

