"""
CS 620
HW2-a
@author: Sai Hymavathi Majeti
"""


"""Given two list of numbers that are already sorted, 
 return a single merged list in sorted order.
"""  
def merge(sortedListA, sortedListB):
    #Complete this part
    sortedList = sorted(sortedListA + sortedListB)
    return sortedList

"""Given a list of numbers in random order, return the summary statistics 
that includes the max, min, mean, population standard deviation, median,
75 percentile, and 25 percentile.
"""    
def summaryStatistics(listOfNums):
    #Complete this part. 
    #You can decide to return the following statistics either in a sequence 
    #type (i.e., list, tuple), or a key-value pair (i.e., dictionary)
    import statistics as st
    import numpy as np
    maxVal = max(listOfNums)
    minVal = min(listOfNums)
    meanVal = round(st.mean(listOfNums), 2)
    stdev = round(st.stdev(listOfNums), 2) 
    median = st.median(listOfNums)
    perc75 = np.percentile(listOfNums, 75)
    perc25 = np.percentile(listOfNums, 25)
    return {'max': maxVal, 
            'min': minVal, 
            'mean': meanVal, 
            'stdev': stdev,
            'median': median,
            'perc75': perc75,
            'perc25': perc25}

"""Given a list of real numbers in any range, scale them to be 
between 0 and 1 (inclusive). For each number x in the list, the new number 
is computed with the formula ((x - min)/(max - min)) where max is the 
maximum value of the original list and min is the minimum value of the list. 
"""	
def minMax(listOfNums): 
    #complete this part
    minVal = min(listOfNums)
    maxVal = max(listOfNums)
    #formula = ((x - minVal)/(maxVal - minVal))
    #newList = [formula for x in listOfNums]
    newList = [round(((x - minVal)/(maxVal - minVal)),2) for x in listOfNums]
    return newList