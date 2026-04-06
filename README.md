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



## Cara Menjalankan

### 1. Install dependensi
```bash
pip install -r requirements.txt
```

### 2. Siapkan dataset
Download E-Commerce Public Dataset dari Dicoding/Kaggle dan letakkan semua file `.csv` ke dalam folder `data/`.

### 3. Jalankan Notebook
```bash
jupyter notebook notebook.ipynb
```

### 4. Jalankan Dashboard Streamlit
```bash
streamlit run dashboard.py
```

---

## Pertanyaan Bisnis

1. **Kategori produk apa yang menghasilkan revenue tertinggi dan bagaimana tren penjualannya per bulan?**
2. **Bagaimana distribusi review score pelanggan dan apakah waktu pengiriman mempengaruhi kepuasan pelanggan?**

---

## Fitur Dashboard

-  **Overview** — Ringkasan eksekutif + tren bulanan
-  **Pertanyaan 1** — Analisis revenue per kategori produk
-  **Pertanyaan 2** — Analisis kepuasan pelanggan & pengiriman
-  **RFM Analysis** — Segmentasi pelanggan (analisis lanjutan)
