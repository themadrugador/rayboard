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

s = fred.get_series('SP500', observation_start='1/31/2014')
s.tail()