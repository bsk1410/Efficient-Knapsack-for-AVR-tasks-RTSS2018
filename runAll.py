#Dependencies
import NewMultiAVR  #Knapsack Algorithm
import DRTMultiAVR  #DRT Algorithm
import plotGraphs   #Graph plotting script
import argparse     #To read command line arguments
import sys          #Handle command-line arguments

#Parse Command-Line Arguments
parser = argparse.ArgumentParser(description='Run the Knapsack and DRT AVR Task Demand Calculations, graph results')
parser.add_argument('-r','--runs', metavar='N', type=int,default='1',help ='Enter the number of times to run per Mode Count (positive integer)')
parser.add_argument('-m','--minMode', metavar='N', type=int,default='6',help ='Enter the min Number of Modes (positive integer)')
parser.add_argument('-M','--maxMode', metavar='N', type=int,default='15',help ='Enter the max Number of Modes (positive integer)')
args = parser.parse_args()

#Validate Input
if(args.runs < 0):
    print("Negative run count. Runs must be 0 or greater")
    exit(-1)

if(args.minMode < 0):
    print("Negative min Number of Modes. Min Number of Modes must be 0 or greater")
    exit(-2)

if(args.maxMode < 0):
    print("Negative max Number of Modes. Max Number of Modes must be 0 or greater")
    exit(-3)

if(args.maxMode < args.minMode):
    print("Max Number of Modes is less than Min Number of Modes. Max Number of Modes must be >= Min Number of Modes")
    exit(-4)

#Accept input
runsPerMode = args.runs
minNumMode = args.minMode
maxNumMode = args.maxMode

#Input Args
print("Executing ",runsPerMode," run(s) per Mode Count")

#Run NewAlg for Mode count 6 through 15
print("---Knapsack-Based Algorithm---")
for r in range(0,runsPerMode):
    print("\tExecuting Run ",r," of ", runsPerMode," for Mode Counts ",minNumMode,"-",maxNumMode)
    for m in range(minNumMode,maxNumMode+1):
        NewMultiAVR.NewMultiAVRgen(m)

#Run DRT Alg for Mode count 6 through 15
print("---DRT Algorithm---")
for r in range(0,runsPerMode):
    print("\tExecuting Run ",r," of ", runsPerMode," for Mode Counts ",minNumMode,"-",maxNumMode)
    for m in range(minNumMode,maxNumMode+1):
        DRTMultiAVR.DRTMultiAVRgen(m)

#Compare Graphs
plotGraphs.multiAVRPlot()