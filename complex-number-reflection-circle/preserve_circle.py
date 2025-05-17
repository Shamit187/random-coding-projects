import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def reflect(z):
    x = z.real
    y = z.imag
    return (x + 1j * y) / (x * x + y * y)

# Initial circle center and radius
q_init = 2 - 3j
r_init = 1
theta = np.linspace(0, 2*np.pi, 200)

# Set up figure and axis
fig, ax = plt.subplots(figsize=(10, 8))
plt.subplots_adjust(left=0.1, bottom=0.3)

# Unit circle (static)
unit_theta = np.linspace(0, 2*np.pi, 200)
u = np.cos(unit_theta)
v = np.sin(unit_theta)
ax.plot(u, v, 'g--', label='Unit Circle')

# Initial circle
u_c = r_init * np.cos(theta) + q_init.real
v_c = r_init * np.sin(theta) + q_init.imag
z = u_c + 1j * v_c
z_ref = reflect(z)

# Plot elements (placeholders)
circle_plot, = ax.plot(z.real, z.imag, 'b-', label='Original Circle')
reflected_plot, = ax.plot(z_ref.real, z_ref.imag, 'r-', label='Reflected Circle')

# Axes formatting
ax.axhline(0, color='black', lw=0.5)
ax.axvline(0, color='black', lw=0.5)
ax.grid(True)
ax.set_aspect('equal', adjustable='box')
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.set_title('Reflecting a Circle in Complex Plane')
ax.legend(loc='upper right')

# Slider axes
axcolor = 'lightgoldenrodyellow'
slider_width = 0.65
slider_height = 0.03

ax_qr = plt.axes([0.2, 0.22, slider_width, slider_height], facecolor=axcolor)
ax_qi = plt.axes([0.2, 0.17, slider_width, slider_height], facecolor=axcolor)
ax_r = plt.axes([0.2, 0.12, slider_width, slider_height], facecolor=axcolor)

# Sliders
s_qr = Slider(ax_qr, 'Re(q)', -5.0, 5.0, valinit=q_init.real)
s_qi = Slider(ax_qi, 'Im(q)', -5.0, 5.0, valinit=q_init.imag)
s_r = Slider(ax_r, 'r', 0.1, 5.0, valinit=r_init)

# Update function
def update(val):
    q = s_qr.val + 1j * s_qi.val
    r = s_r.val

    u = r * np.cos(theta) + q.real
    v = r * np.sin(theta) + q.imag
    z = u + 1j * v
    z_ref = reflect(z)

    circle_plot.set_data(z.real, z.imag)
    reflected_plot.set_data(z_ref.real, z_ref.imag)

    fig.canvas.draw_idle()

# Bind sliders
s_qr.on_changed(update)
s_qi.on_changed(update)
s_r.on_changed(update)

# Initial draw
update(None)
plt.show()
