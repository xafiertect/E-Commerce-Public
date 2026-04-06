<<<<<<< HEAD
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
=======
# 🛒 E-Commerce Public Data Analysis Dashboard

<p align="center">
  <b>Interactive Data Analytics Dashboard using Streamlit</b><br>
  Transforming raw data into actionable business insights 🚀
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-red?style=for-the-badge&logo=streamlit">
  <img src="https://img.shields.io/badge/Data%20Analysis-EDA-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge">
</p>

---

## 📌 Project Overview

This project presents a comprehensive analysis of an e-commerce dataset through an interactive dashboard built with Streamlit.

It focuses on extracting meaningful insights from raw transactional data, enabling better decision-making in areas such as sales performance, customer satisfaction, and customer segmentation.

---

## 👤 Author

* **Rizqi Maulidiyah**
* 📧 [elkanaxafier@gmail.com](mailto:elkanaxafier@gmail.com)

---

## 🎯 Objectives

✔ Identify top-performing product categories
✔ Analyze customer satisfaction based on delivery performance
✔ Understand customer behavior using RFM segmentation
✔ Visualize business insights in an interactive dashboard

---

## 🧠 Business Questions

### 1️⃣ Product Performance

* Which product categories generate the highest revenue?
* How does sales performance evolve over time?

### 2️⃣ Customer Satisfaction

* What is the distribution of review scores?
* Does delivery time affect customer satisfaction?

---

## 🏗️ Project Structure

```
E-Commerce-Public/
│
├── 📂 dashboard/
│   └── dashboard.py
│
├── 📂 data/
│   ├── orders_dataset.csv
│   ├── order_items_dataset.csv
│   ├── order_payments_dataset.csv
│   ├── order_reviews_dataset.csv
│   ├── products_dataset.csv
│   ├── product_category_name_translation.csv
│   └── customers_dataset.csv
│
├── 📓 notebook.ipynb
├── 📄 requirements.txt
├── 📄 README.md
└── 🔗 url.txt
>>>>>>> a65296d (progress update)
```

# Installation and Execution

## 1. Environment Setup
Ensure you have placed all the **E-Commerce Public Dataset (.csv files)** inside the `E-Commerce Public/` folder as specified in the directory structure.

---

<<<<<<< HEAD
## 2. Quick Start (Terminal Commands)

Copy and execute the following commands in your terminal to install dependencies and launch the dashboard:
=======
## ⚙️ Installation
>>>>>>> a65296d (progress update)

```bash
# Install required technical dependencies
pip install -r requirements.txt
```
```bash
# Launch the interactive Streamlit dashboard
streamlit run dashboard.py
```

<<<<<<< HEAD

##  Detailed Analysis

To review the full **Data Wrangling, Cleaning, and Exploratory Data Analysis (EDA)** methodology, run:

=======
---

## ▶️ How to Run

### 🔹 Run Notebook (EDA)

>>>>>>> a65296d (progress update)
```bash
jupyter notebook notebook.ipynb
```

<<<<<<< HEAD
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
=======
### 🔹 Run Dashboard

```bash
streamlit run dashboard/dashboard.py
```

---

## 📊 Dashboard Features

### 🧾 Overview

* Key metrics (Revenue, Orders, Rating, Delivery Time)
* Monthly trends visualization

### 💰 Revenue Analysis

* Top product categories by revenue
* Relationship between price, order volume, and revenue

### ⭐ Customer Satisfaction

* Review score distribution
* Delivery time vs rating analysis
* On-time vs delayed delivery comparison

### 👥 RFM Analysis

Customer segmentation into:

* 🏆 Champions
* 💎 Loyal Customers
* 🌱 Potential Loyalists
* ⚠️ At Risk
* ❌ Lost
>>>>>>> a65296d (progress update)

##  Product Performance
- Revenue distribution across product categories
- Identify top-performing products

<<<<<<< HEAD
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
=======
## 💡 Key Insights

📈 **Top Categories:**
Health & Beauty, Watches & Gifts, and Bed & Bath dominate revenue.

🚚 **Delivery Impact:**
Faster delivery (1–7 days) leads to significantly higher customer satisfaction.

⚠️ **Late Delivery Issue:**
Delayed orders consistently receive lower ratings.

👥 **Customer Segmentation:**
Most users fall into *Potential Loyalists* and *At Risk*, indicating retention opportunities.

---

## 🌐 Deployment

This project is deployed using Streamlit Cloud.

### 🚀 Steps:

1. Push project to GitHub
2. Connect repository to Streamlit Cloud
3. Select:

```
dashboard/dashboard.py
```

---

## 📦 Tech Stack

* 🐍 Python
* 📊 Pandas & NumPy
* 📈 Matplotlib & Seaborn
* 🌐 Streamlit

---

## ⚠️ Notes

* Large datasets may affect performance during deployment
* Consider using sampled data for cloud deployment

---

## ⭐ Highlights

✨ Clean and interactive dashboard UI
✨ Real-world dataset analysis
✨ End-to-end data workflow (Cleaning → EDA → Insight → Dashboard)
✨ Business-oriented insights

---

## 📄 License

This project is intended for educational and portfolio purposes.

---

## 💬 Final Words

This project showcases the ability to:

* Perform data cleaning and preprocessing
* Conduct exploratory data analysis (EDA)
* Extract actionable insights
* Build interactive dashboards

---

<p align="center">
  🚀 Built with passion for data & analytics
</p>
>>>>>>> a65296d (progress update)
