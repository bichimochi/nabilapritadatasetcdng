import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.cluster import KMeans

# Load the data
day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")

# Add title and header
st.title("Bike Sharing Dashboard 🚲")
st.header("Analisis Data Penyewaan Sepeda 🔍")

# Show raw data
st.subheader("Data Penyewaan Sepeda")
st.write("Data Hari:")
st.dataframe(day_df)
st.write("Data Jam:")
st.dataframe(hour_df)

# Visualization: Pengaruh Kondisi Cuaca Terhadap Jumlah Penyewaan Sepeda
st.subheader("Pengaruh Kondisi Cuaca terhadap Jumlah Penyewaan Sepeda")
weathersit_counts = {1: 2257952, 2: 996858, 3: 37869}
labels = ['Cerah', 'Mendung', 'Hujan']
counts = [weathersit_counts[1], weathersit_counts[2], weathersit_counts[3]]
colors = ['#FFB6C1', '#DDA0DD', '#ADD8E6']

plt.figure(figsize=(8, 5))
plt.bar(labels, counts, color=colors)
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Jumlah Penyewaan Sepeda')
plt.title('Pengaruh Kondisi Cuaca Terhadap Jumlah Penyewaan Sepeda')
plt.grid(axis='y')
st.pyplot(plt)

# Visualization: Perbedaan Jumlah Sepeda yang Disewa antara Hari Kerja dan Akhir Pekan
st.subheader("Perbedaan Jumlah Sepeda yang Disewa antara Hari Kerja dan Akhir Pekan")
day_df['day_type'] = day_df['weekday'].apply(lambda x: 'Akhir Pekan' if x in [5, 6] else 'Hari Kerja')
day_type_counts = day_df.groupby('day_type')['cnt'].sum().reset_index()
colors = ['#D5A6E5', '#F2A3C7']

plt.figure(figsize=(8, 5))
sns.barplot(x='day_type', y='cnt', data=day_type_counts, palette=colors)
plt.title('Jumlah Penyewaan Sepeda Berdasarkan Tipe Hari')
plt.xlabel('Tipe Hari')
plt.ylabel('Jumlah Penyewaan Sepeda')
plt.xticks(rotation=45)
plt.grid(axis='y')
st.pyplot(plt)

# Visualization: Pengaruh Temperatur dan Kondisi Cuaca Terhadap Jumlah Penyewaan Sepeda
st.subheader("Pengaruh Temperatur dan Kondisi Cuaca Terhadap Jumlah Penyewaan Sepeda")
plt.figure(figsize=(8, 5))
sns.scatterplot(x='temp', y='cnt', hue='weathersit', data=day_df, palette="viridis")
plt.xlabel('Temperatur')
plt.ylabel('Jumlah Penyewaan Sepeda')
plt.title('Pengaruh Temperatur dan Kondisi Cuaca Terhadap Jumlah Penyewaan Sepeda')
plt.grid(True)
st.pyplot(plt)

# Clustering Analysis
st.subheader("Analisis Clustering Jumlah Penyewaan Sepeda")
# Menyiapkan data untuk clustering
data = day_df[['cnt']].copy()

# Binning data
bins = [0, 100, 500, 1000, 2000, 3000]  # Rentang penyewaan
labels = ['Sangat Rendah', 'Rendah', 'Sedang', 'Tinggi', 'Sangat Tinggi']
data['Cluster'] = pd.cut(data['cnt'], bins=bins, labels=labels)

# Menampilkan hasil binning
st.write("Hasil Clustering:")
st.write(data['Cluster'].value_counts())

# Visualisasi clustering
plt.figure(figsize=(10, 6))
plt.hist(data['cnt'], bins=bins, color='skyblue', alpha=0.7, edgecolor='black')
plt.title('Distribusi Jumlah Penyewaan Sepeda')
plt.xlabel('Jumlah Penyewaan')
plt.ylabel('Frekuensi')
plt.grid(axis='y')
st.pyplot(plt)

# RFM Analysis
st.subheader("Analisis RFM")
# 1. Recency: Menghitung jumlah hari sejak terakhir kali pelanggan melakukan penyewaan
day_df['last_rent'] = day_df['cnt'].shift(1).fillna(0)
day_df['recency'] = (day_df['last_rent'] == 0).astype(int)  # 1 jika tidak ada penyewaan sebelumnya

# 2. Frequency: Total penyewaan untuk setiap hari
frequency = day_df['cnt'].sum()

# 3. Monetary: Rata-rata pendapatan dari penyewaan
# (Misalkan 1 penyewaan = 1 unit uang)
monetary = day_df['cnt'].sum()  # Total penyewaan sebagai monetary value

# Menggabungkan RFM ke dalam dataframe
rfm_df = pd.DataFrame({
    'Recency': [day_df['recency'].sum()],
    'Frequency': [frequency],
    'Monetary': [monetary]
})

st.write("Hasil Analisis RFM:")
st.dataframe(rfm_df)

# Conclusion
st.subheader("Kesimpulan")

# Conclusion for question 1
st.write("- **Pertanyaan 1:** Terdapat perubahan signifikan terhadap penyewaan sepeda pada cuaca cerah, mendung, dan hujan. Perubahannya mencapai 50% dari cuaca cerah ke cuaca mendung. Untuk cuaca hujan, penyewa sepeda sangat sedikit dibandingkan dengan mendung dan cuaca cerah.")

# Conclusion for question 2
st.write("- **Pertanyaan 2:** Terdapat perbedaan yang tidak terlalu signifikan antara penyewaan sepeda pada hari kerja dan akhir pekan. Meskipun ada sedikit peningkatan pada akhir pekan, jumlah penyewaan sepeda pada hari kerja tetap cukup tinggi.")

# Footer
st.write("**Developed by:** Nabila P. 🚲")
st.write("**Source of Data:** [Bike Sharing Dataset](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset)")

# Run the app
if __name__ == '__main__':
    st.write("This is a streamlit app!")
