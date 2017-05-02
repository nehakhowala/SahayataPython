import os
import numpy as np
import pandas as pd
import sys

crimeData = pd.read_csv('SFCrime.csv')

crimeCountByLatLong = crimeData.round({
    'X': 3,
    'Y': 3
}).groupby(['X', 'Y']).size().reset_index(name = 'crimeNumbers')

def takeLatLongReturnCrimeNumbers(A,B):
    return int(crimeCountByLatLong.loc[(crimeCountByLatLong['X'] == A ) & (crimeCountByLatLong['Y'] == B )].crimeNumbers.values)

def classifyArea(crimeCount):
    if crimeCount>1000 :	
        return "Zone 1 extremely unsafe area"
    elif crimeCount>500 :
        return "Zone 2 very high crime rate area"
    elif crimeCount>100 :
        return "Zone 3 moderately high crime rate area"
    elif crimeCount>50 :
        return "Zone 4 low crime rate area"
    else:
        return "Zone 5 safest area"
    