# Panduan Manual: Analisis Data Aplikasi Sewa Sepeda dengan Streamlit

## 1. Persiapkan Lingkungan Kerja
Pastikan Python dan pip telah terinstal di lingkungan kerja Anda.
Instal library yang diperlukan dengan menjalankan perintah berikut di terminal atau command prompt:
bash
Copy code
```
pip install pandas streamlit matplotlib seaborn scikit-learn
```
## 2. Siapkan Dataset
Pastikan Anda memiliki file dataset `jam.csv`yang digunakan dalam code.
Letakkan file dataset di direktori yang sama dengan script Python.
## 3. Unduh Gambar dan Library
Unduh gambar `spd.jpg` dan letakkan di direktori yang sama dengan script Python.
Pastikan semua library yang diimpor pada script tersedia.
## 4. Jalankan Script Python
Buka terminal atau command prompt.
Pindah ke direktori tempat Anda menyimpan script Python.
Jalankan perintah berikut:
bash
Copy code
```
streamlit run nama_script.py
```
Gantilah 'nama_script.py' dengan nama file Python yang berisi code di atas.
## 5. Gunakan Aplikasi Streamlit
Setelah menjalankan perintah di atas, akan muncul URL lokal (biasanya http://localhost:8501) di terminal.
Buka URL tersebut di browser web Anda.
## 6. Atur Rentang Waktu dengan Kalender
Di sidebar aplikasi, Anda akan melihat bagian "Kalender".
Pilih rentang waktu dengan mengklik kalender.
Pilih tanggal awal dan tanggal akhir.
## 7. Amati Visualisasi yang Berubah
Setelah memilih rentang waktu, semua visualisasi dalam aplikasi akan disesuaikan dengan rentang waktu yang Anda pilih.
Amati dan analisis pivot table, heatmap, pie chart, bar chart, line chart, k-means clustering, dan ringkasan statistik berdasarkan rentang waktu yang telah Anda tentukan.
## 8. Eksplorasi Data
Nikmati eksplorasi data yang dinamis dan sesuaikan analisis Anda berdasarkan rentang waktu yang diinginkan.

# Selamat menggunakan aplikasi analisis data sepeda! 
