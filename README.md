# 🧺 Sistem Pemesanan Laundry - Kasir Java (GUI & CLI)

Aplikasi manajemen kasir dan sistem pemesanan laundry berbasis bahasa pemrograman **Java**. Proyek ini mendukung antarmuka berbasis grafis (**GUI Swing**) serta interaksi terminal (**CLI**) untuk memproses transaksi laundry mulai dari pemilihan jenis bahan pakaian, berat cucian, penentuan paket layanan, hingga kalkulasi pembayaran kembalian secara otomatis.

---

## 📁 Struktur Repositori & Folder

Berdasarkan arsitektur proyek pada folder `src/uas`, berikut adalah pemetaan file yang tersedia:

```text
📂 Kasir_Java/
│
└── 📂 src/
    └── 📂 uas/
        ├── 📄 Koneksi.java        # Driver & konfigurasi koneksi ke Database (MySQL/SQLite)
        │
        ├── 📄 kasir.java          # Logika utama aplikasi / Backend proses transaksi
        ├── 📄 kasir.form          # Layout UI komponen Swing untuk halaman kasir utama
        │
        ├── 📄 previewkasir.java   # Logika komponen tampilan nota / ringkasan transaksi
        └── 📄 previewkasir.form   # Layout UI komponen Swing untuk halaman preview nota
