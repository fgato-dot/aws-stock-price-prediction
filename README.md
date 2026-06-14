
# AWS Stock Price Prediction Pipeline 🚀

An end-to-end machine learning pipeline built on AWS that ingests historical stock market data, trains LSTM neural networks, and delivers 18-month price forecasts through an interactive dashboard.

## 📌 Project Overview

This project follows a cloud-native architecture to predict stock prices for 5 major equities:
**AAPL | MSFT | GOOGL | AMZN | NVDA**

## 🏗️ Architecture

Yahoo Finance API → Amazon S3 (Data Lake)

↓

AWS Glue (ETL + Cataloguing)

↓

Amazon Athena (SQL Queries)

↓

Amazon SageMaker + TensorFlow (LSTM Model)

↓

Tableau Dashboard (Visualisation)

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Data Ingestion | Yahoo Finance API, Python |
| Data Lake | Amazon S3 |
| ETL | AWS Glue, Glue Data Catalog |
| Query | Amazon Athena |
| ML Training | Amazon SageMaker, TensorFlow, LSTM |
| Visualisation | Tableau Public, Matplotlib |
| Automation | AWS Lambda, EventBridge |
| Infrastructure | AWS CLI, boto3 |

## 📊 Results

- 547-day (18-month) price predictions for 5 stocks
- Predictions stored in S3 and visualised in Tableau
- Model retrained automatically with fresh market data

## 🚀 How to Run

1. Configure AWS credentials:
```bash
aws configure
```

2. Install dependencies:
```bash
pip install yfinance boto3 pandas scikit-learn tensorflow matplotlib
```

3. Run the pipeline:
```bash
python Mystockprediction.py
```

## 📁 Project Structure

aws-stock-price-prediction/

│

├── Mystockprediction.py    # Main pipeline script

├── predictions/            # CSV files with stock forecasts

└── README.md

## 👤 Author

**Fernando Ferraz**
Economist & Quantitative Researcher | AWS Cloud & Data Engineer
[GitHub](https://github.com/fgato-dot)
