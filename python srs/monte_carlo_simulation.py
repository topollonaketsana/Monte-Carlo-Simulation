## This is Python code to visualize and calculate the area under a curve which is f(x) = x ** 3.
import matplotlib.pyplot as plt
import random

# Define the bounds and constants
x_min = 0
x_max = 3
y_min = 0
y_max = 27
N = 10000       # increase or decrease the number of stones thrown

actual_value = 20.25  # this is just for an error, we dont have to always know the exact value

# Define the variables
estimated_value = 0
incount = 0
M = 5
M_estimated = 0
j = 0
i = 0
x = 0
y = 0

# Lists to store points for visualization
inside_points = []
outside_points = []

# Throw stones and count how many fall under the curve
for j in range(0, M + 1):
    incount = 0

    for i in range(0, N + 1):
        x = random.uniform(x_min, x_max)
        y = random.uniform(y_min, y_max)

        if y <= x ** 3:
            incount += 1
            inside_points.append((x, y))
        else:
            outside_points.append((x, y))

# Calculate the area estimation
area_estimated = (incount / N) * (x_max - x_min) * (y_max - y_min)
absolute_error = abs(area_estimated - actual_value)
print("Estimated area:", area_estimated, "\nAbsolute error:", absolute_error)

# Visualize points
inside_x, inside_y = zip(*inside_points)
outside_x, outside_y = zip(*outside_points)

plt.scatter(inside_x, inside_y, color='red', label='Inside')
plt.scatter(outside_x, outside_y, color='blue', label='Outside')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Monte Carlo Simulation')
plt.show()




