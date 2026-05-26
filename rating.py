class Rating:
    def __init__(self, kualitas, pelayanan, harga, waktu):
        self.kualitas = kualitas
        self.pelayanan = pelayanan
        self.harga = harga
        self.waktu = waktu

    def validasi_rating(self):
        # Memvalidasi apakah semua nilai rating antara 1 hingga 5
        return all(1 <= nilai <= 5 for nilai in [self.kualitas, self.pelayanan, self.harga, self.waktu])

    def hitung_rata_rata(self):
        # Menghitung rata-rata dari semua penilaian yang diberikan
        total = self.kualitas + self.pelayanan + self.harga + self.waktu
        rata_rata = total / 4
        return rata_rata
