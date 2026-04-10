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
├── Proyek_Analisis_Data.ipynb         # Comprehensive analysis and data processing
├── app.py                             # Streamlit interactive dashboard source code
├── requirements.txt                   # Technical dependencies
├── README.md                          # Project documentation
└── E-Commerce Public Dataset/         # Dataset directory (CSV files)
    ├── orders_dataset.csv
    ├── order_items_dataset.csv
    ├── order_payments_dataset.csv
    ├── order_reviews_dataset.csv
    ├── products_dataset.csv
    ├── product_category_name_translation.csv
    └── customers_dataset.csv
```

---

## Setup Environment and Run the Dashboard

### 1. Clone the Repository
```bash
git clone <repository-url>
cd proyek-ecommerce
```

### 2. Create a Virtual Environment

Creating a virtual environment isolates the project dependencies and prevents conflicts with other Python libraries installed on your system.

**Using `venv` (recommended):**
```bash
python -m venv venv
```

**Activate the virtual environment:**

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **macOS / Linux:**
  ```bash
  source venv/bin/activate
  ```

> Make sure the virtual environment is active before proceeding to the next step. You will see `(venv)` at the beginning of your terminal prompt when it is active.

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Prepare the Dataset
Make sure all CSV files from the **E-Commerce Public Dataset** are placed inside the `E-Commerce Public Dataset/` folder as shown in the directory structure above.

### 5. Run the Dashboard
```bash
streamlit run app.py
```

The dashboard will automatically open in your browser at `http://localhost:8501`.

---

## Detailed Analysis (Notebook)

To review the complete **Data Wrangling, Cleaning, and Exploratory Data Analysis (EDA)** process, run:

```bash
jupyter notebook Proyek_Analisis_Data.ipynb
```

---

## Business Questions

This analysis is designed to answer the following business questions:

1. **Which product categories had the highest number of orders (by order count) during the 2017–2018 period?**
2. **How does shipping duration (in days) affect the average customer review score for orders delivered during the 2017–2018 period?**

---

## Dashboard Features

### Executive Overview
- High-level summary of business performance
- Total revenue and order insights
- Monthly and yearly trends visualization

### Product Performance
- Revenue and order volume per product category
- Identification of best-selling product categories

### Logistics & Customer Satisfaction
- Shipping efficiency insights
- Correlation between delivery time and customer satisfaction

### RFM Segmentation
- Customer segmentation based on Recency, Frequency, and Monetary value
- Identification of high-value customers
- Actionable business strategies per segment
