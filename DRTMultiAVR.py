from time import perf_counter
from math import sqrt
from bisect import bisect_left #to find the first element greater than a given number in a list
from collections import defaultdict
import numpy as np
import random
import sys

def DRTMultiAVRgen(M):

    # Multiple AVR Tasks generation
    # inputs that need to given - Umax, M_min, M_max, Umax
    #M = int(sys.argv[1])
    a_max = 600000
    a_min = -600000
    fileMname = 'DRTMultiAVROutputs/DRTAlg_MultiAVR'+str(M)+'.txt'

    # start1 = perf_counter()
    random.seed(100)
    Ustar = 0.25
    Udict = dict()
    for i in range(M):
        Udict[i] = random.uniform(0.85*Ustar, Ustar)
    Udict[M-1] = Ustar

    while True:
        while True:
            boundarySpeeds = sorted(random.sample(range(500,6500),M-1))
            boundarySpeeds = [500]+boundarySpeeds+[6500]
            for i in range(M):
                k = i
                if boundarySpeeds[i+1] - boundarySpeeds[i] < 3000/M:
                    continue
                    
            if k==M-1:
                break
        br = 0
        executionTimes = []
        for i in range(M):
            executionTimes.append(1000**2*Udict[i]*60/boundarySpeeds[i])   #in micro seconds
        for c1,c2 in zip(executionTimes[:-1],executionTimes[1:]):
            if c1<c2:
                br=1
                break
        if br==0:
            break

    # print(executionTimes)
    # print()
    # print(boundarySpeeds)
    # print()
    print('Modes = ',M)
    # end1 = perf_counter()
    # print('Time Taken to compute Random values is ', (end1-start1)*1000)

    start = perf_counter()
    boundarySpeeds = [i**2 for i in boundarySpeeds]
    maxSpeed = boundarySpeeds[-1]


    nodespeeds = set()
    for i in range(len(boundarySpeeds)):
        speed = boundarySpeeds[i]
        while speed <= boundarySpeeds[-1]:
            nodespeeds.add(speed)
            speed = speed + 2*a_max
        
        speed = boundarySpeeds[i]
        while speed>=boundarySpeeds[0]:
            nodespeeds.add(speed)
            speed = speed + 2*a_min
    nodespeeds = sorted(nodespeeds)


    nodes = []
    for i,j in zip(nodespeeds[:-1],nodespeeds[1:]):
        nodes.append((i,j))



    adjMatrix = dict()
    for i in range(len(nodes)):
        currentRB = nodes[i][1]
        for j in range(i,len(nodes)):
            nextRB = nodes[j][1]
            maxReach = currentRB + 2*a_max
            if nextRB > maxReach:
                break
                
            if nextRB == maxReach:
                adjMatrix[(i,j)] = 60*(sqrt(nextRB)-sqrt(currentRB))/a_max
            else:
                midSpeed = (2*a_min*a_max+a_min*currentRB-a_max*nextRB)/(a_min-a_max)
                if midSpeed <= maxSpeed:
                    adjMatrix[(i,j)] = 60*((sqrt(midSpeed)-sqrt(currentRB))/a_max +(sqrt(nextRB)-sqrt(midSpeed))/a_min)
                else:
                    t1 = (sqrt(maxSpeed) - sqrt(currentRB))/a_max
                    t2 = (1-((maxSpeed-currentRB)/(2*a_max))-((nextRB-maxSpeed)/(2*a_min)))/sqrt(maxSpeed)
                    t3 = (sqrt(nextRB)-sqrt(maxSpeed))/a_min
                    adjMatrix[(i,j)] = 60*(t1 + t2 + t3)
            adjMatrix[(j,i)] = adjMatrix[(i,j)]
            

    saved_map = defaultdict(dict)

    def calc_demand(i,time):
        demand_max = 0
        
        time = round(time,5)
        
        if i in saved_map.keys():
            if time in saved_map[i].keys():
                return saved_map[i][time]
            
        if nodes[i][1]!=boundarySpeeds[0]:
            demNode = executionTimes[bisect_left(boundarySpeeds,nodes[i][1])-1]#execution_time(sqrt(nodes[i][1]))
        else:
            demNode = executionTimes[0]
        
        for j in range(len(nodes)):
            if (i,j) in adjMatrix.keys():
                timeNextNode = adjMatrix[(i,j)]
                
                if time - timeNextNode < 0:
                    continue
                
                if time - timeNextNode == 0:
                    if demNode > demand_max:
                        demand_max = demNode
                        continue
                
                demand = demNode + calc_demand(j,time-timeNextNode)
            
                if demand > demand_max:
                    demand_max = demand
        
        saved_map[i][time] = demand_max
        return demand_max

    #f = open('DRTAlgoOutput.txt','w')
    for tot_time in np.arange(0.01,1.01,0.01):
        max_demand = 0
        for i in range(len(nodes)):
            demand = calc_demand(i,tot_time)
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

if __name__ == '__main__':
    M = int(sys.argv[1])
    DRTMultiAVRgen(M)