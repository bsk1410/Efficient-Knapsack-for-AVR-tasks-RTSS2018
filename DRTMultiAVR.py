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

    #Start timer
    start = perf_counter()

    #Boundary Speeds
        #Squares of right boundary speeds used to avoid repeated sqrt computation later
        #Speeds in the first step are not counted per Lemma 2 - start from first right boundary speed
    boundarySpeeds = [speed**2 for speed in boundarySpeeds]
    maxSpeed = boundarySpeeds[-1]

    #Setup nodeSpeeds
    nodeSpeeds = set()

    #Iterate through all boundary speeds, creating nodes for all reachable speeds
    for i in range(len(boundarySpeeds)):
        speed = boundarySpeeds[i]           #Select boundary speed
        while speed <= maxSpeed:            #While speed has not exceed maxspeed
            nodeSpeeds.add(speed)               #Create node for speed
            speed = speed + 2*a_max             #Add subsequent, increasing speed via a_max
        
        speed = boundarySpeeds[i]           #Select boundary speed
        while speed>=boundarySpeeds[0]:     #While speed has not fallen below the lowest boundary speed
            nodeSpeeds.add(speed)               #Create node for speed
            speed = speed + 2*a_min             #Add subsequent, decreasing speed via a_min
    nodeSpeeds = sorted(nodeSpeeds)         #Nodes sorted by speed increasing order

    #Setup nodes
    nodes = []

    for i,j in zip(nodeSpeeds[:-1],nodeSpeeds[1:]): #For each tuple in a list of created tuples
        nodes.append((i,j))                             #Add each tuple to nodes

    adjMatrix = dict()  #Empty adjacency matrix for creating DRT graph

    for i in range(len(nodes)):                 #For every node tuple
        currentRB = nodes[i][1]                     #Select right boundary
        for j in range(i,len(nodes)):               #Iterate through all possible next right boundaries
            nextRB = nodes[j][1]                        #Select next right boundary
            maxReach = currentRB + 2*a_max              #Calculate maximum next speed

            #If next right boundary is not reachable, break
            if nextRB > maxReach:
                break

            #If next right boundary is reachable via constant a_max...
            if nextRB == maxReach: 
                #Calculate minimum interarrival time - Mohaqeqi et al. Sec. 3.2 Case 2
                adjMatrix[(i,j)] = 60*(sqrt(nextRB)-sqrt(currentRB))/a_max 

            #...otherwise, the next right boundary is reachable via variable acceleration
            else:
                #Calculate the prospective peak speed
                midSpeed = (2*a_min*a_max+a_min*currentRB-a_max*nextRB)/(a_min-a_max)

                #If the prospective peak speed does not exceed maximum speed...
                if midSpeed <= maxSpeed:
                    #Calculate3 minimum interarrival time in seconds - Mohaqeqi et al. Sec 3.2 Eqn 20
                    adjMatrix[(i,j)] = 60*((sqrt(midSpeed)-sqrt(currentRB))/a_max +(sqrt(nextRB)-sqrt(midSpeed))/a_min)

                #...otherwise, the prospective peak speed exceeds maximum speed
                else:
                    #Calculate the time to reach maximum speed - Mohaqeqi et al. Sec. 3.2 Eqn 21 t_1^*
                    t1 = (sqrt(maxSpeed) - sqrt(currentRB))/a_max
                    #Calculate the time over which maximum speed is maintained - Mohaqeqi et al. Sec. 3.2 Eqn 21 t_2^*
                    t2 = (1-((maxSpeed-currentRB)/(2*a_max))-((nextRB-maxSpeed)/(2*a_min)))/sqrt(maxSpeed)
                    #Calculate the time to descend from maximum speed to final speed - Mohaqeqi et al. Sec. 3.2 Eqn 21 t_3^*
                    t3 = (sqrt(nextRB)-sqrt(maxSpeed))/a_min

                    #Sum individual time segments and conver to seconds
                    adjMatrix[(i,j)] = 60*(t1 + t2 + t3)

            #Mirror adjacency matrix
            adjMatrix[(j,i)] = adjMatrix[(i,j)]
            

    #Dictionary for logging speeds, completion times - Supports dynamic programming.
    hashTable = defaultdict(dict)

    #Function for calculating maximum demand given a starting node over a set duration of time
    def calc_demand(i,time):
        
        #Initialization
        demand_max = 0
        time = round(time,5)
        
        #Stored demand check
        if i in hashTable.keys():
            if time in hashTable[i].keys():
                return hashTable[i][time]
        
        #If node is not the first right bounday speed...
        if nodes[i][1]!=boundarySpeeds[0]:
            #Assign execution time based on index
            demNode = executionTimes[bisect_left(boundarySpeeds,nodes[i][1])-1]
        #...otherwise, assign first execution time
        else:
            demNode = executionTimes[0]
        
        #Iterate through all nodes
        for j in range(len(nodes)):

            #If the node pair selected is reachable from each other...
            if (i,j) in adjMatrix.keys():

                #Extract the time required to reach the next node
                timeNextNode = adjMatrix[(i,j)]
                
                #If insufficient time remains to reach the next node...
                if time - timeNextNode < 0:
                    #Do not count towards demand, try next node
                    continue
                
                #If time remaining is exactly the required time...
                if time - timeNextNode == 0:
                    #Update demand if necessary and continue
                    if demNode > demand_max:
                        demand_max = demNode
                        continue
                
                #Calculate new demand
                demand = demNode + calc_demand(j,time-timeNextNode)
            
                #Update demand if necessary
                if demand > demand_max:
                    demand_max = demand
        
        #Update hash table with max demand and return
        hashTable[i][time] = demand_max
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

    #End performance counting, calculate and log total time
    end = perf_counter()
    fileM = open(fileMname,'a')
    total_time = end - start
    fileM.write(str((end-start))+'\n')
    print('Total time is ',total_time)
    fileM.close()

if __name__ == '__main__':
    M = int(sys.argv[1])
    DRTMultiAVRgen(M)