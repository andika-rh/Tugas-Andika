import csv
Nama_file= 'tugas.csv'
datalist = []

def listdata():
    with open(Nama_file,'r', newline='') as csvfile:
        baca = csv.reader(csvfile)
        for baris in baca:
            datalist.append(baris)

def bacadata():
    with open(Nama_file,'r',newline='') as csvfile:
        baca = csv.reader(csvfile)
        for baris in baca:
            print(baris)

def tambahdata():
    Tanggal = input("Masukkan Tanggal : ")
    Nama = input("Masukkan Nama : ")
    Kendaraan = input("Masukkan Kendaraan: ")
    Pembayaran = int(input("Masukkan Pembayaran : "))
    Denda = int(input("Masukkan Denda : "))
    Total = Pembayaran + Denda
    print("Total :",(Total))
    with open(Nama_file, 'a', newline='') as csvfile:
        tulis = csv.writer(csvfile, delimiter=',')
        tulis.writerow([Tanggal, Nama, Kendaraan, Pembayaran, Denda, Total])

def hapusdata(inputan):
    datalist.remove(datalist[inputan])
    with open(Nama_file, 'w', newline='') as csvfile:
        tulis_ulang = csv.writer(csvfile, delimiter=',')
        tulis_ulang.writerows(datalist)

def menu():
    print('''
    1. Baca Data
    2. Tambah Data
    3. Hapus Data
    ''')
    return int(input("Masukan Pilihan: "))

if __name__ == "__main__":
    listdata()

    pilih = menu()

    if pilih == 1:
        bacadata()
    
    elif pilih == 2:
        tambahdata()
        print("Data Berhasil ditambahkan")

    elif pilih == 3:
        inputan = int(input("Masukkan indeks yang akan dihapus : "))
        print("",format(datalist[inputan]))
        hapusdata(inputan)
        print("Data Berhasil dihapus")










