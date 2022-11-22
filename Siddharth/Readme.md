<a name="readme-top"></a>

## Time Series Analysis of the employment data

This part of the project has been contributed by Siddharth Satyam. 
The data files are uploaded as "92212_Alameda_FederalGovt.csv", "92212_Alameda_StateGovt.csv" and "44422_Alameda_Private.csv", which were extracted from the main data using the SQL query in queries.sql

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#modules-required">Modules required</a></li>
    <li><a href="#code-structure">Code Structure</a></li>
  </ol>
</details>



<!-- Modules required -->
## Modules required

```sh
  pip install pymannkendall
```
```sh
  pip install kats==0.1 ax-platform==0.2.3 statsmodels==0.12.2
```

* Matplotlib pyplot
* csv
* pandas
* datetime
* statsmodels.tsa.arima.model
* math
* sklearn.metrics
* statsmodels.tsa.stattools
* kats.consts
* kats.utils.decomposition
* argparse
* pymannkendall

<!-- Code Structure -->
## Code Structure

Time Series Analysis has been done for 2 industries:
* Alameda County, Industry: Police Protection, NAICS: 92212, Ownership: State Government
* Alameda County, Industry: Police Protection, NAICS: 92212, Ownership: Federal Government

There are 2 .py code files "run_analysis_state.py" and "run_analysis_state.py" for the 2 industries of Police Protection. 
In each file we have:
* Plotting of Time Series Data
* Autocorrelation Plot for the time series
* Augmented Dickey-Fuller Test to check stationarity
* Finding trend in the time series using Mann-Kendall Trend Test
* Finding Seasonality
* Time series prediction using ARIMA

The instructions for running the code for "run_analysis_state.py" are as follows:

Firstly, generate and save the pandas time series from the csv files using:
 
```sh
  python run_analysis_state.py --generate_series
```

Now the other parts of the code can be run in any order.
To plot the time series and autocorrelation plot:

```sh
  python run_analysis_state.py --gen_plot_series
```

To perform ADF test for stationarity:

```sh
  python run_analysis_state.py --adf_test
```

To perform MK test for checking trend in the data:

```sh
  python run_analysis_state.py --mk_test
```

To perform seasonality test:

```sh
  python run_analysis_state.py --seasonality_test
```

To perform time series prediction using ARIMA:

```sh
  python run_analysis_state.py --ARIMA
```

Similarly, we can perform all the tests for the second code by replacing 'state' with 'federal'.




<p align="right">(<a href="#readme-top">back to top</a>)</p>

