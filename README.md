# E-Commerce-Public
Interactive E-Commerce Data Analysis Dashboard built with Streamlit.  This project explores sales performance, customer satisfaction, and customer segmentation (RFM) using real-world datasets.  Includes data cleaning, exploratory analysis, and business insights to support data-driven decision making.

# Proyek Analisis Data: E-Commerce Public Dataset
**Nama:** Rizqi Maulidiyah  
**Email:** elkanaxafier@gmail.com  

---

## Struktur Proyek
```
proyek-ecommerce/
├── notebook.ipynb          # Notebook analisis lengkap
├── dashboard.py            # Dashboard Streamlit
├── requirements.txt        # Dependensi Python
├── README.md               # File ini
└── E-Commerce Public/                   # Letakkan semua file CSV di sini
    ├── orders_dataset.csv
    ├── order_items_dataset.csv
    ├── order_payments_dataset.csv
    ├── order_reviews_dataset.csv
    ├── products_dataset.csv
    ├── product_category_name_translation.csv
    └── customers_dataset.csv
```

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