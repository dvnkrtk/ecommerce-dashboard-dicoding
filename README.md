# E-Commerce Public Data Analysis Dashboard 

## Deskripsi Proyek
Proyek ini merupakan dasboard interaktif berbasis web yang dibangun menggunakan Streamlit. Dasboard ini menyajikan hasil eksplorasi dan analisis data dari E-Commerce Public Dataset. 

Tujuan utama dari dasbor ini adalah untuk memberikan wawasan bisnis (business insights) terkait:
1. Performa penjualan berdasarkan kategori produk (mengidentifikasi kategori paling laris dan paling sepi).
2. Persebaran demografi pelanggan berdasarkan negara bagian (state) untuk melihat konsentrasi pasar.
3. Melakukan segmentasi pelanggan menggunakan metode RFM (Recency, Frequency, Monetary) Analysis.

## Struktur Direktori
- `/dashboard`: Berisi file utama aplikasi Streamlit (`dashboard.py`) dan data bersih yang digunakan (`main_data.csv`).
- `/data`: Berisi file dataset mentah berformat CSV.
- `notebook.ipynb`: Berisi alur kerja analisis data mulai dari pengumpulan, pembersihan, eksplorasi, hingga analisis lanjutan.

## Cara Menjalankan Dasbor (Lokal)

### 1. Setup Environment
Pastikan Python sudah terinstal di komputermu. Buka terminal atau command prompt, lalu instal semua library yang dibutuhkan dengan menjalankan perintah berikut:

```bash
pip install -r requirements.txt
cd dashboard
streamlit run dashboard.py

cd dashboard
streamlit run dashboard.py
