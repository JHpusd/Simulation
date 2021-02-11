import sys
sys.path.append('src')
from euler_estimator import *
import matplotlib.pyplot as plt

rates = {
    's': (lambda t,x: -0.0003 * x['s'] * x['i']),
    'i': (lambda t,x: (0.0003 * x['s'] * x['i']) - (0.02 * x['i'])),
    'r': (lambda t,x: 0.02 * x['i'])}
model = EulerEstimator(rates)
init_vals = {'s': 1000, 'i': 1, 'r': 0}
init_point = (0, init_vals)

model.plot(init_point, 1, 500, "sir_model", "upper right")

'''
susceptible = 1000
infected = 1
recovered = 0
s_list = []
i_list = []
r_list = []

t = []
for i in range(501):
    t.append(i)

for _ in range(len(t)):
    s_list.append(susceptible)
    i_list.append(infected)
    r_list.append(recovered)

    s_copy = susceptible
    i_copy = infected
    r_copy = recovered

    susceptible += -0.0003*s_copy*i_copy
    infected += (0.0003*s_copy*i_copy) - (0.02*i_copy)
    recovered += 0.02*i_copy

plt.plot(t, s_list, label='susceptible')
plt.plot(t, i_list, label='infected')
plt.plot(t, r_list, label='recovered')
plt.legend(loc='center right')
plt.xlabel('time')
plt.ylabel('people')
plt.savefig('sir_model.png')
'''