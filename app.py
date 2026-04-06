import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

#  Page config 
st.set_page_config(
    page_title="E-Commerce Dashboard",
    page_icon=":shopping_cart:",
    layout="wide",
    initial_sidebar_state="expanded"
)

#  Global CSS 
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600;700&family=DM+Mono:wght@400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

/*  Sidebar  */
[data-testid="stSidebar"] {
    background: #0f1117 !important;
    border-right: 1px solid #1e2130;
}
[data-testid="stSidebar"] * {
    color: #c9d1e0 !important;
}
[data-testid="stSidebar"] .stRadio label {
    font-size: 0.85rem;
    padding: 0.3rem 0;
}
[data-testid="stSidebar"] hr {
    border-color: #1e2130 !important;
}

/*  Main background  */
.main .block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
    max-width: 1200px;
}

/*  Page header  */
.page-header {
    display: flex;
    align-items: flex-end;
    gap: 1rem;
    margin-bottom: 1.8rem;
    padding-bottom: 1rem;
    border-bottom: 1px solid #e8ecf2;
}
.page-header .title {
    font-size: 1.55rem;
    font-weight: 700;
    color: #0d1117;
    letter-spacing: -0.02em;
    margin: 0;
}
.page-header .sub {
    font-size: 0.82rem;
    color: #8892a4;
    margin: 0;
    padding-bottom: 2px;
}

