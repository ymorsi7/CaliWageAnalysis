
"""
Time Series Analysis for:
Alameda County, Industry: Nursery, Garden & Farm Supply Stores, NAICS: 44422, Ownership: Private
"""


import matplotlib.pyplot as plt
import csv
import pandas as pd
from datetime import datetime
from pandas.plotting import autocorrelation_plot
from statsmodels.tsa.arima.model import ARIMA
from math import sqrt
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.stattools import adfuller
import argparse
import pickle
import pymannkendall as mk
from kats.consts import TimeSeriesData
from kats.utils.decomposition import TimeSeriesDecomposition
from kats.detectors.seasonality import FFTDetector
from kats.detectors.seasonality import ACFDetector

parser = argparse.ArgumentParser()
parser.add_argument('--generate_series', help="To generate the pandas series for employment", action='store_true')
parser.add_argument('--gen_plot_series', help="To generate plots for time series and its autocorrelation", action='store_true')
parser.add_argument('--adf_test', help="Augmented Dickey-Fuller Test to check stationarity", action='store_true')
parser.add_argument('--mk_test', help="Finding trend in the time series using Mann-Kendall Trend Test", action='store_true')
parser.add_argument('--seasonality_test', help="Finding Seasonality", action='store_true')

args = parser.parse_args()

filename = '44422_Alameda_Private.csv'


if args.generate_series:

    emp = []

    with open(filename, mode ='r') as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
                emp += [int(x) for x in lines[2:5]]

    time = pd.date_range(start='2004',end='2022',periods=len(emp))
    emp_series = pd.Series(emp,index=time)

    print('Time Series for employment generated')

    #Save the time series thorugh pickle dump
    with open('emp_series',"wb") as f:
      pickle.dump(emp_series,f)

if args.gen_plot_series:

    with open('emp_series',"rb") as f:
      emp_series = pickle.load(f)
    
    emp_series.plot()
    plt.title('Employment rates in Alameda County, \nIndustry = Nursery, Garden & Farm Supply Stores, Ownership = Private')
    plt.ylabel('Employment')
    plt.show()

    """
    We will find the correlation of the time series with itself at different values of time lag. 
    This will provide us information about how many time steps to use for ARIMA time series prediction.
    """
    autocorrelation_plot(emp_series)
    plt.show()

if args.adf_test:

    with open('emp_series',"rb") as f:
      emp_series = pickle.load(f)

    adfuller(emp_series)

if args.mk_test:

    with open('emp_series',"rb") as f:
      emp_series = pickle.load(f)
      
    mk.original_test(emp_series)

if args.seasonality_test:
    """We decompose the time series into different components: Trend, seasonality, and residual components
    """    

    with open('emp_series',"rb") as f:
      emp_series = pickle.load(f)

    df = emp_series.rename("value")
    df = df.to_frame()
    df.reset_index(inplace=True)
    df = df.rename(columns={"index": "time"})
    ts = TimeSeriesData(df)

    decomposer = TimeSeriesDecomposition(ts, decomposition="additive")
    results = decomposer.decomposer()
    fig = decomposer.plot()    

    fft_detector = FFTDetector(ts)
    print(fft_detector.detector())

    detector = ACFDetector(ts)
    detector.detector(diff=1, alpha = 0.01)
    detector.plot()

