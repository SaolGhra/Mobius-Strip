import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


def mobius_function(u, v, t):
    x = (1 + 0.5 * v * np.cos(u / 2 + t)) * np.cos(u)
    y = (1 + 0.5 * v * np.cos(u / 2 + t)) * np.sin(u)
    z = 0.5 * v * np.sin(u / 2 + t)
    return x, y, z


def animate(t):
    ax.clear()
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(-1, 1, 100)
    u, v = np.meshgrid(u, v)
    x, y, z = mobius_function(u, v, t)
    ax.plot_surface(x, y, z, cmap='viridis')

    # Parameters for the point moving along the strip
    point_u = np.cos(t)
    point_v = np.sin(t)
    point_x, point_y, point_z = mobius_function(point_u, point_v, t)

    # Plot the point moving along the strip
    ax.scatter(point_x, point_y, point_z, color='red')


ani = FuncAnimation(fig, animate, frames=np.linspace(0, 2 * np.pi, 200), interval=1)
plt.show()
