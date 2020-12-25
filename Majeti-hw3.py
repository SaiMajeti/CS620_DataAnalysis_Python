"""
CS 620
HW2-a
@author: Sai Hymavathi Majeti
"""

import numpy as np
import pandas as pd
import os
from bs4 import BeautifulSoup
import xml.dom.minidom as md 


# Read the .csv file into a DataFrame called “csv_data” 
csv_data = pd.read_csv('SP500_ind.csv', sep= ',', engine= 'python')

#converting date column to datetime.
csv_data['Date'] = pd.to_datetime(csv_data['Date'], format='%Y%m%d')

#print(csv_data.head())

# read .xml file to a dictionary called “xml_dict” in your python module.
with open('SP500_symbols.xml', 'r') as f:
    data = f.read()
xml_dict = BeautifulSoup(data, "xml")
#print(xml_dict.prettify())

# Generate a list of unique symbol values from the csv_data and name the list “ticker” using unique() method.
ticker = csv_data.Symbol.unique()

"""This function takes in the xml_dict and a
Symbol (ticker). Return the name of the ticker
Ex: for ticker “A”, the function returns Agilent Technologies Inc
"""
def ticker_find(xml_dict, ticker):
        c_name = xml_dict.find('symbol', {'ticker': item})
        if c_name == None:
            company_name = "No data in SP500"  
        else:
            company = c_name.get('name')
            company_name = company
        return company_name

"""This function takes in the csv_data and a ticker.
Return the average opening price for the stock as a float.
"""
def calc_avg_open(csv_data, ticker):
            avg_open = csv_data.loc[csv_data['Symbol'].eq(item),'Open'].mean().round(2)
            #avg_open = csv_data.groupby('Symbol')['Open'].mean()
            return avg_open

"""This function takes in the csv_data and a ticker. Return the volume weighted average
price (VWAP) of the stock. In order to do this, ...
(hint: average price for each day = (high + low + close)/3)"""
def vwap(csv_data, ticker):
    #first find the average price of the stock on each day
    #Then, multiply that price with the volume on that day.
    csv_data['avg_day'] = (((csv_data['High']+csv_data['Low']+csv_data['Close'])/3)*csv_data['Volume']).round(2)
    #Take the sum of these values
    wv = csv_data.loc[csv_data['Symbol'].eq(item), 'avg_day'].sum()
    #Finally, divide that value by the sum of all the volumes'''
    volumes = csv_data.loc[csv_data['Symbol'].eq(item),'Volume'].sum()
    vws = (wv/volumes).round(2)
    return vws

for item in ticker: 
    name = ticker_find(xml_dict, ticker)
    avg = calc_avg_open(csv_data, ticker)
    vwap_value = vwap(csv_data, ticker)
    print(name + ' ' + str(avg) + ' ' + str(vwap_value))
