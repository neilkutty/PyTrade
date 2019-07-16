#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 21:18:21 2017

@author: NNK
@title: Analysis of Investment Vehicles in Python
"""



#%%
#%matplotlib inline

import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
#import pandas_datareader.data as web
#import datetime
import seaborn as sb
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
#import sklearn.linear_model as lm
#from sklearn.model_selection import train_test_split
#import sklearn as sk
sb.set_style("whitegrid")
plotly.tools.set_credentials_file(username='sampsonsimpson', 
                                  api_key='GBUBRUGNCAHxJ5uZdAs3')

import fix_yahoo_finance as yf

#%%
TWTR = yf.download('TWTR','2016-01-01','2018-09-01')
TSM = yf.download('TSM','2016-01-01','2018-09-01')
NVDA = yf.download('NVDA','2016-01-01','2018-09-01')


##%% Get price data
#
#start = datetime.datetime(2014,1,1)
#end = datetime.datetime.today()
#
##%%
#NVDA = web.DataReader("NVDA", 'google', start, end)
#TSM = web.DataReader("TSM", 'google', start, end)
#TWTR = web.DataReader("TWTR", 'google', start, end)
#%% OHLC Plotting in Plotly



trace = go.Ohlc(x=TWTR.index,
                open=TWTR.Open,
                high=TWTR.High,
                low=TWTR.Low,
                close=TWTR.Close)
data = [trace]
py.plot(data, filename='simple_ohlc')


#%%

trace = go.Ohlc(x=TWTR.index,
                open=TWTR.Open,
                high=TWTR.High,
                low=TWTR.Low,
                close=TWTR.Close)
data = [trace]
py.plot(data, filename='simple_ohlc')

#%%  Data Manipulation

#  LAG Variables

NVDA = pd.DataFrame(NVDA)
NVDA['Close1'] = NVDA.Close.diff(periods = 1)

# Transformations

for i in range(0,len(NVDA)):
    j = NVDA['Close'][i] - NVDA['Close'][i - 1]
    break

# subset
NVDA[(NVDA.index > '2017-11-01')][['Open','Close']].plot()





#%%
TSM[(TSM.index > '2017-08-01')][['Open','Close']].plot()


#%%
#

#%%  Plot of TSM

#  Look into functionalization of plotly to be able to switch between equities 
# for same chart design.    


layout = go.Layout(
        title='Taiwan Semiconductor Manuf. (TSM) Open vs. Close',
        
        updatemenus=list([
        dict(x=-0.1, y=0.7,
             yanchor='middle',
             bgcolor='c7c7c7',
             borderwidth=2,
             bordercolor='#ffd6dc'),
             ]),
        xaxis=dict(
                title='Open (TSM)'
                ),
        yaxis=dict(
                title='Close (TSM)'
                )
             
             )

d = [
     go.Scatter(
             x=TSM[(TSM.index > '2017-09-01')].Open.tolist(),
             y=TSM[(TSM.index > '2017-09-01')].Close.tolist(),
             mode = "markers",
             marker= dict(size= 14,
                    line= dict(width=1),
                    color= TSM[(TSM.index > '2017-09-01')].Volume.tolist(),
                    opacity= 0.7
                   ))]


fig = go.Figure(data=d, layout=layout)

py.plot(fig, filename='TSM-Open-Close_scatter')

#%%

