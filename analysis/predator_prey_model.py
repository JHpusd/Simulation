import sys
sys.path.append('src')
from euler_estimator import *
import matplotlib.pyplot as plt

rates = {
    'deer': (lambda t,x: (0.6*x['deer']) - (0.05*x['deer']*x['wolves'])),
    'wolves': (lambda t,x: (0.02*x['deer']*x['wolves']) - (0.9*x['wolves']))}
model = EulerEstimator(rates)
initial_vals = {'deer': 100, 'wolves': 10}
init_point = (0, initial_vals)

model.plot(init_point, 0.001, 100, "predator_prey_model")

