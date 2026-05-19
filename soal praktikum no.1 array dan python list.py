# Program Array dan Python List

# Function menampilkan nilai
def tampilkan_nilai(data):
    print("Daftar Nilai:", data)

# Function menambah nilai
def tambah_nilai(data, nilai_baru):
    print("\nTambah nilai:", nilai_baru)
    data.append(nilai_baru)

    print("Data setelah ditambah:")
    print(data)

# Function menghapus nilai
def hapus_nilai(data, nilai_hapus):
    print("\nHapus nilai:", nilai_hapus)

    if nilai_hapus in data:
        data.remove(nilai_hapus)

        print("Data setelah dihapus:")
        print(data)
    else:
        print("Nilai tidak ditemukan")

# Function menghitung rata-rata
def hitung_rata_rata(data):
    rata = sum(data) / len(data)
    print("\nRata-rata nilai:", rata)

# Function nilai tertinggi dan terendah
def nilai_tertinggi_terendah(data):
    print("Nilai tertinggi:", max(data))
    print("Nilai terendah:", min(data))


# Program Utama

# Menyimpan minimal 5 nilai mahasiswa ke dalam list
nilai_mahasiswa = [70, 80, 90, 75, 85]

# Menampilkan seluruh nilai
tampilkan_nilai(nilai_mahasiswa)

# Menambahkan nilai baru
tambah_nilai(nilai_mahasiswa, 95)

# Menghapus salah satu nilai
hapus_nilai(nilai_mahasiswa, 75)

# Menghitung rata-rata nilai
hitung_rata_rata(nilai_mahasiswa)

# Menampilkan nilai tertinggi dan terendah
nilai_tertinggi_terendah(nilai_mahasiswa)