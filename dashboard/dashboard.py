import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Mengatur tema seaborn
sns.set_theme(style="darkgrid")

# 1. Menyiapkan Fungsi Bantuan (Helper Functions)
def create_category_performance_df(df):
    category_df = df.groupby("product_category_name").order_id.count().reset_index()
    category_df.rename(columns={"order_id": "order_count"}, inplace=True)
    return category_df.sort_values(by="order_count", ascending=False)

def create_customer_demographics_df(df):
    demographics_df = df.groupby("customer_state").customer_unique_id.nunique().reset_index()
    demographics_df.rename(columns={"customer_unique_id": "customer_count"}, inplace=True)
    return demographics_df.sort_values(by="customer_count", ascending=False)

# 2. Load Data
# Menggunakan st.cache_data agar data tidak dimuat ulang setiap kali ada interaksi
@st.cache_data
def load_data():
    df = pd.read_csv("main_data.csv")
    # Pastikan kolom waktu bertipe datetime
    df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"])
    return df

all_df = load_data()

# 3. Komponen Sidebar (Filter)
min_date = all_df["order_purchase_timestamp"].dt.date.min()
max_date = all_df["order_purchase_timestamp"].dt.date.max()

with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    st.header("Filter Data")
    
    # Mengambil rentang waktu dari input user
    start_date, end_date = st.date_input(
        label="Rentang Waktu",
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

# 4. Filter Data Utama Berdasarkan Sidebar
main_df = all_df[(all_df["order_purchase_timestamp"].dt.date >= start_date) & 
                 (all_df["order_purchase_timestamp"].dt.date <= end_date)]

# 5. Menyiapkan Dataframe Agregat
category_performance_df = create_category_performance_df(main_df)
customer_demographics_df = create_customer_demographics_df(main_df)

# ==========================================
# 6. MEMBANGUN UI DASHBOARD MAIN PAGE
# ==========================================
st.title("E-Commerce Data Dashboard 🛒")

# Bagian 1: Performa Produk
st.subheader("Top & Bottom Performing Product Categories")

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))
colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(x="order_count", y="product_category_name", data=category_performance_df.head(5), palette=colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel("Jumlah Penjualan", fontsize=15)
ax[0].set_title("5 Kategori Produk Paling Banyak Terjual", loc="center", fontsize=18)
ax[0].tick_params(axis='y', labelsize=15)

sns.barplot(x="order_count", y="product_category_name", data=category_performance_df.sort_values(by="order_count", ascending=True).head(5), palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel("Jumlah Penjualan", fontsize=15)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("5 Kategori Produk Paling Sedikit Terjual", loc="center", fontsize=18)
ax[1].tick_params(axis='y', labelsize=15)

# Render plot di Streamlit
st.pyplot(fig)

# Bagian 2: Demografi Pelanggan
st.subheader("Customer Demographics by State")

fig2, ax2 = plt.subplots(figsize=(10, 5))
top_10_states = customer_demographics_df.head(10)
sns.barplot(
    x="customer_count", 
    y="customer_state",
    data=top_10_states,
    palette=["#72BCD4" if i == 0 else "#D3D3D3" for i in range(len(top_10_states))],
    ax=ax2
)
ax2.set_title("Jumlah Pelanggan Terbanyak Berdasarkan State", fontsize=15)
ax2.set_xlabel("Jumlah Pelanggan", fontsize=12)
ax2.set_ylabel("State", fontsize=12)

# Render plot di Streamlit
st.pyplot(fig2)

st.caption("Dashboard Created by Devina Kartika")