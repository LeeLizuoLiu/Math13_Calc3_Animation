import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# Define the function to integrate
def f(x, y):
    return x**2 + y**2

# Domain boundaries
x_min, x_max = 0, np.pi
y_min, y_max = 0, np.pi

# Create figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Function to update the plot for each frame
def update(n):
    ax.clear()
    
    # Number of subdivisions (increases with frame number)
    n_subdivisions = n + 2
    
    # Create grid
    x_edges = np.linspace(x_min, x_max, n_subdivisions)
    y_edges = np.linspace(y_min, y_max, n_subdivisions)
    
    # Calculate Riemann sum
    riemann_sum = 0
    
    # Plot the rectangles
    for i in range(len(x_edges)-1):
        for j in range(len(y_edges)-1):
            # Midpoint or corner evaluation
            x_mid = (x_edges[i] + x_edges[i+1]) / 2
            y_mid = (y_edges[j] + y_edges[j+1]) / 2
            
            # Height of the rectangle
            z_height = f(x_mid, y_mid)
            
            # Area of the base
            dx = x_edges[i+1] - x_edges[i]
            dy = y_edges[j+1] - y_edges[j]
            
            # Add to Riemann sum
            riemann_sum += z_height * dx * dy
            
            # Plot the rectangle
            x_rect = [x_edges[i], x_edges[i], x_edges[i+1], x_edges[i+1]]
            y_rect = [y_edges[j], y_edges[j+1], y_edges[j+1], y_edges[j]]
            z_rect = [0, 0, 0, 0]
            ax.plot_trisurf(x_rect, y_rect, z_rect, color='blue', alpha=0.2)
            
            # Plot the top face
            z_top = [z_height, z_height, z_height, z_height]
            ax.plot_trisurf(x_rect, y_rect, z_top, color='red', alpha=0.5)
            
            # Connect the vertices
            for k in range(4):
                ax.plot([x_rect[k], x_rect[k]], [y_rect[k], y_rect[k]], [0, z_top[k]], 'k-', alpha=0.3)
    
    # Plot the actual function surface
    x = np.linspace(x_min, x_max, 30)
    y = np.linspace(y_min, y_max, 30)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
    ax.plot_surface(X, Y, Z, alpha=0.3, color='green')
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(f'Riemann Sum with {n_subdivisions-1}×{n_subdivisions-1} rectangles\nSum = {riemann_sum:.4f}')

# Create animation
ani = FuncAnimation(fig, update, frames=range(1, 10), interval=1000)

# To save the animation
# ani.save('riemann_double_integral.gif', writer='pillow', fps=1)

plt.show()