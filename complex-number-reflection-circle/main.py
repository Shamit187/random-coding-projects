import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def reflect(z):
    x = z.real
    y = z.imag
    return (x + 1j * y) / (x * x + y * y)

# Initial values for z1 and z2
z1_init = 1 + 1j
z2_init = 1 - 2j

fig, ax = plt.subplots(figsize=(10, 8))
plt.subplots_adjust(left=0.1, bottom=0.3)  

# Dummy values to start
alpha = np.linspace(-10, 10, 2000)
line, = plt.plot([], [], 'r-')
line_reflected, = plt.plot([], [], 'b-')
z1_point, = plt.plot([], [], 'bo')
z2_point, = plt.plot([], [], 'bo')
z1_reflected, = plt.plot([], [], 'ro')
z2_reflected, = plt.plot([], [], 'ro')

# Unit circle
theta = np.linspace(0, 2*np.pi, 200)
u = np.cos(theta)
v = np.sin(theta)
plt.plot(u, v, 'g--')

plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.grid()
plt.gca().set_aspect('equal', adjustable='box')
plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.title('Reflecting Line between z1 and z2')

# Create sliders
axcolor = 'lightgoldenrodyellow'
ax_z1r = plt.axes([0.25, 0.25, 0.65, 0.03], facecolor=axcolor)
ax_z1i = plt.axes([0.25, 0.20, 0.65, 0.03], facecolor=axcolor)
ax_z2r = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
ax_z2i = plt.axes([0.25, 0.10, 0.65, 0.03], facecolor=axcolor)

s_z1r = Slider(ax_z1r, 'Re(z1)', -5.0, 5.0, valinit=z1_init.real)
s_z1i = Slider(ax_z1i, 'Im(z1)', -5.0, 5.0, valinit=z1_init.imag)
s_z2r = Slider(ax_z2r, 'Re(z2)', -5.0, 5.0, valinit=z2_init.real)
s_z2i = Slider(ax_z2i, 'Im(z2)', -5.0, 5.0, valinit=z2_init.imag)

def update(val):
    z1 = s_z1r.val + 1j * s_z1i.val
    z2 = s_z2r.val + 1j * s_z2i.val
    z = (1 - alpha) * z1 + alpha * z2
    z_ref = reflect(z)

    line.set_data(z.real, z.imag)
    line_reflected.set_data(z_ref.real, z_ref.imag)

    z1_point.set_data([z1.real], [z1.imag])
    z2_point.set_data([z2.real], [z2.imag])

    z1r = reflect(z1)
    z2r = reflect(z2)
    z1_reflected.set_data([z1r.real], [z1r.imag])
    z2_reflected.set_data([z2r.real], [z2r.imag])

    fig.canvas.draw_idle()

# Attach sliders to update function
s_z1r.on_changed(update)
s_z1i.on_changed(update)
s_z2r.on_changed(update)
s_z2i.on_changed(update)

# Initial plot
update(None)
plt.show()
