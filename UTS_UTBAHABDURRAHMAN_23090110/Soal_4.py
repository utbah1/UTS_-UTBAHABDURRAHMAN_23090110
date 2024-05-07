def kalkulator_bmi(berat, tinggi):
    bmi = berat / (tinggi ** 2)
    if bmi < 18.5:
        rekomendasi = "Berat badan kurang"
    elif 18.5 <= bmi < 24.9:
        rekomendasi = "Berat badan normal"
    elif 25 <= bmi < 29.9:
        rekomendasi = "Kelebihan berat badan"
    else:
        rekomendasi = "Obesitas"
    return bmi, rekomendasi

def main():
    print("Masukkan Berat Badan (Kg): ")
    berat= float(input())
    print("Masukkan Tinggi Badan (M): ")
    tinggi = float(input())

    bmi, rekomendasi = kalkulator_bmi(berat, tinggi)

    print(f"Berat Badan : {berat} Kg")
    print(f"Tinggi Badan : {tinggi} M")
    print(f"Nilai BMI Anda : {bmi:.2f}")
    print(f"Kategori BMI : {rekomendasi}")

if __name__ == "__main__":
    main()