#Dependencies
import NewMultiAVR  #Knapsack Algorithm
import DRTMultiAVR  #DRT Algorithm
import plotGraphs   #Graph plotting script
import argparse     #To read command line arguments
import sys          #Handle command-line arguments

#Parse Command-Line Arguments
parser = argparse.ArgumentParser(description='Run the Knapsack and DRT AVR Task Demand Calculations, graph results')
parser.add_argument('-r','--runs', metavar='N', type=int,default='1',help ='Enter the number of times to run per Mode Count (positive integer)')
args = parser.parse_args()

#Validate Input
if(args.runs < 0):
    print("Negative run count. Runs must be 0 or greater")

#Accept input
runsPerMode = args.runs

#Input Args
print("Executing ",runsPerMode," run(s) per Mode Count")


#Run NewAlg for Mode count 6 through 15
print("---Knapsack-Based Algorithm---")
for r in range(0,runsPerMode):
    print("\tExecuting Run ",r," of ", runsPerMode," for Mode Counts 6-15")
    NewMultiAVR.NewMultiAVRgen()

#Run DRT Alg for Mode count 6 through 15
print("---DRT Algorithm---")
for r in range(0,runsPerMode):
    print("\tExecuting Run ",r," of ", runsPerMode," for Mode Counts 6-15")
    for i in range(6,16):
        DRTMultiAVR.DRTMultiAVRgen(i)

#Compare Graphs
plotGraphs.multiAVRPlot()