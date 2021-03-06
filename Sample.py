# Ex1: M=1, SIR
import numpy as np
import pyross

M     = 1                  # the SIR model has no age structure
Ni    = 1000*np.ones(M)    # so there is only one age group
N     = np.sum(Ni)         # and the total population is the size of this age group

beta  = 0.01566               # infection rate
gIa   = 0.1                # recovery rate of asymptomatic infectives
gIs   = 0.1                # recovery rate of symptomatic infectives
alpha = 0                  # fraction of asymptomatic infectives
fsa   = 1                  # the self-isolation parameter

Ia0   = np.array([0])      # the SIR model has only one kind of infective
Is0   = np.array([1])      # we take these to be symptomatic
R0    = np.array([0])      # and assume there are no recovered individuals initially
S0    = N-(Ia0+Is0+R0)     # initial susceptibles are obtained from S + Ia + Is + R = N

# there is no contact structure
def contactMatrix(t):   
    return np.identity(M)

# instantiate model
parameters = {'alpha':alpha, 'beta':beta, 'gIa':gIa, 'gIs':gIs, 'fsa':fsa}
model      = pyross.deterministic.SIR(parameters, M, Ni)

# simulate model
Tf, Nt = 160,  160           # duration of simulation and data points
data = model.simulate(S0, Ia0, Is0, contactMatrix, Tf, Nt)

# time series of S, Ia, Is, R
S  = model.S(data)
Ia = model.Ia(data)
Is = model.Is(data)
R  = model.R(data)
