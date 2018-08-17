#Dependencies
import numpy as np                  #http://www.numpy.org/
import matplotlib.pyplot as plt     #https://matplotlib.org/api/pyplot_api.html

def multiAVRPlot():

    #Initialization
    plt.style.use('seaborn-poster')

    #DRT Extraction Initialization
    baseName = 'DRTMultiAVROutputs/DRTAlg_MultiAVR_'
    multiDRTRuntimes = []

    #Extracting MultiAVR DRT Runtimes
    for i in range(6,16):
        with open(baseName+str(i)+'.txt') as f:
            content = f.readlines()
        currRuntime = [float(x.strip('\n')) for x in content]
        
        multiDRTRuntimes.append(np.mean(currRuntime))

    #New Alg Extraction Initialization
    baseName = 'NewMultiAVROutputs/NewAlg_Multi_'
    multiNewAlgRuntimes = []

    #Extracting MultiAVR New Alg Runtimes
    for i in range(6,16):
        with open(baseName+str(i)+'.txt') as f:
            content = f.readlines()
        currRuntime = [float(x.strip('\n')) for x in content]
        
        multiNewAlgRuntimes.append(np.mean(currRuntime))

    #Extracting DRT Alg Runtimes for pre-defined tasksets
    baseName = 'DRTMultiAVROutputs/DRTAlg_'
    DRTAlgRuntimes = []
    for i in [1,2]:
        with open(baseName+str(i)+'.txt') as f:
            content = f.readlines()
        currRuntime = [float(x.strip('\n')) for x in content]
    
        DRTAlgRuntimes.append(np.mean(currRuntime))
    

    #Extracting New Alg Runtimes for pre-defined tasksets
    baseName = 'NewMultiAVROutputs/NewAlg_'
    NewAlgRuntimes = []
    for i in [1,2]:
        with open(baseName+str(i)+'.txt') as f:
            content = f.readlines()
        currRuntime = [float(x.strip('\n')) for x in content]
    
        NewAlgRuntimes.append(np.mean(currRuntime))

    #Initialize Improvement Ratios
    improvementRatios = []

    #Calculate Improvement Ratios
    for i in range(0,10):
        improvementRatios.append(multiDRTRuntimes[i]/multiNewAlgRuntimes[i])

    for i in range(0,2):
        improvementRatios.append(DRTAlgRuntimes[i]/NewAlgRuntimes[i])
    
    #Display Improvement Ratios
    print("Improvement Ratios (DRT Time / Knapsack Time):")
    print(improvementRatios)
    print("Minimum Improvement", min(improvementRatios))
    print("Average Improvement", sum(improvementRatios)/len(improvementRatios))

    #Constuct Plot
    plt.figure()                                                #Figure Init
    plt.plot(range(6,16),multiDRTRuntimes,label='DRT Alg.')          #DRT Data Plotting
    plt.plot(range(6,16),multiNewAlgRuntimes,'--',label='Our Alg.')  #New Alg Data Plotting

    #Title, Label and Legend Generation
    plt.title('Runtime vs Number of Modes')
    plt.xlabel('Number of Modes')
    plt.ylabel('Runtime (sec)')
    plt.xticks(range(6,16))                   #Display all the points on the x-axis
    plt.legend()

    #Uncomment the bottom line to save the plot
    #plt.savefig('runtimePlot.png',bbox_inches='tight')

    #Show plot to user
    plt.show()

if __name__ == '__main__':
    multiAVRPlot()