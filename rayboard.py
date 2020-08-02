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
                'PCE Price Index': 'PCEPI',
                'PCE Core Price Index': 'PCEPILFE',
                'Personal Income': 'PI',
                'Personal Saving Rate': 'PSAVERT',
                'M2': 'M2',
                'FED Assets': 'WALCL',
                'Federal Debt': 'MVGFD027MNFRBDAL',
                'Federal Deficit': 'MTSDS133FMS',
                'US Dollar': 'DTWEXAFEGS',
                '10yr Treasury': 'DGS10',
                'Home Prices': 'CSUSHPISA',
                'CPI Shelter (34%)': 'CUSR0000SAH1',
                'CPI Commodities Less Food & Energy (20%)': 'CUSR0000SACL1E',
                'CPI Medical Care Services (7%)': 'CUSR0000SAM2',
                'CPI Education (6%)': 'CPIEDUSL',
                'CPI Transportation Services (5%)': 'CUSR0000SAS4',
                'CPI Recreation (4%)': 'CPIRECSL',
                'CPI Food (14%)': 'CPIUFDSL',
                'CPI Energy (6%)': 'CPIENGSL'}

start_date = '1/1/2019'
for metric in FRED_metrics:
    df = df.append(get_FRED(metric,FRED_metrics[metric],start_date))
df.reset_index(inplace = True, drop = True)

#%% Plot metrics
for i in range(len(df)):
    plt.figure()
    df.loc[i,'Data'].plot()
    plt.title(df.loc[i,'Metric'])

#%%
'''
OBSERVATIONS:

MONEY FLOW
-Unemployment is up due to shutdowns
-Incomes are up due to stimulus
-Spending is down (likely due to shutdowns), and therefore savings are up
-Conclusion: Federal stimulus is likely flowing directly into asset prices, though not the economy

INFLATION / DOLLAR VALUATION
-Prices are down due to spending cuts in certain sectors.
-FED purchasing is flat after initial spike, which indicates that the market is naturally bidding down interest rates
-US Gov is running large deficit--need to connect to debt issuance (treasury supply)
-FED may eventually need to begin purchasing more treasuries to keep rates low
-Need to better figure out how to represent value of the dollar

IMPLICATIONS
-Asset prices: valuations will continue rising with fiscal stimulus due to saving effect

INFLATION RISK:
-FED risk: if inflation picks up before employment, FED may have to consider pulling back on stimulus
-FED risk: if demand for USD / treasuries drops, FED will have to buy more bonds increasing inflation risk

DEFLATION RISK:
-spending is entirely dependent on govt stimulus; pulling back on stimulus would be very deflationary
'''