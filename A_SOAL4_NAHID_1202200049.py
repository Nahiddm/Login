jumlah_barang=int(input("Masukkan Jumlah Barang : "))
total_harga=0
diskon=0
for i in range (jumlah_barang):
    harga_barang=int(input("Masukkan Harga Barang: "))
    total_harga= total_harga+harga_barang
print("Total Harga sebelum diskon:",total_harga)
if total_harga > 75000:
    diskon = (total_harga * 20)/100
total_bayar = total_harga - diskon
print("Total yang belanjaan yang harus dibayar Rp.",total_bayar)