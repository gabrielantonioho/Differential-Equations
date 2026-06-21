import numpy as np
import matplotlib.pyplot as plt

# nx, ny - step size in the x and y direction
# minX, maxX - range of values of x
# minY, maxY - range of values of y 

class Grid():
    def __init__(self, nx, ny, minX, minY, maxX, maxY):
        self._x = np.arange(minX, maxX + 1, nx)
        self._y = np.arange(minY, maxY + 1, ny)
        
        # create a rectangular grid of points
        self._X, self._Y = np.meshgrid(self._x, self._y)
    
    def PlotDirectionField(self, f, ax=None):
        # f is a function of (x, y) representing dy/dx
        dX = np.ones(self._X.shape)       
        dY = f(self._X, self._Y)        

        # normalize vector arrows
        norm = np.sqrt(dX**2 + dY**2)
        dX_norm = dX / norm
        dY_norm = dY / norm

        if ax is None:
            fig, ax = plt.subplots()

        ax.quiver(self._X, self._Y, dX_norm, dY_norm, angles='xy', 
                    pivot = 'mid', scale = 40)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        return ax


def f(x,y):
    return y*((y-1)**2)

grid = Grid(nx = 0.3, ny= 0.3, minX = 0, minY = -5, maxX = 3, maxY = 5)
grid.PlotDirectionField(f)
plt.title('Direction Field')
plt.show()