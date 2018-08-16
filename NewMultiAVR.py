from time import perf_counter
#start = perf_counter()
from math import sqrt
from collections import defaultdict
import numpy as np
from pprint import pprint
import random
from bisect import bisect_left

def NewMultiAVRgen():

    #Units
    #a_max, a_min : revolutions / min^2
    #speed, peak_speed, speed_new : revolutions / minute (RPM)

    #Acceleration equal in magnitude to deceleration per Bijinemula et al. Sec. III.A Para. 4 
    a_max = 600000
    a_min = -a_max

    #Multiple AVR Tasks generation
    #inputs that need to given - Umax, M_min, M_max, Umax
    for M in range(6,16):
        a_max = 600000
        a_min = -600000
        fileMname = 'NewMultiAVROutputs/NewAlg_Multi_'+str(M)+'.txt'
        
        start1 = perf_counter()
        random.seed(100)
        #M = random.randint(M_min,M_max)
        Ustar = 0.25
        Udict = dict()
        for i in range(M):
            Udict[i] = random.uniform(0.85*Ustar, Ustar)
        Udict[M-1] = Ustar

        while True:
            while True:
                rightBoundarySpeeds = sorted(random.sample(range(500,6500),M-1))
                rightBoundarySpeeds = [500]+rightBoundarySpeeds+[6500]
                for i in range(M):
                    k = i
                    if rightBoundarySpeeds[i+1] - rightBoundarySpeeds[i] < 3000/M:
                        continue
                        
                if k==M-1:
                    break
            br = 0
            executionTimes = []
            for i in range(M):
                executionTimes.append(1000**2*Udict[i]*60/rightBoundarySpeeds[i])   #in micro seconds
            for c1,c2 in zip(executionTimes[:-1],executionTimes[1:]):
                if c1<c2:
                    br=1
                    break
            if br==0:
                break
        #print(executionTimes)
        #print()
        #print(rightBoundarySpeeds)
        #print()
        print('Modes = ',M)
        end1 = perf_counter()
        #print('Time Taken to compute Random values is ', (end1-start1)*1000)    
        #continue
        #Start timer
    start = perf_counter()

    #Boundary Speeds
        #Squares of right boundary speeds used to avoid repeated sqrt computation later
        #Speeds in the first step are not counted per Lemma 2 - start from first right boundary speed
    rightBoundarySpeeds =[speed**2 for speed in rightBoundarySpeeds[1:]]

    #Case Flags
    #3 - The initial speed is one of the right boundary speeds and the next job release is at the same speed
    #2 - The initial speed is not a right boundary speed and variable acceleration is to be used
    #1 - Maximum Acceleration is used

    #Helper function to calculate the minimum interarrival time given the initial and final speed - Based on the formulae in Mohaqeqi et al.
    def calc_min_time(speed,speed_new,flag):

        #If speed is a right boundary speed and speed_new is equal to speed...
        if flag == 3:
            peak_speed = speed+a_max

            #If peak_speed does not exceed maximum speed...
            if peak_speed <= rightBoundarySpeeds[-1]:
                #From Mohaquqi et al. Eqn (20) - Accelerate maximimally to peak_speed, decelerate maximally back to speed
                min_time = (sqrt(peak_speed)-sqrt(speed))/a_max + (sqrt(speed)-sqrt(peak_speed))/a_min
            
            #...otherwise peak_speed exceeds maximum speed.
            else:
                #Maintain constant speed
                min_time = 1/sqrt(speed)

            #Return minimum time in seconds
            return min_time*60
        
        #...otherwise, initial speed is not a right boundary speed.
        else:
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

        #Dictionary for logging speeds, flags, execution times, release times - Supports dynamic programming.
        #Speeds in "itemSet" are saved as RPM
        itemSet = defaultdict(dict)

        ##itemSet Population Routine
        #Iterate through all the right boundary speeds to build the item list that is used to fill the Knapsack.
        for i in range(len(rightBoundarySpeeds)):

            #Select right boundary speeds in ascending order
            speed = rightBoundarySpeeds[i]
            
            #Evaluate only ascending speed sequences - per Bijinemula et al. Lemma 2
            while speed<=rightBoundarySpeeds[-1]:

                #If speed is an unlogged right boundary speed...
                if (speed in rightBoundarySpeeds) and (sqrt(speed) not in itemSet.keys()):

                    #Flag rotation as starting from a right boundary speed and ending with the same speed
                    flag = 3 

                    #Calculate release time in seconds
                    release_time = calc_min_time(speed, speed,flag)

                    #Index current speed
                    current_step = bisect_left(rightBoundarySpeeds,speed)

                    #Assign execution time based on index
                    exec_time = executionTimes[current_step]

                    #Log result
                    itemSet[sqrt(speed)][flag] = [exec_time, release_time,sqrt(speed)]
                
                #...otherwise, the speed is not a right boundary or is a logged right boundary.
                else:

                    #Calculate new speed at maximum acceleration
                    speed_new = speed+2*a_max

                    #Index the current speed
                    current_step = bisect_left(rightBoundarySpeeds,speed)
                    
                    #If speed_new exceeds the current right boundary and is not logged
                    if (speed_new > rightBoundarySpeeds[current_step]) and (sqrt(speed) not in itemSet.keys()):

                        #Flag rotation as starting from a non-right boundary speed and having a variable acceleration
                        flag = 2 

                        #Calculate release time in seconds
                        release_time = calc_min_time(speed,rightBoundarySpeeds[current_step],flag)

                        #Assign execution time based on index
                        exec_time = executionTimes[current_step]

                        #Log result
                        itemSet[sqrt(speed)][flag] = [exec_time, release_time,sqrt(rightBoundarySpeeds[current_step])]
                        
                        #If speed_new is less than maximum speed
                        if speed_new < rightBoundarySpeeds[-1]:

                            #Flag rotation as one with maximum acceleration
                            flag = 1

                            #Calculate release time in seconds
                            release_time = 60*((sqrt(speed_new)-sqrt(speed))/a_max)

                            #Log result
                            itemSet[sqrt(speed)][flag] = [exec_time, release_time,sqrt(speed_new)]
                            
                            #Update speed for next iteration
                            speed = speed_new

                        #...otherwise, speed_new exceeds maximum allowable speed.
                        else:
                            #Exit the while loop, moving on to next right boundary
                            break

                    #...otherwise, speed_new does not exceed the current right boundary OR is not logged                                    
                    else:

                        #If speed_new exceeds the maximum allowable speed
                        if speed_new > rightBoundarySpeeds[-1]:
                            #Exit the while loop, moving on to next right boundary
                            break

                        #otherwise, speed_new does not exceed the maximum allowable speed.
                        else:

                            #Flag rotation as one with maximum acceleration
                            flag = 1

                            #Calculate release time in seconds
                            release_time = 60*((sqrt(speed_new)-sqrt(speed))/a_max)

                            #Index the current speed
                            current_step = bisect_left(rightBoundarySpeeds,speed)
                            
                            #Assign execution time based on index
                            exec_time = executionTimes[current_step]

                            #Log result
                            itemSet[sqrt(speed)][flag] = [exec_time, release_time,sqrt(speed_new)]
                            
                            #Update speed
                            speed = speed_new

        #Dictionary for logging speeds, completion times - Supports dynamic programming.
        hashTable = defaultdict(dict)

        #Function for calculating maximum demand given an initial speed over a set duration of time - Bijinemula et al. Algorithm 1
        def calc_demand(speed, time):

            #Initialization
            demand_max = 0
            time = round(time,5)

            #Stored demand check
            if speed in hashTable.keys():
                    if time in hashTable[speed].keys():
                        return hashTable[speed][time]
                    
            if 1 in itemSet[speed].keys():
                flag = 1
            else:
                flag = list(itemSet[speed].keys())[0]
            
            #If remaining time is less than minimum rotation time...
            if time < itemSet[speed][flag][1]:
                #Demand over remaining time is zero
                return 0
            
            #For each possible acceleration type...
            for flag in [3,2,1]:

                #If flag exists for the selected speed...
                if flag in itemSet[speed].keys():

                    #Extract the new speed
                    speed_new = itemSet[speed][flag][2]

                    #Calculate demand using saved value of initial speed AND calculated demand of speed_new
                    demand = itemSet[speed][flag][0] + calc_demand(speed_new,time-itemSet[speed][flag][1])
                    
                    #Update demand_max if needed
                    if demand > demand_max:
                        demand_max = demand
            
            #Save maximum demand to speed-time hash table
            hashTable[speed][time] = demand_max

            #Return maximum demand given initial speed and time window
            return demand_max

        ##Recursive Demand Calculation
        #Initialization
        max_demand = 0
        #f = open('NewAlgoOutput.txt','w')
        
        #For every 0.01 timestep in [0.01,1.01)
        for tot_time in np.arange(0.01,1.01,0.01):

            #For every right boundary speed
            for i in range(len(rightBoundarySpeeds)):

                #Select right boundary speed
                speed = sqrt(rightBoundarySpeeds[i])

                #Calculate maximum demand starting from selected right boundary
                demand = calc_demand(speed,tot_time)

                #Update maximum demand if needed
                if demand > max_demand:
                    max_demand = demand
            #print('Max demand for time: {} = {}'.format(tot_time,max_demand))
            #f.write('Max demand for time: {} = {}\n'.format(tot_time,max_demand))
        #f.close()

        #End performance counting, calculate and log total time
        end = perf_counter()
        fileM = open(fileMname,'a')
        total_time = end - start
        fileM.write(str((end-start))+'\n')
        print('Total time is ',total_time)
        fileM.close()

if __name__ == '__main__':
    NewMultiAVRgen()