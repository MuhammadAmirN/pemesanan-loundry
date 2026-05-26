class JenisPakaian:
    def __init__(self, jenis):
        self.jenis = jenis

    def __str__(self):
        return f"Jenis Pakaian: {self.jenis}"

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
    return JenisPakaian(jenis_pakaian_options[pilihan])
