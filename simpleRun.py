#Dependencies
import NewMultiAVR
import DRTMultiAVR
import plotGraphs

#Run NewAlg for Mode count 6 through 15
NewMultiAVR.NewMultiAVRgen()

#Run DRT Alg for Mode count 6 through 15
for i in range(6,16):
    DRTMultiAVR.DRTMultiAVRgen(i)

#Compare Graphs
plotGraphs.multiAVRPlot()