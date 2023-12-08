saldo = 100000

while True:
    print("Pilih Jenis Jasa Antar :")
    print("1. Customer")
    print("2. Barang")
    print("3. Makanan")
    print("4. Keluar")

    pilihan = int(input("Pilih Jenis Jasa: "))

    if pilihan == 4:
        print("Terima Kasih Sudah Menggunakan jasa Antar Kami!!")
        break

    jarak = float(input("Masukan Jarak Lokasi Tujuan/km: "))

    if pilihan == 1:
        harga = 2000
    elif pilihan == 2:
        harga = 3000
    elif pilihan == 3:
        harga = 3500
    else:
        print("PILIHAN JASA TIDAK TERSEDIA")
        continue

    totalbayar = jarak * harga

    print("Biaya Yang Harus di Bayar :", totalbayar)
    print("Pilih cara pembayaran:")
    print("1. Saldo")
    print("2. Cash")

    pembayaran = int(input("Masukkan pilihan pembayaran (1-2): "))

    if pembayaran == 1:
        if totalbayar > saldo:
            print("Saldo tidak cukup.")
            print("Silahkan pilih metode pembayaran cash")
        else:
            saldo -= totalbayar
            print(f"Transaksi berhasil. Saldo Anda sekarang:", saldo,  "rupiah.")
    elif pembayaran == 2:
        print("Silahkan lakukan pembayaran ke driver sesuai nominal pembayaran")
    else:
        print("PILIHAN PEMBAYARAN TIDAK TERSEDIA")
        print("Silahkan lakukan pembayaran secara cash ke driver sesuai nominal pembayaran")