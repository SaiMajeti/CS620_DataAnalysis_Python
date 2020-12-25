"""
CS 620
HW2-b
@author: Sai Hymavathi Majeti
"""
import pandas as pd
import glob
import gc
import os
import numpy as np


#part I
path = r'yob-names' # use your path   
yobPath = 'yob-names.csv' 
all_files = glob.glob(yobPath + "/*.txt")

files = [os.path.join(path, filename) for filename in os.listdir(path)] #read each file and add to list
data = pd.DataFrame() # initialize a dataframe

for file in files:
    df = pd.read_csv(file, names=['name', 'gender', 'count']) # read in each .txt to .csv to df
    df['year'] = file # add a column with the filename
    data = data.append(df) # add all small dfs to big df 

data['year'] = data['year'].map(lambda x: x.strip('yob-names\yob').strip('.txt')) 
# get rid of yob(filename on right) and (filename on left).txt and just keep the year from filename.
neworder = ['year','name','gender','count']
data=data.reindex(columns = neworder) #re-order columns per given requirement
data['year'] = pd.to_numeric(data['year'], errors='coerce') #convert year to numeric values

data.to_csv(yobPath, index=False) #append data to csv # output: total: [1957046 rows x 4 columns]

# Part II
# a)	What is the most popular boys name in year 1980?
given_gender = "M" #give gender here
given_year = 1980 #give year here

#Subsetting data for given year and gender
Boys_year = data[(data.year == given_year) & (data.gender == given_gender)]
MPBN_year = Boys_year.nlargest(1, ['count']) 
# most popular name would be the ne with highest-count(frequency) in that year.
# output: 1980  Michael  M  68696 #MPBN- most-popular-boys-name 

# b)	How many girls were born between 1990 and 2000?
given_gender = "F" #give gender
min_year = 1990 #give minimum year
max_year = 2000 #give maximum year

#subsetting data based on given years and gender
num_gender = data[(data.gender == given_gender) & (data.year >= min_year) & (data.year <= max_year)] #result: [176854 rows x 4 columns]

tot_gender = num_gender['count'].sum() # 19816748 girls born between 1990 & 2000

#c)	How many female Benjamin’s are alive today (year 2020)? 
lifeExpectancy = pd.read_csv("D:/Courses\DS with Py/HW2/hw2-resources/hw2-wrangling/cdc-life-expectancy.csv")

till_date = 2020 #input the till_date to be considered
given_year = 1950 #input year here
given_gender = "F" #input gender here
given_person_name = "Benjamin" #input name here

LE_year = lifeExpectancy[(lifeExpectancy.year >= given_year)] # subsetting/taking only values after given_year

min_LE_gender = min(set(LE_year[given_gender])) #minimum life_expectancy of the given gender

#subsetting/taking only female benjis born on or after 1950.
gender_name = data[(data.name == given_person_name) & (data.gender == given_gender) & (data.year >= given_year)]  

# number of given-person alive today 
#born year + minimum_life_expectancy >= given till_date => they are alive today. #assuming 2020 people are still alive - since we only know the year, not the exact date.
#vice-versa --> if < given till_date => they expired.

person_alive = gender_name[(gender_name.year + min_LE_gender >= till_date)] 
# result for Benjamin: [69 rows x 4 columns]

tot_person_alive = person_alive['count'].sum() 
# total count - result for Benjamin: 2149



