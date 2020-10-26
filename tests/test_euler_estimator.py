import sys
sys.path.append('src')
from euler_estimator import *

def deriv(t):
    return t + 1

euler = EulerEstimator(deriv)
print("Testing 'EulerEstimator' class with derivative x'(t) = t + 1 ...")
assert euler.calc_derivative_at_point((1, 4)) == 2
assert euler.step_forward((1, 4), 0.5) == (1.5, 5)
print("First 4 steps (starting at (1,4) with step size 0.5):")
euler.calc_estimated_points((1,4), 0.5, 4)
print("PASSED")
