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