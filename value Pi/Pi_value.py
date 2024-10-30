## Pi value estimation
import matplotlib.pyplot as plt
import numpy as np
import random

## define constants and bounds
x_min = -5
y_min = -5
x_max = 5
y_max = 5
r = 5
N = 1000


estimated_area = 0
x = 0
y = 0
incount = 0 
j = 0 
i = 0

# store
inside = []
outside = []

t = np.linspace(-5, 5, 100)
X = r*np.cos(t)
Y = r*np.sin(t)


for j in range(0, 5):
    incount = 0 
    
    for i in range(1, N):
        x = random.uniform(x_min, x_max)
        y = random.uniform(y_min, y_max)

        if np.all(x <= X) and np.all(y <= Y):
            incount += 1
            inside.append((x, y))
        else:
            outside.append((x, y))



        



