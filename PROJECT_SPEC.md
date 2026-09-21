# Earnings Intelligence Radar — Project Specification

## 1. Project Overview

Earnings Intelligence Radar is a near-real-time financial intelligence platform designed to estimate upcoming company earnings performance using free and publicly available financial, economic, industry, and alternative-data sources.

The project is designed as a research-grade financial data and analytics product rather than a simple stock-price prediction model.

## 2. Core Objective

The platform will attempt to answer four questions:

1. What is the company's expected upcoming revenue performance?
2. Why is the model making that prediction?
3. How reliable has the model been historically?
4. Which publicly available data sources provide genuine incremental predictive information?

## 3. Core Outputs

The platform should provide:

- Revenue nowcast
- Prediction range
- Prediction distribution
- Probability of beat / meet / miss
- Driver contributions
- Historical model performance
- Probability calibration
- Forecast evolution over time
- Data-source incremental value
- Data freshness
- Data provenance
- Data quality indicators
- Model agreement
- Model limitations and risks

## 4. Data Cost Constraint

The project must use free and publicly available data sources.

Target data sources may include:

- SEC XBRL
- FRED
- ALFRED
- Google Trends
- U.S. Census data
- NOAA
- Other relevant free public datasets where appropriate

Paid financial-data APIs and proprietary alternative-data subscriptions are outside the core project scope.

## 5. Near-Real-Time Requirement

The platform should provide near-real-time intelligence based on the latest available public data.

It must not claim true real-time coverage when the underlying public source has publication delays.

Each important data source should have:

- Last available observation
- Publication/update information where available
- Retrieval timestamp
- Data freshness status

## 6. Point-in-Time Requirement

The forecasting system must avoid look-ahead bias.

Historical predictions should use only information that would have been available at the relevant point in time.

Where revised macroeconomic data are involved, historical vintages should be considered using ALFRED or equivalent point-in-time methodology where feasible.

## 7. Forecasting Approach

The system should begin with simple baseline models before introducing more complex models.

Potential models include:

- Historical/seasonal baseline
- Ridge regression
- Lasso regression
- Gradient boosting
- Ensemble approaches where justified

Models should be evaluated using chronological walk-forward validation rather than random train/test splitting.

## 8. Uncertainty and Probability

The platform should not provide only a single point estimate.

Where statistically justified, it should provide:

- Expected revenue
- Prediction interval/range
- Probability distribution
- Beat probability
- Meet probability
- Miss probability

Probabilities must be calibrated using historical outcomes rather than arbitrarily assigned.

## 9. Alternative-Data Research

The project should test whether additional publicly available information improves earnings forecasts.

Possible feature groups include:

- Historical financial performance
- Macro indicators
- Search-interest data
- Industry indicators
- Retail/consumer indicators
- Other relevant public alternative-data proxies

The project should compare incremental predictive value rather than assuming that every data source is useful.

## 10. Validation

Validation should include, where appropriate:

- Walk-forward validation
- Out-of-sample evaluation
- Forecast error analysis
- Model comparison
- Probability calibration
- Brier score or equivalent probability metric
- Information-coefficient analysis where appropriate
- Multiple-testing controls where appropriate
- Signal decay analysis

Negative or weak findings should be reported honestly rather than hidden.

## 11. Product Features

The final product should aim to include:

### Company Selection

Allow the user to select a supported company.

### Earnings Nowcast

Display the current model estimate for upcoming revenue performance.

### Driver Analysis

Explain the major factors contributing to the forecast.

### Forecast Evolution

Show how the forecast changed as new information became available.

### What Changed?

Compare the current forecast with the previous forecast and identify major drivers of the change.

### Historical Replay

Allow users to examine what the model would have predicted before previous earnings announcements.

### Data Source Analysis

Show how forecast performance changes when different data sources are added or removed.

### Data Freshness

Show whether important inputs are current, delayed, stale, or missing.

### Model Agreement

Show the estimates produced by different models and whether they agree.

### Limitations

Clearly communicate what the model does not know and what could cause the prediction to fail.

## 12. Product Positioning

The platform is intended to demonstrate capabilities relevant to:

- Financial data analysis
- Equity research
- Quantitative research
- Financial data science
- Market intelligence
- Alternative-data research
- Financial technology
- Investment research platforms

## 13. Non-Goals

The project is not intended to:

- Provide guaranteed earnings predictions
- Provide investment advice
- Generate unsupported BUY/SELL recommendations
- Use paid proprietary datasets as a requirement
- Hide failed signals
- Present uncalibrated probabilities as facts
- Use future information in historical forecasts

## 14. Technical Direction

Expected technologies may include:

- Python
- pandas
- NumPy
- statsmodels
- scikit-learn
- Plotly
- Streamlit

The exact implementation should be determined during the architecture stage.

## 15. Project Philosophy

The objective is not to create a model that appears impressive.

The objective is to create a defensible financial intelligence product in which:

Data → Features → Forecast → Probability → Explanation → Validation → Intelligence

Every important claim should be supported by data and appropriate validation.

## 16. Current Status

Project setup has begun.

GitHub repository has been created.

The next major stage is architecture and project scaffolding.
