#Dependencies
import NewAlgMultipleAVRTests.NewAlg_MultiAVR
import DRTAlgMultiAVRTests.DRTAlg_MultiAVR
import plotGraphs

#Run NewAlg for Mode count 6 through 15
NewAlgMultipleAVRTests.NewAlg_MultiAVR.NewMultiAVRgen()

#Run DRT Alg
DRTAlgMultiAVRTests.DRTAlg_MultiAVR.DRTMultiAVRgen(1)

#Compare Graphs
plotGraphs.multiAVRPlot()