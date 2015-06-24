#! /usr/bin/env python
# -*- coding utf-8 -*-

#*************************************************************************
# imports
#*************************************************************************
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.integrate import odeint
#*************************************************************************
def f(X, t):
    """

    Inputs:
    ------

    """
    x1, x2 = X
    return [-x1**3, x1]

x1 = np.linspace(-2.0, 2.0, 20)
x2 = np.linspace(-2.0, 2.0, 20)

X1, X2 = np.meshgrid(x1, x2)

t = 0

u, v = np.zeros(X1.shape), np.zeros(X2.shape)
NI, NJ = X1.shape

for i in xrange(NI):
    for j in xrange(NJ):
        x = X1[i, j]
        y = X2[i, j]
        yprime = f([x,y], t)
        u[i, j] = yprime[0]
        v[i, j] = yprime[1]


fig, ax = plt.subplots()
#ellipse = mpl.patches.Ellipse(xy=(0, 0), width=1.7, height=1.5)
#fig.gca().add_artist(ellipse)
plt.quiver(X1, X2, u, v, color='r',pivot='mip',units='x')
plt.streamplot(X1,X2,u,v)

#ax.text(0, 0, r'$\vec{\nabla}\mathbf{f}<0$', fontsize=20)
plt.xlabel('$x_1$',fontsize=20)
plt.ylabel('$x_2$',fontsize=20)
plt.title(r'Retrato de fase: $\dot{\mathbf{x}}=\mathbf{f}(\mathbf{x})$',fontsize=15)
plt.xlim([-2, 2])
plt.ylim([-2, 2])

#-------------------------------------------------------------------------
# button press action capture
#-------------------------------------------------------------------------
def on_button_press(event):

    t_sim = np.linspace(0,10,200)
    x, y = event.xdata, event.ydata # event data capture

    x0 = [x,y]
    ys = odeint(f, x0, t_sim)
    plt.plot(ys[:,0], ys[:,1], 'k-', markersize=10) # path
    plt.plot([ys[0,0]], [ys[0,1]], 'o', markersize=10) # start
    plt.plot([ys[-1,0]], [ys[-1,1]], 's', markersize=10) # end

    fig.canvas.draw()

    #plt.savefig('phase_portrait.png')

fig.canvas.mpl_connect('button_press_event', on_button_press)

plt.show()

