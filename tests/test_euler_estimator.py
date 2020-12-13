import sys
sys.path.append('src')
from euler_estimator import *
'''
def deriv(t):
    return t + 1

euler = EulerEstimator(deriv)

print("Testing 'EulerEstimator' class with derivative x'(t) = t + 1 ...")
assert euler.calc_derivative_at_point((1, 4)) == 2
assert euler.step_forward((1, 4), 0.5) == (1.5, 5)
print("First 4 steps (starting at (1,4) with step size 0.5):")
euler.calc_estimated_points((1,4), 0.5, 4)
print("PASSED")

euler.plot((-5, 10), 0.1, 100)
'''
print("Testing EulerEstimator for systems of equations...")
derivatives = {
        'A': (lambda t,x: x['A'] + 1),
        'B': (lambda t,x: x['A'] + x['B']),
        'C': (lambda t,x: 2*x['B']) 
    }
euler = EulerEstimator(derivatives)
initial_values = {'A': 0, 'B': 0, 'C': 0}
initial_point = (0, initial_values)

assert euler.calc_derivative_at_point(initial_point) == {'A': 1, 'B': 0, 'C': 0}

point_2 = euler.step_forward(initial_point, 0.1)
assert point_2 == (0.1, {'A': 0.1, 'B': 0, 'C': 0})
assert euler.calc_derivative_at_point(point_2) == {'A': 1.1, 'B': 0.1, 'C': 0}

point_3 = euler.step_forward(point_2, -0.5)
for key in point_3[1]:
    point_3[1][key] = round(point_3[1][key], 6)
assert point_3 == (-0.4, {'A': -0.45, 'B': -0.05, 'C': 0})

est_list = euler.calc_estimated_points(point_3, 2, 3)
for point in est_list:
    for key in point[1]:
        point[1][key] = round(point[1][key], 6)
assert est_list == [
   (-0.4, {'A': -0.45, 'B': -0.05, 'C': 0}),
   (1.6, {'A': 0.65, 'B': -1.05, 'C': -0.2}),
   (3.6, {'A': 3.95, 'B': -1.85, 'C': -4.4}),
   (5.6, {'A': 13.85, 'B': 2.35, 'C': -11.8})
]
print("PASSED")
