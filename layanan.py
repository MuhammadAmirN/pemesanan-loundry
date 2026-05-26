class Layanan:
    def __init__(self, jenis, harga_per_kg):
        self.jenis = jenis
        self.harga_per_kg = harga_per_kg

    def hitung_harga(self, berat):
        return self.harga_per_kg * berat

    def __str__(self):
        return f"Layanan: {self.jenis} - Harga per kg: Rp {self.harga_per_kg}"
