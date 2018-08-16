#Dependencies
import NewMultiAVR  #Knapsack Algorithm
import DRTMultiAVR  #DRT Algorithm
import plotGraphs   #Graph plotting script
import sys          #Handle command-line arguments

#Input Args
runsPerMode = int(sys.argv[1])
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