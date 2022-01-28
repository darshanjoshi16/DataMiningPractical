#practical 6: Implementation of Min-Max Normalization on the records as part of Data Preprocessing

#importing the libraries required to perform the task 
import numpy as np
import pandas as pd

#defining the Min-max normalization function which takes the list as the input parameter
def normalize(x):
    min = float(input("Enter your current minimum value: "))
    max = float(input("Enter your current maximum value: "))
    print("\n===============================================")
    newLowerBound = float(input("Enter your new minimum value: ")) 
    newUpperBound = float(input("Enter your new maximum value: "))
    range = max - min
    newRange = newUpperBound - newLowerBound

    return [((a - min) / range) * newRange + newLowerBound for a in x]


#driver code for the implementation

print("=============Min-Max Normalization===========")

#section 1:Lets create the dataframe for the first university
print("\n ==========Enter the records for University 1===========")
#taking the number of records from user as input
n1= int(input("Enter the number of records you want to normalize:"))
print("\n========================================================")

#name of candidate and performance index is taken in input and appended in the list of name and perform_index
name = [input("Enter the name of candidate "+str(a+1)+" : ") for a in range(n1)]
print("\n=============================================================")
perform_index = [float(input("Enter the performance index of candidate "+str(a+1)+" : ")) for a in range(n1)]
print("\n=============================================================")
#apply normalizing function for perform_index column
normalized_index = normalize(perform_index)

#creating the dataframe 
df = pd.DataFrame(normalized_index,name)
df.columns = ['Performance-Index']

print("\n")
print("\n ==========Enter the records for University 2===========")

#section 2: Lets create the dataframe for the second university as the scaling of index is different
#taking the number of records from user as input
n2= int(input("Enter the number of records you want to normalize:"))
print("\n========================================================")

#name of candidate and performance index is taken in input and appended in the list of name and perform_index
name_2 = [input("Enter the name of candidate "+str(a+1)+" : ") for a in range(n1)]
print("\n=============================================================")
perform_index_2 = [float(input("Enter the performance index of candidate "+str(a+1)+" : ")) for a in range(n1)]
print("\n=============================================================")

#apply normalizing function for perform_index column
normalized_index_2 = normalize(perform_index_2)

#creating the dataframe 
df_2 = pd.DataFrame(normalized_index_2,name_2)
df_2.columns = ['Performance-Index']


#section 3: appending the both dataframes:

frames = [df,df_2]
final_df = pd.concat(frames)

#section 4: sorting the records as per performindex column in descending order to give the merit number

result = final_df.sort_values('Performance-Index', ascending=False, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None)

print("===========The Final Merit after Normalization==========")
print(result)

