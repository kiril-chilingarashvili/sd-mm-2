import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

x = np.arange(0, 20 * np.pi, 0.1)
y = np.cos(3 * x) + np.cos(5 * x)

fig, ax = plt.subplots()  
plt.subplots_adjust(bottom=0.2,left=0.3) 
l, = plt.plot(x, y)

om1= plt.axes([0.25, 0.1, 0.65, 0.03]) 
om2 = plt.axes([0.25, 0.15, 0.65, 0.03]) 

som1 = Slider(om1, r'$\omega_1$', 1, 30.0, valinit=3) 
som2 = Slider(om2, r'$\omega_2$', 1, 30.0, valinit=5)

def update(val):
    s1 = som1.val
    s2 = som2.val
    x = np.arange(0, 20 * np.pi, 0.1)
    y = np.cos(s1 * x) + np.cos(s2 * x)
    l.set_ydata(y)
    l.set_xdata(x)

som1.on_changed(update)
som2.on_changed(update)

plt.show()