/*  Metric cards  */
.kpi-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 0.9rem;
    margin-bottom: 1.8rem;
}
.kpi-card {
    background: #ffffff;
    border: 1px solid #e8ecf2;
    border-radius: 10px;
    padding: 1.1rem 1.3rem;
    position: relative;
    overflow: hidden;
}
.kpi-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: #1a56db;
}
.kpi-card.green::before  { background: #0ca678; }
.kpi-card.amber::before  { background: #e8a000; }
.kpi-card.slate::before  { background: #6b7a99; }
.kpi-label {
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #8892a4;
    margin-bottom: 0.45rem;
}
.kpi-value {
    font-size: 1.85rem;
    font-weight: 700;
    color: #0d1117;
    font-family: 'DM Mono', monospace;
    letter-spacing: -0.02em;
    line-height: 1;
    margin-bottom: 0.4rem;
}
.kpi-note {
    font-size: 0.72rem;
    color: #8892a4;
}

/*  Section label  */
.section-label {
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #8892a4;
    margin: 1.8rem 0 0.8rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
.section-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: #e8ecf2;
}

/*  Insight box  */
.insight {
    background: #f5f7ff;
    border: 1px solid #d6dcf7;
    border-radius: 8px;
    padding: 0.9rem 1.1rem;
    margin-top: 1.2rem;
    font-size: 0.83rem;
    color: #3a4567;
    line-height: 1.6;
}
.insight strong {
    display: block;
    font-size: 0.78rem;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: #1a56db;
    margin-bottom: 0.3rem;
}

/*  Chart wrapper  */
.chart-card {
    background: #ffffff;
    border: 1px solid #e8ecf2;
    border-radius: 10px;
    padding: 1.2rem;
}

/*  Sidebar logo area  */
.sb-brand {
    padding: 0.5rem 0 1rem;
}
.sb-brand .brand-name {
    font-size: 0.95rem;
    font-weight: 700;
    color: #ffffff !important;
    letter-spacing: -0.01em;
}
.sb-brand .brand-sub {
    font-size: 0.72rem;
    color: #6b7a99 !important;
}
.sb-nav-label {
    font-size: 0.65rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #4a5568 !important;
    margin-bottom: 0.3rem;
}
</style>
""", unsafe_allow_html=True)

#  Matplotlib style 
plt.rcParams.update({
    'font.family': 'sans-serif',
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.grid': True,
    'grid.color': '#eef0f5',
    'grid.linewidth': 0.8,
    'axes.facecolor': '#ffffff',
    'figure.facecolor': '#ffffff',
    'axes.labelcolor': '#6b7a99',
    'axes.labelsize': 9,
    'xtick.color': '#6b7a99',
    'ytick.color': '#6b7a99',
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'axes.titlesize': 11,
    'axes.titleweight': 'bold',
    'axes.titlecolor': '#0d1117',
})

BLUE   = '#1a56db'
BLUE2  = '#93b4fb'
GREEN  = '#0ca678'
AMBER  = '#e8a000'
SLATE  = '#6b7a99'
PALETTE = [BLUE, '#3b82f6', '#93b4fb', '#bfdbfe', '#dbeafe']

#  Load data 
@st.cache_data
def load_data():
    try:
        orders        = pd.read_csv('E-Commerce Public Dataset/orders_dataset.csv')
        items         = pd.read_csv('E-Commerce Public Dataset/order_items_dataset.csv')
        reviews       = pd.read_csv('E-Commerce Public Dataset/order_reviews_dataset.csv')
        products      = pd.read_csv('E-Commerce Public Dataset/products_dataset.csv')
        category_trans = pd.read_csv('E-Commerce Public Dataset/product_category_name_translation.csv')
        customers     = pd.read_csv('E-Commerce Public Dataset/customers_dataset.csv')

        date_cols = ['order_purchase_timestamp','order_approved_at',
                     'order_delivered_carrier_date','order_delivered_customer_date',
                     'order_estimated_delivery_date']
        for col in date_cols:
            orders[col] = pd.to_datetime(orders[col])

        orders = orders[orders['order_status'] == 'delivered'].copy()
        orders['delivery_days']  = (orders['order_delivered_customer_date'] - orders['order_purchase_timestamp']).dt.days
        orders['delivery_delay'] = (orders['order_delivered_customer_date'] - orders['order_estimated_delivery_date']).dt.days
        orders = orders[orders['delivery_days'] > 0]

        products   = products.merge(category_trans, on='product_category_name', how='left')
        items_prod = items.merge(products[['product_id','product_category_name_english']], on='product_id', how='left')
        main       = orders.merge(items_prod, on='order_id', how='inner')
        main       = main.merge(reviews[['order_id','review_score']], on='order_id', how='left')
        main       = main.merge(customers[['customer_id','customer_unique_id']], on='customer_id', how='left')

        main['order_month'] = main['order_purchase_timestamp'].dt.to_period('M').astype(str)
        main['order_year']  = main['order_purchase_timestamp'].dt.year
        return main
    except Exception as e:
        st.error(f"Error loading data: {e}")
        st.info("Pastikan folder **E-Commerce Public Dataset/** berisi semua file CSV.")
        return None


df = load_data()

#  Sidebar 
with st.sidebar:
    st.markdown("""
    <div class="sb-brand">
        <div class="brand-name">E-Commerce Analytics</div>
        <div class="brand-sub">Rizqi Maulidiyah &nbsp;·&nbsp; Dicoding Final Project</div>
    </div>
    """, unsafe_allow_html=True)
    st.divider()

    if df is not None:
        years = sorted(df['order_year'].dropna().unique().tolist())
        selected_years = st.multiselect("Tahun", years, default=years)

        categories = ['Semua'] + sorted(df['product_category_name_english'].dropna().unique().tolist())
        selected_cat = st.selectbox("Kategori Produk", categories)

        st.divider()
        st.markdown('<div class="sb-nav-label">Navigasi</div>', unsafe_allow_html=True)
        page = st.radio("", [
            "Overview",
            "Revenue & Produk",
            "Kepuasan Pelanggan",
            "Analisis RFM"
        ], label_visibility="collapsed")
    else:
        page = "Overview"

#  Filter data 
if df is not None:
    filtered = df[df['order_year'].isin(selected_years)] if selected_years else df.copy()
    if selected_cat != 'Semua':
        filtered = filtered[filtered['product_category_name_english'] == selected_cat]

if df is None:
    st.warning("Data belum tersedia. Letakkan file CSV di dalam folder `E-Commerce Public Dataset/`.")
    st.stop()


# PAGE: OVERVIEW
if page == "Overview":

    st.markdown("""
    <div class="page-header">
        <div>
            <p class="title">Ringkasan Eksekutif</p>
            <p class="sub">Performa keseluruhan bisnis berdasarkan data pesanan terkirim</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    total_orders  = filtered['order_id'].nunique()
    total_revenue = filtered['price'].sum()
    avg_review    = filtered['review_score'].mean()
    avg_delivery  = filtered['delivery_days'].mean()

    st.markdown(f"""
    <div class="kpi-grid">
        <div class="kpi-card">
            <div class="kpi-label">Total Orders</div>
            <div class="kpi-value">{total_orders:,}</div>
            <div class="kpi-note">Pesanan terkirim</div>
        </div>
        <div class="kpi-card green">
            <div class="kpi-label">Total Revenue</div>
            <div class="kpi-value">R${total_revenue/1e6:.2f}M</div>
            <div class="kpi-note">Dalam juta BRL</div>
        </div>
        <div class="kpi-card amber">
            <div class="kpi-label">Avg Review Score</div>
            <div class="kpi-value">{avg_review:.2f}</div>
            <div class="kpi-note">dari 5.0 bintang</div>
        </div>
        <div class="kpi-card slate">
            <div class="kpi-label">Avg Delivery Days</div>
            <div class="kpi-value">{avg_delivery:.1f}</div>
            <div class="kpi-note">hari rata-rata</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-label">Tren Bulanan</div>', unsafe_allow_html=True)

    monthly = (
        filtered.groupby('order_month')
        .agg(revenue=('price','sum'), orders=('order_id','nunique'))
        .reset_index()
        .sort_values('order_month')
    )

    fig, ax1 = plt.subplots(figsize=(13, 4.5))
    ax2 = ax1.twinx()

    x = range(len(monthly))
    ax2.bar(x, monthly['orders'], color=BLUE2, alpha=0.35, zorder=1, label='Orders')
    ax1.fill_between(x, monthly['revenue']/1e3, alpha=0.12, color=BLUE, zorder=2)
    ax1.plot(x, monthly['revenue']/1e3, color=BLUE, linewidth=2, marker='o',
             markersize=3.5, zorder=3, label='Revenue')

    step = max(1, len(monthly)//10)
    ax1.set_xticks(range(0, len(monthly), step))
    ax1.set_xticklabels(monthly['order_month'][::step], rotation=40, ha='right')
    ax1.set_ylabel('Revenue (Ribu BRL)', color=BLUE)
    ax2.set_ylabel('Jumlah Order', color=SLATE)
    ax1.tick_params(axis='y', colors=BLUE)
    ax2.tick_params(axis='y', colors=SLATE)
    ax2.spines['right'].set_visible(True)
    ax2.spines['right'].set_color('#e8ecf2')
    ax1.set_title('Tren Revenue & Jumlah Pesanan per Bulan', pad=12)

    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1+lines2, labels1+labels2, fontsize=8, framealpha=0.9,
               loc='upper left', frameon=True, edgecolor='#e8ecf2')

    plt.tight_layout()
    st.pyplot(fig, use_container_width=True)
    plt.close()

    st.markdown("""
    <div class="insight">
        <strong>Insight</strong>
        Bisnis tumbuh konsisten sejak 2017 dengan puncak revenue di akhir 2017, kemungkinan
        didorong oleh event promosi besar (Black Friday). Rata-rata kepuasan pelanggan stabil
        di angka 4+ bintang sepanjang periode.
    </div>
    """, unsafe_allow_html=True)


# PAGE: REVENUE & PRODUK
elif page == "Revenue & Produk":

    st.markdown("""
    <div class="page-header">
        <div>
            <p class="title">Revenue & Kategori Produk</p>
            <p class="sub">Kategori mana yang menghasilkan revenue dan volume order tertinggi?</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col_n = st.slider("Tampilkan Top N Kategori", min_value=5, max_value=20, value=10)

    revenue_cat = (
        filtered.groupby('product_category_name_english')
        .agg(total_revenue=('price','sum'), total_orders=('order_id','nunique'), avg_price=('price','mean'))
        .reset_index()
        .sort_values('total_revenue', ascending=False)
        .head(col_n)
    )

    fig, axes = plt.subplots(1, 2, figsize=(15, 5.5))

    # — Horizontal bar —
    n = len(revenue_cat)
    bar_colors = [BLUE if i == 0 else BLUE2 for i in range(n)]
    bars = axes[0].barh(
        revenue_cat['product_category_name_english'][::-1],
        revenue_cat['total_revenue'][::-1] / 1e6,
        color=bar_colors[::-1], height=0.65
    )
    for bar, val in zip(bars, revenue_cat['total_revenue'][::-1]):
        axes[0].text(bar.get_width() + 0.01, bar.get_y() + bar.get_height()/2,
                     f'R${val/1e6:.2f}M', va='center', fontsize=7.5, color=SLATE)
    axes[0].set_xlabel('Total Revenue (Juta BRL)')
    axes[0].set_title(f'Top {col_n} Kategori — Revenue')
    axes[0].xaxis.set_major_formatter(mtick.FormatStrFormatter('%.1fM'))
    axes[0].grid(axis='y', alpha=0)

    # — Scatter —
    scatter_data = (
        filtered.groupby('product_category_name_english')
        .agg(orders=('order_id','nunique'), avg_price=('price','mean'), revenue=('price','sum'))
        .reset_index()
    )
    top20 = scatter_data.nlargest(20, 'revenue')
    sc = axes[1].scatter(
        top20['orders'], top20['avg_price'],
        s=top20['revenue']/6000, alpha=0.75,
        c=top20['revenue'], cmap='Blues',
        edgecolors='white', linewidth=0.8, zorder=3
    )
    for _, row in top20.iterrows():
        if row['revenue'] > top20['revenue'].quantile(0.72):
            axes[1].annotate(
                row['product_category_name_english'],
                (row['orders'], row['avg_price']),
                fontsize=6.5, ha='center', va='bottom', color=SLATE
            )
    axes[1].set_xlabel('Jumlah Order')
    axes[1].set_ylabel('Rata-rata Harga (BRL)')
    axes[1].set_title('Volume Order vs Harga Rata-rata\n(ukuran lingkaran = total revenue)')
    plt.colorbar(sc, ax=axes[1], label='Revenue (BRL)', shrink=0.8)

    plt.tight_layout(pad=2)
    st.pyplot(fig, use_container_width=True)
    plt.close()

    st.markdown('<div class="section-label">Data Detail Kategori</div>', unsafe_allow_html=True)
    display_df = revenue_cat.copy()
    display_df['total_revenue'] = display_df['total_revenue'].map('R$ {:,.0f}'.format)
    display_df['avg_price']     = display_df['avg_price'].map('R$ {:,.2f}'.format)
    display_df.columns = ['Kategori','Total Revenue','Total Orders','Avg Price']
    st.dataframe(display_df, use_container_width=True, hide_index=True)

    st.markdown("""
    <div class="insight">
        <strong>Kesimpulan</strong>
        Kategori <b>health_beauty</b> mendominasi revenue. <b>watches_gifts</b> dan
        <b>bed_bath_table</b> menempati posisi dua dan tiga. Fokus stok dan promosi
        di ketiga kategori ini akan memberikan dampak terbesar pada pendapatan.
    </div>
    """, unsafe_allow_html=True)


# PAGE: KEPUASAN PELANGGAN
elif page == "Kepuasan Pelanggan":

    st.markdown("""
    <div class="page-header">
        <div>
            <p class="title">Kepuasan Pelanggan</p>
            <p class="sub">Bagaimana waktu pengiriman mempengaruhi review score?</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        fig, ax = plt.subplots(figsize=(6.5, 4.5))
        score_counts = filtered['review_score'].value_counts().sort_index()
        colors_bar = ['#ef4444','#f97316','#facc15','#84cc16','#22c55e']
        bars = ax.bar(score_counts.index, score_counts.values,
                      color=colors_bar[:len(score_counts)],
                      edgecolor='white', linewidth=1.5, width=0.6)
        for bar, val in zip(bars, score_counts.values):
            pct = val / score_counts.sum() * 100
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 80,
                    f'{pct:.1f}%', ha='center', fontsize=9, fontweight='600', color='#0d1117')
        ax.set_xlabel('Review Score')
        ax.set_ylabel('Jumlah Ulasan')
        ax.set_title('Distribusi Review Score Pelanggan')
        ax.yaxis.set_major_formatter(mtick.FuncFormatter(lambda x,_: f'{int(x):,}'))
        plt.tight_layout()
        st.pyplot(fig, use_container_width=True)
        plt.close()

    with col2:
        plot_data = filtered[['delivery_days','review_score']].dropna()
        plot_data = plot_data[(plot_data['delivery_days']>0) & (plot_data['delivery_days']<=60)].copy()
        plot_data['delivery_group'] = pd.cut(
            plot_data['delivery_days'],
            bins=[0,7,14,21,30,60],
            labels=['1–7 hari','8–14 hari','15–21 hari','22–30 hari','>30 hari']
        )
        fig, ax = plt.subplots(figsize=(6.5, 4.5))
        sns.boxplot(data=plot_data, x='delivery_group', y='review_score',
                    palette=['#1a56db','#3b82f6','#60a5fa','#93c5fd','#bfdbfe'],
                    ax=ax, linewidth=0.9, fliersize=2)
        means = plot_data.groupby('delivery_group', observed=True)['review_score'].mean()
        for i,(group,mv) in enumerate(means.items()):
            ax.text(i, mv+0.15, f'{mv:.2f}', ha='center', fontsize=8.5,
                    color=BLUE, fontweight='700')
        ax.set_xlabel('Lama Pengiriman')
        ax.set_ylabel('Review Score')
        ax.set_title('Review Score vs Lama Pengiriman')
        ax.set_yticks([1,2,3,4,5])
        plt.tight_layout()
        st.pyplot(fig, use_container_width=True)
        plt.close()

    st.markdown('<div class="section-label">Analisis Keterlambatan</div>', unsafe_allow_html=True)

    delay_data = filtered[['delivery_delay','review_score']].dropna().copy()
    delay_data['status'] = delay_data['delivery_delay'].apply(
        lambda x: 'Tepat / Lebih Cepat' if x <= 0 else 'Terlambat'
    )

    fig, ax = plt.subplots(figsize=(9, 4))
    delay_avg = (
        delay_data.groupby('status')['review_score']
        .value_counts(normalize=True).unstack().fillna(0) * 100
    )
    delay_avg.plot(kind='bar', ax=ax,
                   color=['#ef4444','#f97316','#facc15','#84cc16','#22c55e'],
                   edgecolor='white', linewidth=0.8)
    ax.set_xlabel('')
    ax.set_ylabel('Persentase (%)')
    ax.set_title('Distribusi Review Score: Tepat Waktu vs Terlambat')
    ax.legend(title='Review Score', bbox_to_anchor=(1.01,1), fontsize=8)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    plt.tight_layout()
    st.pyplot(fig, use_container_width=True)
    plt.close()

    on_time_avg = delay_data[delay_data['status']=='Tepat / Lebih Cepat']['review_score'].mean()
    late_avg    = delay_data[delay_data['status']=='Terlambat']['review_score'].mean()

    st.markdown(f"""
    <div class="kpi-grid" style="grid-template-columns: repeat(2,1fr); max-width:560px;">
        <div class="kpi-card green">
            <div class="kpi-label">Avg Score — Tepat Waktu</div>
            <div class="kpi-value">{on_time_avg:.2f}</div>
        </div>
        <div class="kpi-card" style="border-top:none; position:relative;">
            <div style="position:absolute;top:0;left:0;right:0;height:3px;background:#ef4444;border-radius:10px 10px 0 0;"></div>
            <div class="kpi-label">Avg Score — Terlambat</div>
            <div class="kpi-value">{late_avg:.2f}</div>
            <div class="kpi-note" style="color:#ef4444;">Lebih rendah {on_time_avg-late_avg:.2f} poin</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="insight">
        <strong>Kesimpulan</strong>
        Ada korelasi negatif yang jelas antara lama pengiriman dan kepuasan pelanggan.
        Pesanan yang tiba dalam <b>1–7 hari</b> mendapatkan rating tertinggi.
        Pesanan yang <b>terlambat</b> dari estimasi menurunkan skor ulasan secara signifikan.
        Investasi pada efisiensi logistik adalah prioritas utama.
    </div>
    """, unsafe_allow_html=True)


# PAGE: RFM
elif page == "Analisis RFM":

    st.markdown("""
    <div class="page-header">
        <div>
            <p class="title">Segmentasi Pelanggan — RFM</p>
            <p class="sub">Recency · Frequency · Monetary</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    snapshot_date = filtered['order_purchase_timestamp'].max() + pd.Timedelta(days=1)

    rfm = filtered.groupby('customer_unique_id').agg(
        Recency  =('order_purchase_timestamp', lambda x: (snapshot_date - x.max()).days),
        Frequency=('order_id','nunique'),
        Monetary =('price','sum')
    ).reset_index()

    rfm['R_Score'] = pd.qcut(rfm['Recency'], q=4, labels=[4,3,2,1], duplicates='drop').astype(float).astype(int)
    rfm['F_Score'] = pd.cut(rfm['Frequency'], bins=[0,1,2,3,rfm['Frequency'].max()],
                             labels=[1,2,3,4], include_lowest=True).astype(float).astype(int)
    rfm['M_Score'] = pd.qcut(rfm['Monetary'], q=4, labels=[1,2,3,4], duplicates='drop').astype(float).astype(int)
    rfm['RFM_Score'] = rfm['R_Score'] + rfm['F_Score'] + rfm['M_Score']

    def segment(s):
        if   s >= 10: return 'Champions'
        elif s >= 7:  return 'Loyal Customers'
        elif s >= 5:  return 'Potential Loyalists'
        elif s >= 3:  return 'At Risk'
        else:         return 'Lost'

    rfm['Segment'] = rfm['RFM_Score'].apply(segment)
    seg_dist = rfm['Segment'].value_counts()

    col1, col2 = st.columns([1, 1.3])

    with col1:
        fig, ax = plt.subplots(figsize=(5.5, 5.5))
        seg_colors = [BLUE,'#3b82f6','#60a5fa','#f97316','#ef4444']
        wedges, texts, autotexts = ax.pie(
            seg_dist.values, labels=seg_dist.index,
            autopct='%1.1f%%', colors=seg_colors[:len(seg_dist)],
            startangle=90, pctdistance=0.80,
            wedgeprops={'edgecolor':'white','linewidth':2.5}
        )
        for at in autotexts:
            at.set_fontsize(9); at.set_fontweight('700')
        for t in texts:
            t.set_fontsize(8.5); t.set_color('#0d1117')
        ax.set_title('Distribusi Segmen Pelanggan', pad=14)
        plt.tight_layout()
        st.pyplot(fig, use_container_width=True)
        plt.close()

    with col2:
        seg_order = ['Champions','Loyal Customers','Potential Loyalists','At Risk','Lost']
        seg_m = rfm.groupby('Segment')[['Recency','Frequency','Monetary']].mean().reindex(
            [s for s in seg_order if s in rfm['Segment'].unique()]
        )
        seg_m['Monetary'] = seg_m['Monetary'] / 100

        fig, ax = plt.subplots(figsize=(7, 5))
        x, w = np.arange(len(seg_m)), 0.24
        ax.bar(x - w,   seg_m['Recency'],   w, label='Recency (hari)', color='#ef4444', alpha=0.85)
        ax.bar(x,       seg_m['Frequency'], w, label='Frequency',       color=BLUE,     alpha=0.85)
        ax.bar(x + w,   seg_m['Monetary'],  w, label='Monetary (BRL/100)', color=GREEN, alpha=0.85)
        ax.set_xticks(x)
        ax.set_xticklabels(seg_m.index, rotation=15, ha='right', fontsize=8)
        ax.set_title('Perbandingan RFM per Segmen')
        ax.legend(fontsize=7.5, framealpha=0.9, edgecolor='#e8ecf2')
        plt.tight_layout()
        st.pyplot(fig, use_container_width=True)
        plt.close()

    st.markdown('<div class="section-label">Ringkasan Segmen</div>', unsafe_allow_html=True)
    summary = rfm.groupby('Segment').agg(
        Jumlah_Pelanggan=('customer_unique_id','count'),
        Avg_Recency     =('Recency','mean'),
        Avg_Frequency   =('Frequency','mean'),
        Avg_Monetary    =('Monetary','mean')
    ).round(1).reset_index()
    summary['Avg_Monetary'] = summary['Avg_Monetary'].map('R$ {:,.1f}'.format)
    st.dataframe(summary, use_container_width=True, hide_index=True)

    st.markdown("""
    <div class="insight">
        <strong>Insight RFM</strong>
        Sebagian besar pelanggan masuk dalam segmen <b>Potential Loyalists</b> dan <b>At Risk</b>.
        Fokuskan program loyalitas pada segmen <b>Champions</b> dan strategi re-engagement untuk
        segmen <b>At Risk</b> agar tidak bergeser ke segmen <b>Lost</b>.
    </div>
    """, unsafe_allow_html=True)


#  Footer 
st.divider()
st.markdown("""
<p style="text-align:center; color:#8892a4; font-size:0.75rem; letter-spacing:0.04em;">
    E-Commerce Analytics Dashboard &nbsp;·&nbsp; Rizqi Maulidiyah &nbsp;·&nbsp; Proyek Akhir Dicoding Data Analysis
</p>
""", unsafe_allow_html=True)