# Import required libraries
import numpy as np
from scipy.optimize import linprog

# Set the inequality constraints matrix
# Note: the inequality constraints must be in the form of <=
A = np.array([[-2, 6, -3, 3], [-3, -4, 1, -1], [-4, 1, -5, 5],
    [-1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]])

# Set the inequality constraints vector
b = np.array([-50, -40, -60, 0, 0, 0, 0])

# Set the coefficients of the linear objective function vector
c = np.array([1, 1, 1, -1])

# Solve linear programming problem
res = linprog(c, A_ub=A, b_ub=b)

# Print results
print('Optimal value:', round(res.fun, ndigits=2),
      '\nx values:', res.x,
      '\nNumber of iterations performed:', res.nit,
      '\nStatus:', res.message)