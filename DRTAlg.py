from time import perf_counter           #Performance counter - clock with highest available resolution
from math import sqrt                   #Square root
from bisect import bisect_left          #to find the first element greater than a given number in a list
from collections import defaultdict     #Dictionary that does not throw KeyErrors
import numpy as np                      #http://www.numpy.org/
import argparse                         #To read command line arguments
import json                             #To read the input taskset file
import sys

#Units
#a_max, a_min - revolutions / min^2
#speed, peak_speed, speed_new - revolutions / minute (RPM)
a_max = 600000
a_min = -600000

#Execution time values (micro seconds) from the Mohaqeqi et al. - http://user.it.uu.se/~yi/pdf-files/2017/ecrts17.pdf
executionTimes = [965,576,424,343,277,246]

a_max = 600000
a_min = -600000

#parse input arguments
parser = argparse.ArgumentParser(description='Run the algorithm by Bijinemula et al.')
parser.add_argument('-t','--taskset',choices=['1','2','3'],metavar='',default='1',help ='Enter the taskset to run the algorithm on. For a new taskset enter -t 3 -i <space separated filename>')
parser.add_argument('-v','--verbose',action='store_true',help='Get detailed output')
args = parser.parse_args()

if args.taskset == '1':
    boundarySpeeds = range(500,7500,1000)
elif args.taskset == '2':
    #boundary speeds of taskset-2 in Bijinemula et al.
    boundarySpeeds = range(1200,8200,1000)
else:
    #custom taskset
    with open('taskset.json') as f:
        taskset = json.load(f)

    #sort the boundary speeds so that they are in increasing order
    boundarySpeeds = sorted(taskset['boundarySpeeds'])
    #sort the execution times so that they are in decreasing order
    executionTimes = sorted(taskset['executionTimes'], reverse=True)
    a_max = taskset['a_max']
    a_min = taskset['a_min']

    if len(boundarySpeeds) != len(executionTimes)+1:
        print('Error: The number of boundary speeds should be one more than the number of execution times.')
        sys.exit(0)

    if a_max != -a_min:
        print('Error: The magnitude of a_max and a_min should be the same as mentioned in the paper.')
        sys.exit(0)

#Start timer
start = perf_counter()

#Boundary Speeds
    #Squares of right boundary speeds used to avoid repeated sqrt computation later
    #Speeds in the first step are not counted per Lemma 2 - start from first right boundary speed
boundarySpeeds = [speed**2 for speed in boundarySpeeds]
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
        
    if nodes[i][1]!=boundarySpeeds[0]:
        demNode = executionTimes[bisect_left(boundarySpeeds,nodes[i][1])-1]
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
    
    hashTable[i][time] = demand_max
    return demand_max


##Recursive Demand Calculation
#Initialization
max_demand = 0

#If verbose requested - store the demand values corresponding to each time-step in a file
if args.verbose:
    f = open('DRTAlgOutput.txt','w')
    
#For every 0.01 timestep in [0.01,1.01)    
for tot_time in np.arange(0.01,1.01,0.01):

    #For each node
    for i in range(len(nodes)):

        #Calculate maximum demand starting from the selected node
        demand = calc_demand(i,tot_time)

        #Update maximum demand if needed
        if demand > max_demand:
            max_demand = demand

    #If verbose requested write the demand for this time-step to file
    if args.verbose:
        f.write('Max demand for time: {} = {}\n'.format(tot_time,max_demand))

#File handling
if args.verbose:
    f.close()

#End performance counting, calculate and log total time
end = perf_counter()
total_time = end - start
print('Total time is ',total_time)

#If verbose output is requested
if args.verbose:
    print('Total demand corresponding to each timestep is given in the file DRTAlgOutput.txt.')