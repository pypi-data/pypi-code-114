
import math,re,subprocess,os
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
class Processor:
    def __init__(self,ParameterNumber,outputvalues,outCount,datavalues):
        """
        This class performs stastistical Analysis on results and returns mean, std of each result, and generates a few graphs.
        """
        #First the mean/std value of the inputs will be determined and displayed to the user.
        for i in range(ParameterNumber):
            meaninpValue = datavalues[i].mean()
            stdinpValue = datavalues[i].std()
            print("The mean of Input Paramater " + str(i+1) + " is " + str(meaninpValue))
            print("The standard deviation of Input Paramater " + str(i+1) + " is " + str(stdinpValue))

        #Determine if the passed in away is 2 or 3 dimensions passed out number of outCounts. Perform Basic Statistics on the Outputs.
        #Graph Each result, Parameter versus output.
        #As the response has been sorted automatically, it is necessary to sort the input as well.
        #Perform a linear regression, and plot fitted line.
            if outCount >1:
                for k in range(outCount):
                    meanoutValue = outputvalues[i,:,k].mean()
                    stdoutValue = outputvalues[i,:,k].std()
                    print("The mean of Output Paramater " + str(k+1) + " is " + str(meanoutValue))
                    print("The standard deviation of Output Paramater " + str(k+1) + " is " + str(stdoutValue))

                    plt.plot(np.sort(datavalues[i]),outputvalues[i,:,k], label = ("original data"))
                    plt.title('Plot of Parameter '+str(i+1) + ' Vs. Output ' + str(k+1))
                    plt.xlabel('Parameter ' +str(i+1))
                    plt.ylabel('Output ' +str(k+1))
                    res = stats.linregress(datavalues[i],outputvalues[i,:,k])
                    plt.plot(np.sort(datavalues[i]), res.intercept + res.slope*np.sort(datavalues[i]), 'r', label='fitted line')
                    plt.legend()
                    plt.show()
                    print(res)


            else:
                meanoutValue = outputvalues[i].mean()
                stdoutValue = outputvalues[i].std()
                print("The mean of the output is " +str(meanoutValue))
                print("The mean of the output is " +str(stdoutValue))
                print(datavalues)
                plt.plot(np.sort(datavalues[i]),outputvalues[i,:],label = ("original data"))
                plt.title('Plot of Parameter '+str(i+1) + ' Vs. Output 1')
                plt.xlabel('Parameter ' +str(i+1))
                plt.ylabel('Output 1')
                res = stats.linregress(datavalues[i],outputvalues[i,:])
                plt.plot(np.sort(datavalues[i]), res.intercept + res.slope*np.sort(datavalues[i]), 'r', label='fitted line')
                plt.legend()
                plt.show()



