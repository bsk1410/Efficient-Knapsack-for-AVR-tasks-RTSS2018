#Dependencies
import NewMultiAVR
import DRTMultiAVR
import plotGraphs

#Run NewAlg for Mode count 6 through 15
NewMultiAVR.NewMultiAVRgen()

#Run DRT Alg
DRTMultiAVR.DRTMultiAVRgen(1)

#Compare Graphs
plotGraphs.multiAVRPlot()