import sys
sys.path.append('src')
from euler_estimator import *
import math

# alphas, betas, stimulus
def alpha_n(t,x):
    V = x[0]
    return (0.01*(10-V))/(math.exp(0.1*(10-V) - 1))
def alpha_m(t,x):
    V = x[0]
    return (0.1*(25-V))/(math.exp(0.1*(25-V)) - 1)
def alpha_h(t,x):
    V = x[0]
    return 0.07*math.exp(-V/20)

def beta_n(t,x):
    V = x[0]
    return 0.125*math.exp(-V/80)
def beta_m(t,x):
    V = x[0]
    return 4*math.exp(-V/18)
def beta_h(t,x):
    return 1/(math.exp(0.1*(30-V) + 1))

def stim(t):
    if 10<=t<=11 or 20<=t<=21 or 30<=t<=40 or 50<=t<=51 or 53<=t<=54 or 56<=t<=57 or 59<=t<=60 or 62<=t<=63 or 65<=t<=66:
        return 150
    return 0

# constants
V_0 = 0
n_0 = alpha_n(0)/(alpha_n(0) + beta_n(0))
m_0 = alpha_m(0)/(alpha_m(0) + beta_m(0))
h_0 = alpha_h(0)/(alpha_h(0) + beta_h(0))

C = 1.0
V_Na = 115
V_k = -12
V_L 10.6

# main variables
def dV_dt(t,x):


