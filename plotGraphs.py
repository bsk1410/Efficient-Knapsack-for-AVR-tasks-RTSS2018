#Dependencies
import numpy as np                  #http://www.numpy.org/
import matplotlib.pyplot as plt     #https://matplotlib.org/api/pyplot_api.html

def multiAVRPlot():

    #Initialization
    plt.style.use('seaborn-poster')

    #DRT Extraction Initialization
    baseName = 'DRTMultiAVROutputs/DRTAlg_MultiAVR_'
    DRTRuntimes = []

    #Extracting DRT Runtimes
    for i in range(6,16):
        with open(baseName+str(i)+'.txt') as f:
            content = f.readlines()
        currRuntime = [float(x.strip('\n')) for x in content]
        
        DRTRuntimes.append(np.mean(currRuntime))

    #New Alg Extraction Initialization
    baseName = 'NewMultiAVROutputs/NewAlg_Multi_'
    NewAlgRuntimes = []

    #Extracting New Alg Runtimes
    for i in range(6,16):
        with open(baseName+str(i)+'.txt') as f:
            content = f.readlines()
        currRuntime = [float(x.strip('\n')) for x in content]
        
        NewAlgRuntimes.append(np.mean(currRuntime))

    #Constuct Plot
    plt.figure()                                                #Figure Init
    plt.plot(range(6,16),DRTRuntimes,label='DRT Alg.')          #DRT Data Plotting
    plt.plot(range(6,16),NewAlgRuntimes,'--',label='Our Alg.')  #New Alg Data Plotting

    #Label and Legend Generation
    plt.xlabel('Number of Modes')
    plt.ylabel('Runtime (sec)')
    plt.legend()

    #Show plot to user
    plt.show()

if __name__ == '__main__':
    multiAVRPlot()