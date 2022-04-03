#importing the library
import pandas as pd

#reading the dataset
data = pd.read_csv ('https://raw.githubusercontent.com/darshanjoshi16/DataMiningPractical/main/Extra%20Practical%202/Q2-tennis.csv')
print (data)

print("==================================================\n")

#calculating the priori probabilities
prior = data.groupby('Play').size().div(len(data)) 
print(prior)

print("==================================================\n")

#Likelihood is generated for each of the features of the dataset. 
#Basically  likelihood is probability of finding each feature given class label.
likelihood = {}
likelihood['Outlook'] = data.groupby(['Play', 'Outlook']).size().div(len(data)).div(prior)
likelihood['Temp.'] = data.groupby(['Play', 'Temp.']).size().div(len(data)).div(prior)
likelihood['Humidity'] = data.groupby(['Play', 'Humidity']).size().div(len(data)).div(prior)
likelihood['Windy'] = data.groupby(['Play', 'Windy']).size().div(len(data)).div(prior)

print (likelihood)

print("==================================================\n")

#calculating the posterior probabilites

# Probability that the person will play
p_yes = likelihood['Outlook']['sunny']['yes'] * likelihood['Temp.']['cool']['yes'] * \
        likelihood['Humidity']['high']['yes'] * likelihood['Windy']['false']['yes'] \
        * prior['yes']

# Probability that the person will NOT play
p_no = likelihood['Outlook']['sunny']['no'] * likelihood['Temp.']['cool']['no'] * \
       likelihood['Humidity']['high']['no'] * likelihood['Windy']['false']['no'] \
       * prior['no']

print ('Probability of Playing : ', p_yes)
print ('Probability of not Playing :  ', p_no)