from time import time
import cvxpy as cp
import numpy as np

# Problem data.
m = 30
n = 20
np.random.seed(1)
A = np.random.randn(m, n)
b = np.random.randn(m)

def tst():
  # Construct the problem.
  t1= time()
  x = cp.Variable(n)
  objective = cp.Minimize(cp.sum_squares(A*x - b))
  constraints = [1 <= x, x <= 0]
  prob = cp.Problem(objective, constraints)

  # The optimal objective value is returned by `prob.solve()`.
  result = prob.solve()
  print(x.value)
# The optimal value for x is stored in `x.value`.
#  print(x.value)
# The optimal Lagrange multiplier for a constraint is stored in
# `constraint.dual_value`.
#  print(constraints[0].dual_value)
  t2 = time()
  print(t2-t1)

for _ in range(25000):
    tst()

