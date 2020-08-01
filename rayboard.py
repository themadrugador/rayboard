# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 12:59:06 2020

@author: johnc
"""

#FRED API
#7cf9fa4cb90133896f70986c11b6d454

#%% Import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import quandl
from fredapi import Fred
fred = Fred()


quandl.ApiConfig.api_key = "nU9zmvaiSyzDh7XoyLbj"

api_key_file = '7cf9fa4cb90133896f70986c11b6d454'
#%%
'''
url = 'https://api.stlouisfed.org/fred/category?category_id=125&api_key=' + api_key + '&file_type=json'
r = requests.get(url)

mydata = quandl.get("FRED/GDP")
'''
#%%
df = pd.DataFrame()


def get_FRED(name, series, start_date):
    print(name + ' ' + series)
    df_i = pd.DataFrame()
    s = fred.get_series(series, observation_start = start_date)
    data = {'Metric': name, 'Source': 'FRED ' + series, 'Data':[s]}
    df_i = pd.DataFrame(data)
    return df_i

FRED_metrics = {'CPI': 'CPIAUCSL', 
                'Unemployment': 'UNRATE',
                'PCE': 'PCE',
                'Personal Income': 'PI',
                'Personal Saving Rate': 'PSAVERT',
                'M2': 'M2',
                'FED Assets': 'WALCL',
                'Federal Debt': 'MVGFD027MNFRBDAL',
                'Federal Deficit': 'MTSDS133FMS',
                'US Dollar': 'DTWEXAFEGS',
                '10yr Treasury': 'DGS10'}

start_date = '1/1/2019'
for metric in FRED_metrics:
    df = df.append(get_FRED(metric,FRED_metrics[metric],start_date))
df.reset_index(inplace = True, drop = True)

#%% Plot metrics
for i in range(len(df)):
    plt.figure()
    df.loc[i,'Data'].plot()
    plt.title(df.loc[i,'Metric'])
    