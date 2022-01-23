import math 
import numpy as np


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
    
    return bins

def equi_freq(arr, freq):
    
    length = len(arr) 
    number_of_bins = math.ceil(length / freq) 
    print(number_of_bins, 'bins') 
    bins = list()

    for x in range(number_of_bins): 
        bins.append(arr[x * freq : (x+1) * freq])

    return bins


def median_smoothing(bins, number_of_bins):
    
    for i in range(number_of_bins):
        if len(bins[i]):
            bins[i] = list(np.ones(len(bins[i])) * round(np.median(np.array(bins[i])), 2))

    return bins

def boundary_smoothing(bins, number_of_bins): 
    
    for i in range(number_of_bins): 
        
        for index in range(len(bins[i])):
            
            if abs(bins[i][index] - bins[i][0]) <= abs(bins[i][index] - bins[i][-1]):
                bins[i][index] = bins[i][0]
            
            else:
                bins[i][index] = bins[i][-1]

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

print("\n===============================================================================")
#taking the choice from the user and implementing the according logic as per user's choice
choice = int(input('Enter the choice for method of binning : '))

print("\n================================================================================")
if choice == 1: 
    number_of_bins = int(input('Enter Number of bins : ')) 
    bins = equi_width(arr, number_of_bins)

elif choice == 2:
    width_of_bins = int(input('Enter Width of the bin : ')) 
    bins = equi_freq(arr, width_of_bins)

print("Result after performing the binning method:")
print(bins)
            

print("\n ================================Smoothing Method Choices========================")
print('\n1. Smoothing using Bin Median') 
print('2. Smoothing using Bin Boundary\n')

choice = int(input('Enter the choice for method of smoothing : ')) 
number_of_bins = len(bins)

if choice == 1: 
    bins = median_smoothing(bins, number_of_bins)

elif choice == 2: 
    bins = boundary_smoothing(bins, number_of_bins)

for bin in bins:
    print(bin)