def menentukan_tahun(TAHUN):
    if TAHUN % 400 == 0:
        return True
    elif TAHUN % 100 == 0:
        return False
    elif TAHUN % 4 == 0:
        return True
    else:
        return False
print("Masukan Tahun:")
TAHUN = int(input())
if menentukan_tahun(TAHUN):
    print(f"Tahun {TAHUN} Merupakan Tahun Kabisat")
else:
    print(f"Tahun {TAHUN} Bukan Tahun Kabisat")