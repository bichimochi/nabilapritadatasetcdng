## Bike Sharing Dashboard 🚲

## Deskripsi
Dashboard ini merupakan aplikasi analisis data penyewaan sepeda yang dibuat menggunakan Streamlit. Aplikasi ini memungkinkan pengguna untuk menganalisis faktor-faktor yang mempengaruhi jumlah penyewaan sepeda berdasarkan data cuaca dan jenis hari.Dalam proyek ini, kami menganalisis data penyewaan sepeda untuk memahami faktor-faktor yang mempengaruhi jumlah penyewaan. Analisis ini bertujuan untuk memberikan wawasan yang lebih dalam mengenai bagaimana kondisi cuaca, jenis hari, dan faktor lainnya mempengaruhi perilaku penyewaan sepeda.


## Fitur
- Tampilkan data penyewaan sepeda harian dan per jam.
- Visualisasi pengaruh kondisi cuaca terhadap jumlah penyewaan sepeda.
- Perbandingan jumlah penyewaan antara hari kerja dan akhir pekan.
- Analisis lebih lanjut tentang pengaruh temperatur terhadap jumlah penyewaan sepeda.

## Teknologi yang Digunakan
- **Python**: Bahasa pemrograman yang digunakan.
- **Streamlit**: Framework untuk membuat aplikasi web interaktif.
- **Pandas**: Library untuk manipulasi dan analisis data.
- **Matplotlib**: Library untuk membuat visualisasi data.
- **Seaborn**: Library untuk membuat visualisasi statistik yang lebih menarik.

## Project Analisis Data

Dalam repository ini, saya mempersembahkan proyek analisis data yang dirancang dengan cermat untuk mengungkap wawasan menarik dari data penyewaan sepeda. Dikenalkan melalui platform interaktif Streamlit.

## Struktur Direktori

- **/dashboard**: 
  - **main_data.csv**: File ini berisi data utama untuk analisis. Terdapat dua jenis data di dalamnya:
    - **hour**: Menyimpan data penyewaan sepeda berdasarkan jam, mencakup informasi seperti jumlah penyewaan, kondisi cuaca, dan faktor lainnya yang dapat mempengaruhi penyewaan sepeda per jam.
    - **day**: Menyimpan data penyewaan sepeda berdasarkan hari, dengan informasi mengenai total penyewaan harian, jenis hari (hari kerja atau akhir pekan), dan faktor lain yang mempengaruhi penyewaan sepeda per hari.
  - **dashboard.py**: Script Python ini digunakan untuk membangun aplikasi dashboard menggunakan Streamlit. Di dalamnya terdapat logika untuk memuat data dari yang dianalisis, memproses data, dan menampilkan visualisasi yang interaktif kepada pengguna.

- **/data**: 
  - **data_1.csv**: File ini berisi dataset pertama yang digunakan untuk analisis, mencakup informasi penting yang berkaitan dengan penyewaan sepeda. Data ini bisa berisi variabel yang mendukung analisis dalam `main_data.csv`.
  - **data_2.csv**: File ini berisi dataset kedua yang juga mendukung analisis, mungkin mencakup data tambahan atau data dari sumber lain yang relevan untuk memperkaya analisis penyewaan sepeda. - **notebook.ipynb**: File Jupyter Notebook ini digunakan untuk melakukan analisis data secara eksploratif. 
 - **README.md**: File ini berisi informasi penting tentang proyek, termasuk deskripsi proyek, fitur, cara instalasi, penggunaan, dan detail lainnya yang diperlukan oleh pengguna atau pengembang lain yang ingin memahami atau berkontribusi pada proyek ini.

- **requirements.txt**: File ini berisi daftar pustaka Python yang diperlukan untuk menjalankan proyek. Dengan file ini, pengguna dapat menginstal semua dependensi yang diperlukan dengan satu perintah menggunakan `pip`.

- **url.txt**: File ini berisi tautan atau URL yang relevan untuk proyek. 


## Instalasi

1. Clone repository ini ke komputer lokal Anda menggunakan perintah berikut:

   ```shell
   git clone https://github.com/bichimochi/nabilapritadatasetcdng.git
   
2. Instal pustaka-pustaka tersebut dengan menjalankan perintah berikut:
   pip install -r requirements.txt
3. Direktori proyek (Local):
   cd nabilapritadatasetcdng/dashboard/
   streamlit run dashboard.py
4. Link
   [Project DA (Data Analytics) Bike Dataset](https://nabilapritadatasetcdng-h5bgdbg2lwbqhhsau6autq.streamlit.app/))

---

© 2024 Nabila Prita Rizqika Siagian. All rights reserved.
