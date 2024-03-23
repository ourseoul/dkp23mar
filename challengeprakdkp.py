def cari_nilai_terbesar(array):
    if len(array) == 0:
        return None  # Mengembalikan None jika array kosong
    nilai_terbesar = array[0]  # Menginisialisasi nilai terbesar dengan elemen pertama dari array
    for nilai in array:
        if nilai > nilai_terbesar:
            nilai_terbesar = nilai
    return nilai_terbesar

def cari_nilai_terkecil(array):
    if len(array) == 0:
        return None  # Mengembalikan None jika array kosong
    nilai_terkecil = array[0]  # Menginisialisasi nilai terkecil dengan elemen pertama dari array
    for nilai in array:
        if nilai < nilai_terkecil:
            nilai_terkecil = nilai
    return nilai_terkecil

# Contoh penggunaan program
if __name__ == "__main__":
    # Masukkan nilai-nilai integer ke dalam array
    nilai_array = [int(x) for x in input("Masukkan nilai-nilai integer, pisahkan dengan spasi: ").split()]
    
    # Urutkan array dari terkecil ke terbesar
    nilai_array.sort()
    
    # Panggil fungsi untuk mencari nilai terbesar dan terkecil
    terkecil = cari_nilai_terkecil(nilai_array)
    terbesar = cari_nilai_terbesar(nilai_array)
    
    if terkecil is not None and terbesar is not None:
        print("Urutan dari terkecil ke terbesar:", nilai_array)
        print("Urutan dari terbesar ke terkecil:", nilai_array[::-1])
        print("Nilai terkecil dalam array adalah:", terkecil)
        print("Nilai terbesar dalam array adalah:", terbesar)
    else:
        print("Array kosong")
