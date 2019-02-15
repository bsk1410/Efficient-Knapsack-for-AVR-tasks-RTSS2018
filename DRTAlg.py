#Dependencies
from time import perf_counter               #Performance counter - clock with highest available resolution
from math import sqrt                       #Square root
from collections import defaultdict         #Dictionary that does not throw KeyErrors
import numpy as np                          #http://www.numpy.org/
import argparse                             #To read command line arguments
from bisect import bisect_left              #Provides would-be index of element to insert
import json                                 #To read the input taskset file
from argparse import RawTextHelpFormatter   #Argument Parser help formatting
import sys                                  #Exit command

#Units
#a_max, a_min - revolutions / min^2
#speed, peak_speed, speed_new - revolutions / minute (RPM)

#Acceleration equal in magnitude to deceleration per Bijinemula et al. Sec. III.A Para. 4 
a_max = 600000
a_min = -a_max

#Execution time values (micro seconds) from Mohaqeqi et al. Table 18 - http://user.it.uu.se/~yi/pdf-files/2017/ecrts17.pdf
executionTimes = [965, 576, 424, 343, 277, 246]

#Parse Command-Line Arguments
parser = argparse.ArgumentParser(description='Run the Knapsack-Based AVR Task Demand Calculation algorithm by Bijinemula et al.', formatter_class=RawTextHelpFormatter)
parser.add_argument('-t','--taskset',choices=['1','2','3'],metavar='#',default='1',help ='Enter the taskset number to run the algorithm on.\n1 - Use Task Set #1 in Bijinemula et al.\n2 - Use Task Set #2 in Bijinemula et al.\n3 - Use the custom, user-defined task set in \'taskSetCustom.json\'')
parser.add_argument('-v','--verbose',action='store_true',help='Get detailed output')
args = parser.parse_args()

#If task set 1 is selected...
if args.taskset == '1':
    #Use boundary speeds, execution times, acceleration of Taskset 1 in Bijinemula et al. Table I
    taskSetFileName = 'taskSet1.json'
#If task set 2 is selected...
elif args.taskset == '2':
    #Use boundary speeds, execution times, acceleration of Taskset 2 in Bijinemula et al. Table II
    taskSetFileName = 'taskSet2.json'
#...otherwise, default to custom task set
else:
    #Use boundary speeds, execution times, acceleration of the user's custom task set in 'taskSetCustom.json'
    taskSetFileName = 'taskSetCustom.json'

#Open Task Set File
with open(taskSetFileName) as f:
    taskset = json.load(f)

#Sort Right Boundary Speeds in increasing order
boundarySpeeds = sorted(taskset['boundarySpeeds'])

#Sort execution times in decreasing order
executionTimes = sorted(taskset['executionTimes'], reverse=True)

#Set accelerations equal in magnitude
a_max = taskset['a_max']
a_min = -a_max

#Validate # Right Boundary Speeds is one more than # Execution Times 
if len(boundarySpeeds) != len(executionTimes)+1:
    print('Error: The number of boundary speeds should be one more than the number of execution times.')
    sys.exit(0)

#Print Parameters:
print('Task File:      ',taskSetFileName)
print('boundarySpeeds: ',boundarySpeeds, 'revolutions / minute')
print('executionTimes: ',executionTimes, 'us')
print('a_max:          ',a_max, ' revolutions / min^2')
print('a_min:          ',a_min, 'revolutions / min^2')
print('Executing...')

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