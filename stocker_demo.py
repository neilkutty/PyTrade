#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 20:43:37 2018

@author: https://towardsdatascience.com/stock-prediction-in-python-b66555171a2
"""

#%%
from stocker import Stocker

teradyne = Stocker('TER')

#%%
model, model_data = teradyne.create_prophet_model(days=180)


#%%
teradyne.stock.head()

#%%
teradyne.evaluate_prediction(nshares = 100)

#-------------
#%%

twtr = Stocker('TWTR')
#%%
model, model_data = twtr.create_prophet_model(days=200)

#%%
twtr.stock.tail()
