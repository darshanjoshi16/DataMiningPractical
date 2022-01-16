#importing the needfull library for binning and smoothing method
import numpy as np
import math

#defining the equi_width function which will take the array of elements and number of bins as input parameter
#this function returns the bins in which data is binned according to the width
def equi_width(arr, no_of_bins):
        
        s = arr[0] 
        e = arr[-1] 
        bins_ranges = np.linspace(s, e, no_of_bins + 1) 
        print('boundries of bins :', bins_ranges) 
        bins = [list() for i in range(no_of_bins)]

        current_bin = 0 
        end = 1

        for ele in arr:
            
            if ele <= bins_ranges[end]:
                 bins[current_bin].append(ele)
            
            elif current_bin < no_of_bins:
                while ele > bins_ranges[end]:
                    current_bin += 1 
                    end += 1
                bins[current_bin].append(ele)

            for i in range(no_of_bins):
                if len(bins[i]):
                    bins[i] = list(np.ones(len(bins[i])) * round(np.array(bins[i]).mean(), 2))

        
        return bins

#defining the equi_frequncy function which will take the array of elements and frequency as input parameter
#this function returns the bins in which data is binned according to the frequency of data
def equi_freq(arr, freq):
        
        length = len(arr) 
        number_of_bins = math.ceil(length / freq) #ceiling function which takes the lowest integer among all integers > fraction value 
        print(number_of_bins, 'bins') 
        bins = list()

        for x in range(number_of_bins): 
            bins.append(arr[x * freq : (x+1) * freq])
            
        for i in range(number_of_bins): 
            bins[i] = list(np.ones(freq) * round(np.array(bins[i]).mean(), 2))

        return bins

#driver code of our implementation
print("======================Handling the Noisy Data===============================")
print("\n====================Data Smoothing by Binning=============================")

#taking the input from user and splitting using ',' delimiter
print('Enter the data you want to smooth (seperate with comma) : ') 
arr = [float(x) for x in input().split(',')] 

#binning can be implemented if and only the data is sorted so, here we are sorting the data
arr.sort()
print(arr)

print("\n ================================Binning Method Choices========================")
print('\n1. Equal Width or distance binning') 
print('2. Equal depth or frequency binning\n')

#taking the choice from the user and implementing the according logic as per user's choice
choice = int(input('Enter the choice for method of binning : '))

if choice == 1: 
    no_of_bins = int(input('Enter Number of bins : '))
    bins = equi_width(arr, no_of_bins)

elif choice == 2: 
    width_of_bins = int(input('Enter Width of the bin : '))
    bins = equi_freq(arr, width_of_bins)

#showing the output after performing smoothing by bin means method
print("Result after performing the smoothing binning method:")
print(bins)



