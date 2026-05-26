from layanan import Layanan
from pelanggan import Pelanggan
from berat import Berat
from jenis_pakaian import JenisPakaian  # Tetap gunakan JenisPakaian yang sama
from rating import Rating  # Impor kelas Rating dari rating.py

class PesananLaundry:
    def __init__(self):
        self.jenis_pakaian_list = []
        self.total_berat = 0

    def tambah_pakaian(self, jenis, berat):
        self.jenis_pakaian_list.append((jenis, berat))
        self.total_berat += berat

    def tampilkan_ringkasan_pakaian(self):
        print("\n=== Daftar Pakaian ===")
        for jenis, berat in self.jenis_pakaian_list:
            print(f"Jenis: {jenis}, Berat: {berat} kg")
        print(f"Total Berat: {self.total_berat} kg")

def pilih_jenis_pakaian():
    print("\nPilih jenis pakaian:")
    jenis_pakaian_options = {
        1: "Woll",
        2: "Sutra",
        3: "Katun",
        4: "Denim",
        5: "Poliester",
        6: "Nilon",
        7: "Linen"
    }
    for key, jenis in jenis_pakaian_options.items():
        print(f"{key}. {jenis}")

    pilihan = int(input("Masukkan pilihan jenis pakaian (1/2/3/...): "))
    if pilihan not in jenis_pakaian_options:
        print("Pilihan tidak valid.")
        return None
    return jenis_pakaian_options[pilihan]

def main():
    print("=== Sistem Pemesanan Laundry ===")

    # 1. Input berat cucian terlebih dahulu
    total_berat = 0
    pesanan = PesananLaundry()

    # 2. Input beberapa jenis pakaian
    while True:
        berat_kg = float(input(f"Masukkan berat cucian (kg): "))
        jenis_pakaian = pilih_jenis_pakaian()
        if jenis_pakaian is None:
            return  # Keluar jika pilihan tidak valid

        pesanan.tambah_pakaian(jenis_pakaian, berat_kg)
        total_berat += berat_kg

        tambah_pakaian_lagi = input("Apakah ingin menambah jenis pakaian lain? (y/n): ").lower()
        if tambah_pakaian_lagi != 'y':
            break

    # 3. Input nama pelanggan setelah berat cucian dan jenis pakaian
    nama_pelanggan = input("Masukkan nama pelanggan: ")
    pelanggan = Pelanggan(nama_pelanggan)

    # 4. Pilih layanan
    print("\nPilih layanan laundry:")
    layanan_options = {
        1: Layanan("Cuci Kering", 5000),
        2: Layanan("Cuci Dan Setrika", 8000),
        3: Layanan("Express", 10000),
    }
    for key, layanan in layanan_options.items():
        print(f"{key}. {layanan.jenis} - Rp {layanan.harga_per_kg}/kg")

    pilihan = int(input("Masukkan pilihan layanan (1/2/3): "))
    if pilihan not in layanan_options:
        print("Pilihan tidak valid.")
        return
    layanan = layanan_options[pilihan]

    # 5. Hitung total harga berdasarkan berat yang sudah ditambahkan
    total_harga = layanan.hitung_harga(pesanan.total_berat)

    # Tampilkan ringkasan
    print("\n=== Ringkasan Pemesanan ===")
    print(pelanggan)
    pesanan.tampilkan_ringkasan_pakaian()
    print(f"Layanan: {layanan.jenis}")
    print(f"Total Harga: Rp {total_harga}")

    # 6. Proses pembayaran
    uang_dibayar = float(input("Masukkan jumlah uang yang dibayarkan: Rp "))
    
    if uang_dibayar < total_harga:
        print("\nUang yang Anda bayarkan kurang dari total harga. Silakan bayar lebih.")
    else:
        kembalian = uang_dibayar - total_harga
        print(f"Jumlah uang yang dibayarkan: Rp {uang_dibayar}")
        print(f"Total harga: Rp {total_harga}")
        print(f"Uang kembalian: Rp {kembalian:.2f}")

    # 7. Tambahkan fitur rating dari pelanggan
    print("\n=== Penilaian Layanan ===")
    print("Berikan rating dari 1 sampai 5 untuk masing-masing kriteria berikut:")
    kualitas = int(input("Kualitas Layanan (1-5): "))
    pelayanan = int(input("Pelayanan Pelanggan (1-5): "))
    harga = int(input("Harga (1-5): "))
    waktu = int(input("Kecepatan Waktu Layanan (1-5): "))

    # Buat objek Rating dan validasi input
    rating = Rating(kualitas, pelayanan, harga, waktu)
    if rating.validasi_rating():
        rata_rata_rating = rating.hitung_rata_rata()
        print(f"\nRata-rata rating untuk layanan Anda adalah: {rata_rata_rating:.2f}/5")
    else:
        print("\nTolong masukkan nilai antara 1 sampai 5 untuk semua kriteria.")

if __name__ == "__main__":
    main()
