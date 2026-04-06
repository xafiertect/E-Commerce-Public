# E-Commerce Data Analytics Dashboard
![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-FF4B4B)
![License](https://img.shields.io/badge/License-MIT-green)
![Analysis](https://img.shields.io/badge/Analysis-RFM-orange)

## Project Overview
This repository contains a comprehensive data analysis project focusing on the E-Commerce Public Dataset. The objective is to perform end-to-end data processing—including Data Wrangling and Exploratory Data Analysis (EDA)—to provide actionable insights into sales performance and customer behavior.

## Author
* **Name:** Rizqi Maulidiyah
* **Email:** elkanaxafier@gmail.com
* **Role:** AI Engineer

---

## Project Structure
```text
proyek-ecommerce/
├── notebook.ipynb          # Comprehensive analysis and data processing
├── dashboard.py            # Streamlit interactive dashboard source code
├── requirements.txt        # Technical dependencies
├── README.md               # Project documentation
└── E-Commerce Public/      # Dataset directory (CSV files)
    ├── orders_dataset.csv
    ├── order_items_dataset.csv
    ├── order_payments_dataset.csv
    ├── order_reviews_dataset.csv
    ├── products_dataset.csv
    ├── product_category_name_translation.csv
    └── customers_dataset.csv
---
```

# Installation and Execution

## 1. Environment Setup
Ensure you have placed all the **E-Commerce Public Dataset (.csv files)** inside the `E-Commerce Public/` folder as specified in the directory structure.

---

## 2. Quick Start (Terminal Commands)

Copy and execute the following commands in your terminal to install dependencies and launch the dashboard:
```
```bash
# Install required technical dependencies
pip install -r requirements.txt
```
```bash
# Launch the interactive Streamlit dashboard
streamlit run dashboard.py
```


##  Detailed Analysis

To review the full **Data Wrangling, Cleaning, and Exploratory Data Analysis (EDA)** methodology, run:

```bash
jupyter notebook notebook.ipynb
```

---

# Business Objectives

The analysis is structured to address critical **Key Performance Indicators (KPIs)** through the following inquiries:

##  Revenue Growth Analysis
- Identify product categories with the highest revenue
- Monitor monthly sales trends over time

## Logistics and Satisfaction
- Analyze distribution of customer review scores
- Evaluate impact of shipping lead times on customer satisfaction

---

# Dashboard Features

##  Executive Overview
- High-level summary of business performance
- Total revenue insights
- Monthly trends visualization

##  Product Performance
- Revenue distribution across product categories
- Identify top-performing products

##  Logistics Analysis
- Shipping efficiency insights
- Correlation between delivery time and customer satisfaction

##  RFM Segmentation
- Customer segmentation based on:
  - Recency
  - Frequency
  - Monetary
- Identify high-value customers
- Provide actionable business strategies
