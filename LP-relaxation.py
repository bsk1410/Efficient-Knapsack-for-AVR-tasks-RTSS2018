from math import sqrt
import numpy as np
from math import floor

a_max = 600000
a_min = -a_max
executionTimes = [965, 576, 424, 343, 277, 246]
# boundarySpeeds = [500,1500,2500,3500,4500,5500,6500]
boundarySpeeds = [1200,2200,3200,4200,5200,6200,7200]
rightBoundarySpeeds = [speed**2 for speed in boundarySpeeds[1:]]

#Helper function to calculate the minimum interarrival time given the initial and final speed - Based on the formulae in Mohaqeqi et al.
def calc_min_time(speed,speed_new):
    #From Mohaqeqi et al. Eqn (19) - Case 4 Rotational Speed
    peak_speed = (2*a_max*a_min+a_min*speed-a_max*speed_new)/(a_min-a_max)

    #If peak_speed does not exceed maximum speed...
    if peak_speed <= rightBoundarySpeeds[-1]:
        #From Mohaquqi et al. Eqn (20) - Accelerate maximally to peak_speed, decelerate maximally back to speed.
        min_time = (sqrt(peak_speed)-sqrt(speed))/a_max + (sqrt(speed_new)-sqrt(peak_speed))/a_min

    #...otherwise, peak_speed exceeds maximum speed.
    else:
        #From Mohaqeqi et al. Eqn (21) - Accelerate maximally to maximum allowable speed, decelerate maximally back to speed.
        min_time = ((sqrt(rightBoundarySpeeds[-1])-sqrt(speed))/a_max) + ((1 - ((rightBoundarySpeeds[-1]-speed)/(2*a_max))-((speed_new-rightBoundarySpeeds[-1])/(2*a_min)))/sqrt(rightBoundarySpeeds[-1])) + ((sqrt(speed_new)-sqrt(rightBoundarySpeeds[-1]))/a_min)
    
    #Return minimum time in seconds
    return min_time*60

minTimes = [calc_min_time(speed,speed) for speed in rightBoundarySpeeds]

f = open('LP-1.txt','w')

for t in np.arange(0.01,1.01,0.01):
    d = []
    for mt in range(len(rightBoundarySpeeds)):
        dm = floor(t/minTimes[mt]) * executionTimes[mt]
        d.append(dm)
    f.write('Max demand for time: {} = {}\n'.format(t,max(d)))
f.close()