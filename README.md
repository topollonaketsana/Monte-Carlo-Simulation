# Monte Carlo simulation method to approximate the area under a curve for continuous functions

## Monte Carlo Simulation

This project demonstrates the Monte Carlo simulation method to approximate the area under the curve defined by the function \( f(x) = x^3 \). The simulation involves randomly throwing "stones" within a defined boundary and counting how many fall under the curve to estimate the area.


## Project Description

The Monte Carlo method is a statistical technique that uses random sampling to obtain numerical results. In this project, we use the Monte Carlo method to approximate the area under the curve of the function \( f(x) = x^3 \) between \( x = 0 \) and \( x = 3 \).

## Whats needed

Before running the code, ensure you have the following installed:

- `Python 3.x` (You can download python [here](https://www.python.org/downloads/) if you dont have it yet)
- `matplotlib` library for plotting
- `numpy` library for numerical operations

You can install the required libraries using pip:

```bash
pip install matplotlib numpy
```

##

## Usage
1. Clone the repository and Go to the Project directory:

```bash
git clone https://github.com/topollonaketsana/Monte-Carlo-Simulation.git
cd Monte-Carlo-Simulation
```


2. Run the Python script:
```bash
python monte_carlo_simulation.py

```


##

3. Description of the Python Script:
   The script monte_carlo_simulation.py performs the following steps:

   - Defines the bounds of the rectangular boundary [x_min, x_max]*[y_min, y_max].
   - Randomly generates points within the boundary [x, y].
   - Checks whether each point lies below the curve y = x**3
   - Calculates the estimated area under the curve based on the ratio of points below(Incount) the curve to the total numebr of points(N)

## Code
The code is already included in the 'python' file, you just copy directly and paste it on your codespace.


