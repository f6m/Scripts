# Calculating volatility (which type?) from a csv file
# by f6m

# shell compilation
# python bitvol.py
# chmod +x bitvol
# ./bitvol

# GUI proyect
# https://github.com/cryptarbitrage-code/historical-volatility-calculations/blob/main/main.py
# Volatily function idea
# https://github.com/cryptarbitrage-code/historical-volatility-calculations/blob/main/volatility_calculations.py

import pandas as pd #Pandas or csv library reads a csv file
import matplotlib.pyplot as plt #plot
import numpy as np

#Function
#Entries: file with close prices (thinking in oil/bitcoin), time interval or horizon length
#Outputs: Volatility data series

def volatility(p,L):
    # calculate first L volatility for serie entries in array range 0,...,L-1
    r1=0
    r2=L
    vt=[]
    v=[]
    l=len(p)
    rest = l%L
    for i in range(0,l,L): #jumps of length L in array p
        ml=sum(p[r1:r2])/L
        print(r1,r2)
        for j in range(r1,r2):
            vt.append((p[j]-ml)**2)
        v.append((sum(vt)/L)**(1/2))
        r1=r2
        if(rest==0):
            r2=r2+L
        if(rest!=0 and r2 < l-rest):
            r2=r2+L
        if(r2+rest==l):
            r2=r2+rest
    return v

# Read in the price data from csv
df = pd.read_csv('Bitcoin4H2010-2023.csv')
print(df.head(10))
mean_close_price = df['close'].mean() #close price column mean 
print(mean_close_price)

closeb = df['close'] #close price to array
length = len(closeb)-1
returnprice = [] #return price serie
logprice = [] #log price serie
vol=[]
print(length-1,closeb[0],closeb[27839])

for i in range(0,length):
    returnprice.append((closeb[i+1]-closeb[i])/closeb[i])
    logprice.append(np.log(closeb[i+1]/closeb[i]))

vol=volatility(returnprice,700)   

np.savetxt("rp-volrp-700csv", np.row_stack(vol), delimiter=",", fmt='%s')


#print(returnprice.tail(10))

#https://medium.datadriveninvestor.com/market-volatility-in-python-46f250b070a9

#df['Date'] = pd.to_datetime(df['Date'])  # change text date to pandas datetime
#df = calculate_historical_vols(df, sessions_in_year)

