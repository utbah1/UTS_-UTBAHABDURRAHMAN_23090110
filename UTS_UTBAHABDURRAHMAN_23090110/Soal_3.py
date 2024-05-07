def total_harga():
    jumlah_barang = int(input("Masukkan Jumlah Barang: "))
    total = 0
    for i in range(1, jumlah_barang + 1):
        harga = int(input(f"Masukkan Harga Barang Ke-{i}: "))
        total += harga
    print(f"Total Belanjaan Rp.{total}")
total_harga()