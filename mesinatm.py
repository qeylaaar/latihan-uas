saldo = 1000000

while (True):
    print ("Menu: \n 1. Setor \n 2. Tarik")
    transaksi = int(input("Masukan pilihan anda: "))
    if transaksi == 1:
        print("ANDA INGIN MELAKUKAN SETOR")
        setor = int(input("Masukan jumlah setor: "))
        saldo = saldo + setor
    elif transaksi == 2:
        print("ANDA INGIN MELAKUKAN TARIK")
        tarik = int(input("Masukan jumlah tarik: "))
        if saldo >= tarik:
            saldo = saldo - tarik
        else:
            print("Saldo anda tidak mencukupi jumlah penarikan")   
             
    print("Jumlah saldo anda saat ini ", saldo)

    print("Kemballi ke menu: \n 1. Ya \n 2. Tidak")
    lagi = int(input("Pilihan: "))
    if lagi != 1 :
        break
print("JUMLAH SALDO ", saldo)