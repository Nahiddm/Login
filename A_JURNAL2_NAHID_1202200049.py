print("===SELAMAT DATANG DI PROGRAM BUTIK===")
print(" 1.KAOS\n 2.KEMEJA\n 3.JAS\n 4.SELESAI\n")
kaos = 0
kemeja = 0
jas = 0
status = True
while status == True :
    barang = input("Masukkan Barang Yang Ingin Dibeli (1/2/3/4) :")
    total_barang = 0
    if barang == "1" or barang == "kaos" or barang == "Kaos" :
        kaos = kaos + 25000
        print("Kaos Ditambahkan")
    elif barang == "2" or barang == "kemeja" or barang == "Kemeja":
        kemeja = kemeja + 50000
        print("Kemeja Ditambahkan")
    elif barang == "3" or barang == "jas" or barang == "Jas":
        jas = jas + 100000
        print("Jas Ditambahkan")
    else :
        status = False
    total_barang = kaos + kemeja + jas
print("Total :",total_barang)