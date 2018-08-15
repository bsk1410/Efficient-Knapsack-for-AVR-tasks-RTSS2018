from time import perf_counter
#start = perf_counter()
from math import sqrt
from collections import defaultdict
import numpy as np
from pprint import pprint
import random
from bisect import bisect_left

a_max = 600000
a_min = -600000

#Multiple AVR Tasks generation
#inputs that need to given - Umax, M_min, M_max, Umax
for M in range(5,16):
    a_max = 600000
    a_min = -600000
    fileMname = 'NewAlgo_Multi_'+str(M)+'.txt'
    
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
    start = perf_counter()

    rightBoundarySpeeds = [i**2 for i in rightBoundarySpeeds][1:]

    def calc_min_time(speed,speed_new,flag):
        if flag == 3:
            temp_speed = speed+a_max
            if temp_speed <= rightBoundarySpeeds[-1]:
                min_time = (sqrt(temp_speed)-sqrt(speed))/a_max + (sqrt(speed)-sqrt(temp_speed))/a_min
            else:
                min_time = 1/sqrt(speed)
            return min_time*60
        
        temp_speed = (2*a_max*a_min+a_min*speed-a_max*speed_new)/(a_min-a_max)
       
        if temp_speed <= rightBoundarySpeeds[-1]:
            min_time = (sqrt(temp_speed)-sqrt(speed))/a_max + (sqrt(speed_new)-sqrt(temp_speed))/a_min
        else:
            min_time = ((sqrt(rightBoundarySpeeds[-1])-sqrt(speed))/a_max) + ((1 - ((rightBoundarySpeeds[-1]-speed)/(2*a_max))-((speed_new-rightBoundarySpeeds[-1])/(2*a_min)))/sqrt(rightBoundarySpeeds[-1])) + ((sqrt(speed_new)-sqrt(rightBoundarySpeeds[-1]))/a_min)
        return min_time*60  #to convert into seconds



    #3 - right boundary speed
    #2 - Special Speed
    #1 - normal iteration

    boxSet1 = defaultdict(dict)

    for i in range(len(rightBoundarySpeeds)):
        speed = rightBoundarySpeeds[i]
        
        #ascending speeds
        while speed<=rightBoundarySpeeds[-1]:
            if (speed in rightBoundarySpeeds) and (sqrt(speed) not in boxSet1.keys()):
                flag = 3   #represents right boundary speed
                release_time = calc_min_time(speed, speed,flag)   #60/sqrt(speed)   #in seconds
                current_step = bisect_left(rightBoundarySpeeds,speed)
                exec_time = executionTimes[current_step]
                boxSet1[sqrt(speed)][flag] = [exec_time, release_time,sqrt(speed)]
                
            else:
                speed_new = speed+2*a_max
                current_step = bisect_left(rightBoundarySpeeds,speed)
                
                if (speed_new > rightBoundarySpeeds[current_step]) and (sqrt(speed) not in boxSet1.keys()):
                    flag = 2   #represents Special Speed
                    release_time = calc_min_time(speed,rightBoundarySpeeds[current_step],flag)    #120/(sqrt(speed)+sqrt(rightBoundarySpeeds[current_step]))
                    exec_time = executionTimes[current_step]
                    boxSet1[sqrt(speed)][flag] = [exec_time, release_time,sqrt(rightBoundarySpeeds[current_step])]
                    
                    if speed_new < rightBoundarySpeeds[-1]:
                        flag = 1
                        release_time = 60*((sqrt(speed_new)-sqrt(speed))/a_max)
                        boxSet1[sqrt(speed)][flag] = [exec_time, release_time,sqrt(speed_new)]
                        speed = speed_new

                    else:
                        break
                                        
                else:
                    if speed_new > rightBoundarySpeeds[-1]:
                        break
                    flag = 1
                    release_time = 60*((sqrt(speed_new)-sqrt(speed))/a_max)
                    current_step = bisect_left(rightBoundarySpeeds,speed)
                    exec_time = executionTimes[current_step]
                    boxSet1[sqrt(speed)][flag] = [exec_time, release_time,sqrt(speed_new)]
                    speed = speed_new
        
        
                
                
                
    #3 - right boundary speed
    #2 - Special Speed
    #1 - normal iteration
    saved_map1 = defaultdict(dict)
    c = 0
    d = 0
    def calc_demand1(speed, time):
        demand_max = 0
        time = round(time,5)
        if speed in saved_map1.keys():
                if time in saved_map1[speed].keys():
                    return saved_map1[speed][time]
                
        #flag is chosen so that time left is compared with the minimum rotation time from a given speed
        if 1 in boxSet1[speed].keys():
            flag = 1
        else:
            flag = list(boxSet1[speed].keys())[0]
            
        if time < boxSet1[speed][flag][1]:
            return 0
        
        for flag in [3,2,1]:
            if flag in boxSet1[speed].keys():
                speed_new = boxSet1[speed][flag][2]
                demand = boxSet1[speed][flag][0] + calc_demand1(speed_new,time-boxSet1[speed][flag][1])
                
                if demand > demand_max:
                    demand_max = demand
                    
        saved_map1[speed][time] = demand_max
        return demand_max

    #Recursion Start
    max_demand = 0
    #f = open('NewAlgoOutput.txt','w')
    for tot_time in np.arange(0.01,1.01,0.01):
        for i in range(len(rightBoundarySpeeds)):
            speed = sqrt(rightBoundarySpeeds[i])
            demand = calc_demand1(speed,tot_time)
            
            if demand > max_demand:
                max_demand = demand
        #print('Max demand for time: {} = {}'.format(tot_time,max_demand))
        #f.write('Max demand for time: {} = {}\n'.format(tot_time,max_demand))
    #f.close()
    end = perf_counter()
    fileM = open(fileMname,'a')

    total_time = end - start
    
    fileM.write(str((end-start))+'\n')
    print('Total time is ',total_time)
    fileM.close()