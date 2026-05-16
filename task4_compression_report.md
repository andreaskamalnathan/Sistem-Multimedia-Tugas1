# Laporan Analisis Efisiensi Kompresi Gambar JPEG

**Sumber gambar asli:** `Gambar_original_lab_komputer.jpg`  
**Ukuran gambar asli:** 1,691,764 Bytes (1652.11 KB)

| Komponen / Kualitas (Q) | Ukuran File (Bytes) | Ukuran File (KB) | Rasio Kompresi | Reduksi/penguranga Ukuran (%) | Nama File |
|-------------------------|---------------------|------------------|----------------|--------------------|-------------|
| Asli (Original Baseline) | 1,691,764 | 1652.11 | 1.00:1 | 0.00% | `Gambar_original_lab_komputer.jpg` |
| JPEG (Quality = 10) | 282,938 | 276.31 | 5.98:1 | 83.28% | `./task3_jpeg_q10.jpg` |
| JPEG (Quality = 50) | 676,304 | 660.45 | 2.50:1 | 60.02% | `./task3_jpeg_q50.jpg` |
| JPEG (Quality = 90) | 1,424,161 | 1390.78 | 1.19:1 | 15.82% | `./task3_jpeg_q90.jpg` |

# Kesimpulan

1. **Quality Factor Rendah (Q = 10):** Menghasilkan reduksi data tertinggi (paling hemat memori), tetapi memicu degradasi/penurunan kualitas visual akibat hilangnya frekuensi tinggi dalam blok kuantisasi DCT (*blocking artifacts*).
2. **Quality Factor Menengah (Q = 50):** Merupakan *sweet spot* (titik tengah terbaik) di mana ukuran file berkurang drastis namun mata manusia masih mendeteksi kualitas gambar dengan sangat baik.
3. **Quality Factor Tinggi (Q = 90):** Mengutamakan retensi ketajaman piksel tinggi yang mirip gambar uncompressed/raw, berkonsekuensi pada ukuran penyimpanan yang tetap besar.
