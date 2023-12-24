# import library dasar
import pandas as pd
import streamlit as st
from dateutil.relativedelta import relativedelta  # Import relativedelta

# Plotting statistik untuk dataset
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image 
from sklearn.cluster import KMeans

# Load dataset
df = pd.read_csv('jam.csv')

# Konversi kolom 'tanggal' menjadi tipe data datetime
df['tanggal'] = pd.to_datetime(df['tanggal'])

# Fungsi untuk mengupdate visualisasi berdasarkan rentang waktu
def update_visualisasi(start_date, end_date):
    try:
        # Filter dataframe berdasarkan rentang waktu yang dipilih
        df_terfilter = df[(df['tanggal'] >= start_date) & (df['tanggal'] <= end_date)]

        # Header
        st.title('''
                 Analisis Data Aplikasi Sewa Sepeda
                 Hallo Selamat Datang di Dashboard saya
                Perkenalkan nama saya 
                
                Ahmad Rafi Syaifudin
                
                https://www.linkedin.com/in/ahmad-rafi-syaifudin-908b9426a
                 ''')

        # Tambahkan pivot table dengan kolom "kondisi_cuaca", "periode_hari", "kehangatan", "musim", "pengguna_casual", dan "pengguna_terdaftar"
        st.subheader('Pivot Table')
        tabel_pivot = pd.pivot_table(df_terfilter, values=['jumlah', 'pengguna_casual', 'pengguna_terdaftar'],
                                     index=['kondisi_cuaca', 'periode_hari', 'kehangatan', 'musim'], aggfunc='sum')
        st.dataframe(tabel_pivot.style.background_gradient(cmap='Blues'))
        st.write("Pivot table ini memberikan gambaran total sepeda yang dipakai berdasarkan kondisi cuaca, periode hari, kehangatan, dan musim.")

        # Heatmap untuk seluruh dataset
        st.subheader('Heatmap')
        heatmap_data = df_terfilter.pivot_table(values='jumlah', index='hari', columns='bulan', aggfunc='sum')
        fig, ax = plt.subplots(figsize=(12, 8))
        sns.heatmap(heatmap_data, cmap='Blues', annot=True, fmt='g', linewidths=.5, cbar_kws={"label": "Jumlah"})
        ax.set_facecolor('black')  # Latar belakang plot hitam
        st.pyplot(fig)
        st.write("Heatmap ini menunjukkan tren penggunaan sepeda setiap hari pada setiap bulan. Pada area dengan warna lebih gelap, penggunaan sepeda lebih tinggi.")

        # Pie Chart
        st.subheader('Pie Chart - Pengguna Casual vs Pengguna Terdaftar')
        pie_data = df_terfilter[['pengguna_casual', 'pengguna_terdaftar']].sum()
        fig, ax = plt.subplots()
        ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightcoral'])
        ax.axis('equal')  # Mengatur rasio aspek yang sama memastikan pie digambar sebagai lingkaran.
        st.pyplot(fig)
        st.write("Pie chart ini membandingkan kontribusi pengguna casual dan terdaftar dalam total penggunaan sepeda.")

        # Bar Chart dan Line Chart mengikuti sepeda_2011_jam
        st.subheader('Bar Chart dan Line Chart - Bulan')
        sepeda_2011_jam = df_terfilter[df_terfilter['tahun'] == 2011].groupby(['bulan', 'hari'])[['pengguna_casual', 'pengguna_terdaftar']].sum()

        # Bar Chart
        fig, ax = plt.subplots(figsize=(10, 6))
        sepeda_2011_jam['pengguna_casual'].unstack().plot(kind='bar', ax=ax, stacked=True, colormap='Blues')
        ax.set_facecolor('black')  # Latar belakang plot hitam
        st.pyplot(fig)

        # Line Chart
        fig, ax = plt.subplots(figsize=(10, 6))
        sepeda_2011_jam['pengguna_terdaftar'].unstack().plot(kind='line', ax=ax, colormap='Blues')
        ax.set_facecolor('black')  # Latar belakang plot hitam
        st.pyplot(fig)
        st.write("Bar chart dan Line chart ini menggambarkan tren penggunaan sepeda berdasarkan bulan. Bar chart menunjukkan kontribusi pengguna casual dan terdaftar dalam setiap hari, sementara Line chart menunjukkan tren total penggunaan sepeda.")

        # K-means Clustering
        st.subheader('K-means Clustering - Pengguna Casual vs Pengguna Terdaftar')
        kmeans_data = df_terfilter[['pengguna_casual', 'pengguna_terdaftar']]
        kmeans_model = KMeans(n_clusters=3, random_state=42, n_init=10).fit(kmeans_data)
        df_terfilter['cluster'] = kmeans_model.labels_

        # Penjelasan untuk Cluster
        st.write("**Cluster 0 (Biru):**")
        st.write("- Karakteristik: Instansi dengan nilai relatif rendah untuk 'Pengguna Casual' dan 'Pengguna Terdaftar'.")
        st.write("- Interpretasi: Periode dengan penggunaan sepeda secara keseluruhan rendah, di mana pengguna casual dan pengguna terdaftar memberikan kontribusi lebih sedikit.")

        st.write("**Cluster 1 (Hijau):**")
        st.write("- Karakteristik: Instansi dengan nilai sedang untuk 'Pengguna Casual' dan 'Pengguna Terdaftar'.")
        st.write("- Interpretasi: Periode dengan campuran seimbang pengguna casual dan pengguna terdaftar, menunjukkan tingkat penggunaan sepeda yang lebih konsisten.")

        st.write("**Cluster 2 (Ungu):**")
        st.write("- Karakteristik: Instansi dengan nilai relatif tinggi untuk 'Pengguna Casual' dibandingkan dengan 'Pengguna Terdaftar'.")
        st.write("- Interpretasi: Periode dengan kontribusi lebih tinggi dari pengguna casual, menunjukkan peningkatan permintaan di kalangan pengguna non-terdaftar.")

        fig, ax = plt.subplots(figsize=(10, 6))
        sns.scatterplot(data=df_terfilter, x='pengguna_casual', y='pengguna_terdaftar', hue='cluster', palette='viridis', ax=ax)
        ax.set_facecolor('black')  # Latar belakang plot hitam
        st.pyplot(fig)
        st.write("Scatter plot ini menggunakan teknik k-means clustering untuk mengelompokkan pengguna casual dan terdaftar ke dalam cluster berbeda.")

        # Contoh analisis data lainnya
        st.subheader('Ringkasan Statistik')
        st.dataframe(df_terfilter.describe().style.background_gradient(cmap='Blues'))
        st.write("Ringkasan statistik ini memberikan gambaran statistik deskriptif dari data terfilter.")

    except Exception as e:
        st.error(f"Error: {e}")

# Sidebar
st.sidebar.image(Image.open('spd.jpg'), use_column_width=True)
st.sidebar.header('Kalender')
date_input = st.sidebar.date_input('Pilih rentang waktu', [df['tanggal'].min().date(), df['tanggal'].max().date()],
                                   min_value=df['tanggal'].min(), max_value=df['tanggal'].max(), key="date_input_unique_key")

st.sidebar.header('Tipe Data')
st.sidebar.write(df.dtypes)
st.sidebar.write("Ini adalah tipe data untuk setiap kolom dalam dataset.")

# Panggil fungsi untuk pertama kali
update_visualisasi(pd.to_datetime(date_input[0]), pd.to_datetime(date_input[1]))
