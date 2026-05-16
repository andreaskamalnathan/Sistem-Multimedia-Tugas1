import os
import numpy as np
from PIL import Image

def task1_rgb_to_grayscale(image_path, output_path="task1_grayscale.jpg"):
    """
    TASK 1: Konversi Gambar RGB ke Grayscale Murni dengan memanipulasi bitplanes
    rumus yang digunakan ITU-R 601-2 berbasis luma/luminans untuk mencerminkan 
    sensitivitas mata manusia secara presisi terhadap komponen warna yaitu:
    Y = 0.299*R + 0.587*G + 0.114*B
    """
    img = Image.open(image_path).convert("RGB")
    img_array = np.array(img)
    
    # melakukan ekstraksi matriks untuk maing-masing channel rgb
    r = img_array[:, :, 0]
    g = img_array[:, :, 1]
    b = img_array[:, :, 2]
    
    # transformasi matriks linier
    gray_array = (0.299 * r + 0.587 * g + 0.114 * b).astype(np.uint8)
    
    # menyimpan gambar ke grayscale
    gray_img = Image.fromarray(gray_array)
    gray_img.save(output_path)
    print(f"[Task 1] Behasil. Gambar grayscale berhasil disimpan ke -> {output_path}")
    return output_path


def task2_split_channels(image_path, output_dir="."):
    """
    TASK 2: Split gambar kedalam tiga channel independen (Merah, Hijau, Biru)
    """
    img = Image.open(image_path).convert("RGB")
    img_array = np.array(img)
    
    # Membuat matriks nol (zero padding) seukuran dimensi gambar tunggal
    zeros = np.zeros_like(img_array[:, :, 0])
    
    # Rekonstruksi struktur channel warna independen (3D tensor)
    red_channel = np.stack([img_array[:, :, 0], zeros, zeros], axis=-1)
    green_channel = np.stack([zeros, img_array[:, :, 1], zeros], axis=-1)
    blue_channel = np.stack([zeros, zeros, img_array[:, :, 2]], axis=-1)
    
    # Menentukan path output
    r_path = os.path.join(output_dir, "task2_channel_red.jpg")
    g_path = os.path.join(output_dir, "task2_channel_green.jpg")
    b_path = os.path.join(output_dir, "task2_channel_blue.jpg")
    
    Image.fromarray(red_channel).save(r_path)
    Image.fromarray(green_channel).save(g_path)
    Image.fromarray(blue_channel).save(b_path)
    
    print(f"[Task 2] Berhasil. Channel Merah, Hijau, & Biru disimpan di -> {output_dir}")
    return r_path, g_path, b_path


def task3_jpeg_compression(image_path, qualities=[10, 50, 90], output_dir="."):
    """
    TASK 3: Conversi jpeg algoritmis dengan menetapkan quality factor (Q) = 10, 50, dan 90.
    Menerapkan kuantisasi discrete cosine transform (DCT) dengan variasi nilai Q.
    """
    img = Image.open(image_path).convert("RGB")
    compressed_paths = {}
    
    for q in qualities:
        output_path = os.path.join(output_dir, f"task3_jpeg_q{q}.jpg")
        img.save(output_path, "JPEG", quality=q)
        compressed_paths[q] = output_path
        print(f"[Task 3] Berhasil: jpeg convertion dengan Q={q} disimpan ke -> {output_path}")       
    return compressed_paths


def task4_generate_compression_report(original_path, compressed_paths, report_path="task4_compression_report.md"):
    """
    TASK 4: Membuat markdown (md) report untuk menghitung efisiensi persentase ukuran byte
    pada storage akibat kompresi tersebut dibandingkan raw size matematis.
    yang dihitung adalah ukuran berkas, Rasio Kompresi (CR), dan Persentase Reduksi Data.
    """
    orig_size = os.path.getsize(original_path)
    
    report_lines = [
        "# Laporan Analisis Efisiensi Kompresi Citra JPEG",
        f"**Berkas Gambar Sumber:** `{original_path}`",
        f"**Ukuran Berkas Sumber:** {orig_size:,} Bytes ({orig_size / 1024:.2f} KB)\\n",
        "| Komponen / Kualitas (Q) | Ukuran File (Bytes) | Ukuran File (KB) | Rasio Kompresi | Reduksi Ukuran (%) | Nama Berkas |",
        "|-------------------------|---------------------|------------------|----------------|--------------------|-------------|",
        f"| Asli (Original Baseline) | {orig_size:,} | {orig_size/1024:.2f} | 1.00:1 | 0.00% | `{original_path}` |"
    ]
    #menampilkan row perthitungannya
    for q, path in sorted(compressed_paths.items()):
        comp_size = os.path.getsize(path)
        compression_ratio = orig_size / comp_size
        reduction_percentage = ((orig_size - comp_size) / orig_size) * 100
        
        report_lines.append(
            f"| JPEG (Quality = {q}) | {comp_size:,} | {comp_size/1024:.2f} | {compression_ratio:.2f}:1 | {reduction_percentage:.2f}% | `{path}` |"
        )
        
    report_lines.extend([
        "\\n## Kesimpulan Analisis Sistem Citra Digital",
        "1. **Quality Factor Rendah (Q = 10):** Menghasilkan reduksi data tertinggi (paling hemat memori), tetapi memicu degradasi visual akibat hilangnya frekuensi tinggi dalam blok kuantisasi DCT (*blocking artifacts*).",
        "2. **Quality Factor Menengah (Q = 50):** Merupakan *sweet spot* (titik tengah terbaik) di mana ukuran file berkurang drastis namun mata manusia masih mendeteksi kualitas gambar dengan sangat baik.",
        "3. **Quality Factor Tinggi (Q = 90):** Mengutamakan retensi ketajaman piksel tinggi yang mirip citra uncompressed, berkonsekuensi pada ukuran penyimpanan yang tetap besar."
    ])
    
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\\n".join(report_lines))
        
    print(f"[Task 4] Sukses: Laporan formal dalam format Markdown tersimpan di -> {report_path}")
    return report_path

if __name__ == "__main__":
    # Menetapkan file gambar masukan dari input pengguna
    image_source = "Gambar_original_lab_komputer.jpg"
    
    if not os.path.exists(image_source):
        print(f"Error: Berkas '{image_source}' tidak ditemukan.")
    else:
        print("=== memulai eksekusi pipeline per tasks ===")
        gray_file = task1_rgb_to_grayscale(image_source) #call fungsi task 1
        r_file, g_file, b_file = task2_split_channels(image_source) #call fungsi task 2
        comp_files = task3_jpeg_compression(image_source) #call fungsi task 3
        report_file = task4_generate_compression_report(image_source, comp_files)#call fungsi task 4
        print("=== proses selesai ===")
