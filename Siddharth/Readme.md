<a name="readme-top"></a>

This part of the project has been contributed by Siddharth Satyam. 
The data files are uploaded as "92212_Alameda_FederalGovt.csv" and "92212_Alameda_StateGovt.csv", which were extracted from the main data using the SQL query in 
queries.sql

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#modules-required">Modules required</a></li>
    <li><a href="#code-structure">Code Structure</a></li>
    <li><a href="#Theory">Theory</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
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

<!-- Code Structure -->
## Code Structure

Time Series Analysis has been done for 2 industries:
* Alameda County, Industry: Police Protection, NAICS: 92212, Ownership: State Government
* Alameda County, Industry: Police Protection, NAICS: 92212, Ownership: Federal Government

The code is structure into 2 halves for the 2 industries. In each half we have:
* Plotting of Time Series Data
* Autocorrelation Plot for the time series
* Augmented Dickey-Fuller Test to check stationarity
* Finding trend in the time series using Mann-Kendall Trend Test
* Finding Seasonality
* Time series prediction using ARIMA


<p align="right">(<a href="#readme-top">back to top</a>)</p>

