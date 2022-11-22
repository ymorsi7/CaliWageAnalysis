
"""
Time Series Analysis for:
Alameda County, Industry: Police Protection, NAICS: 92212, Ownership: State Government
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

parser = argparse.ArgumentParser()
parser.add_argument('--generate_series', help="To generate the pandas series for employment", action='store_true')
parser.add_argument('--gen_plot_series', help="To generate plots for time series and its autocorrelation", action='store_true')
parser.add_argument('--adf_test', help="Augmented Dickey-Fuller Test to check stationarity", action='store_true')
parser.add_argument('--mk_test', help="Finding trend in the time series using Mann-Kendall Trend Test", action='store_true')
parser.add_argument('--seasonality_test', help="Finding Seasonality", action='store_true')
parser.add_argument('--ARIMA', help="Time series prediction", action='store_true')

args = parser.parse_args()

filename = '92212_Alameda_FederalGovt.csv'


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
    plt.title('Employment rates in Alameda County, \nIndustry = Police Protection, Ownership = Federal Government')
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

if args.ARIMA:
    """Time Series Prediction
    """    

    with open('emp_series',"rb") as f:
      emp_series = pickle.load(f)

    # Dividing the data into train(66%) and test(33%) sets
    size = int(0.66 * len(emp_series))
    train, test = emp_series.values[0:size], emp_series.values[size:len(emp_series)]

    history = list(train)
    predictions = []

    for t in range(len(test)):
        model = ARIMA(history, order=(25,1,0))
        model_fit = model.fit()
        output = model_fit.forecast()
        yhat = output[0]
        predictions.append(yhat)
        obs = test[t]
        history.append(obs)
        print('predicted=%f, expected=%f' % (yhat, obs))
    
    rmse = sqrt(mean_squared_error(test, predictions))
    print('Test RMSE: %.3f' %rmse)

    plt.plot(test, label="Test")
    plt.plot(predictions, color='red',label="Predictions")
    plt.legend(loc="upper left")
    plt.title('Predictions versus Test data')
    plt.ylabel('Employment')
    plt.xlabel('Time (in months)')
    plt.show()

    s1 = pd.Series(test)
    s2 = pd.Series(predictions)
    print(s1.corr(s2, method='pearson'))

  

