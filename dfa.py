# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 23:20:25 2023

@author: omar
"""

# Calculating DFA time series functioin from a csv file
# by f6m

# shell compilation
# python dfa.py
# chmod +x bitvol
# ./bitvol

# Reference and references therein
# https://en.wikipedia.org/wiki/Detrended_fluctuation_analysis

import pandas as pd #Pandas or csv library reads a csv file
import matplotlib.pyplot as plt #plot
import numpy as np
from scipy import optimize

#Function model (usually a rect) to fit
def funcmodel(x, a, b):
    y = a*x + b
    return y

#Function
#Entries: file with close prices (thinking in oil/bitcoin), time interval or horizon length
#Outputs: Volatility data series

def dfa(p,L):
    # calculate first L volatility for serie entries in array range 0,...,L-1
    r1=0
    r2=L
    Fn=[]
    v=[]
    l=len(p)
    rest = l%L
    while r2 < l: #jumps of length L in array p
        x=np.linspace(r1,r2,num=L+1) #0,...,l 
        y=p[r1:r2+1] #price[0],...,price[l]
        abmodel, _ = optimize.curve_fit(funcmodel, xdata = x, ydata = y)
        a,b = abmodel[0],abmodel[1]
        print(r1,r2)
        for j in range(r1,r2):
            v.append((p[j]-funcmodel(j,a,b))**2)
        r1=r2
        if(rest==0):
            r2=r2+L
        if(rest!=0 and r2 < l-rest):
            r2=r2+L
        if(r2+rest==l):
            r2=r2+rest
    Fn.append((sum(v)/l)**(0.5))
    return Fn

# Read in the price data from csv
df = pd.read_csv('Bitcoin4H2010-2023.csv')
print(df.head(10))
mean_close_price = df['close'].mean() #close price column mean 
print(mean_close_price)

closeb = df['close'] #close price to array
length = len(closeb)-1
cumulativesum = [] #Cumulative sum for time serie
returnprice = [] #return price serie
logprice = [] #log price serie
vol=[]
print(length-1,closeb[0],closeb[27839])

for i in range(0,length):
    returnprice.append((closeb[i+1]-closeb[i])/closeb[i])
    logprice.append(np.log(closeb[i+1]/closeb[i]))

for i in range(0,length):
    cumulativesum.append(closeb[i]-mean_close_price)

## optimize with a rect
#print(cumulativesum)
#print(len(cumulativesum))
dfaa=dfa(cumulativesum,700)   
print(dfaa)
#np.savetxt("cp-dfa-700csv", np.row_stack(dfaa), delimiter=",", fmt='%s')



