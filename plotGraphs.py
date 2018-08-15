import matplotlib.pyplot as plt
plt.style.use('seaborn-poster')
import numpy as np

baseName = 'DRTAlgoMultiAVRTests/DRTAlg_MultiAVR_'

DRTRuntimes = []

for i in range(6,16):
	with open(baseName+str(i)+'.txt') as f:
		content = f.readlines()
	currRuntime = [float(x.strip('\n')) for x in content]
	
	DRTRuntimes.append(np.mean(currRuntime))

baseName = 'NewAlgMultipleAVRTests/NewAlg_Multi_'

NewAlgRuntimes = []

for i in range(6,16):
	with open(baseName+str(i)+'.txt') as f:
		content = f.readlines()
	currRuntime = [float(x.strip('\n')) for x in content]
	
	NewAlgRuntimes.append(np.mean(currRuntime))

plt.figure()
plt.plot(range(6,16),DRTRuntimes,label='DRT Alg.')
plt.plot(range(6,16),NewAlgRuntimes,'--',label='Our Alg.')
plt.xlabel('Number of Modes')
plt.ylabel('Runtime (sec)')
plt.legend()
plt.show()

