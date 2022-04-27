import random
import datetime
from customer import Customer

atm = Customer(id)

while True:

    id = int(input("Masukan Pin Anda :"))
    trial = 0

    while (id != int(atm.checkPin()) and trial < 3):
        id = int(input("Pin anda salah. Silahkan Masukan Lagi : "))
        trial += 1

        if trial == 3:
            print("Error. Silahkan ambil kartu dan coba lagi..")
            exit()

    while True:
        print("Selamat Datang di ATM Progate..")
        print("\n 1 - Cek Saldo \n 2 - Debet \n 3 - Simpan \n 4 - Ganti Pin \n 5 - Keluar ")
        selectmenu = int(input("\nSilahkan pilih menu: "))

        if selectmenu == 1:
            print("\nSaldo anda sekarang: Rp." + str(atm.checkBalance()) + "\n")

        elif selectmenu == 2:
                nominal = float(input("Masukan nominal saldo: "))
                verify_withdraw = input("Konfirmasi: Anda akan melakukan debet dengan nominal berikut" +" "+str(nominal) + "? y/n" +" ")

                if verify_withdraw == "y":
                    print("Saldo awal anda adalah: Rp. " + str(atm.checkBalance()) + " ")
                else:
                    break
                if nominal < atm.checkBalance():
                    atm.withdrawBalance(nominal)
                    print("Transaksi Debet Berhasil!")
                    print("Saldo sisa sekarang: Rp. " + str(atm.checkBalance()) + "")
                else:
                    print("Maaf, Saldo anda tidak cukup untuk melakukan debet")
                    print("Silahkan lakukan penambahan nominal saldo")

        elif selectmenu == 3:
                 nominal = float(input("Masukan nominal saldo:"))
                 verify_deposit = input("Konfirmasi: Anda akan melakukan penyimpanan dengan nominal berikut"+" "+ str(nominal) + "? y/n" +" ")
                 
                 if verify_deposit == "y":
                     atm.depositBalance(nominal)
                     print("Saldo anda sekarang adalah: Rp." + str(atm.checkBalance()) + "\n")
                 else:
                     break
                
        elif selectmenu == 4:
            verify_pin = int(input("Masukan pin anda: "))

            while verify_pin != int(atm.checkPin()):
                print("Pin anda salah, silahkan masukan pin:")
            
            update_pin = int(input("silahkan masukan pin baru:"))
            print("pin anda berhasil diganti")

            verify_newpin = int(input("coba masukan pin baru: "))

            if verify_newpin == update_pin:
                print("pin baru anda sukses!")
            else:
                print("maaf, pin anda salah!")


        elif selectmenu == 5:
            print("========================================")
            print("Resi tercetak otomatis saat anda keluar.\n")
            print("Harap simpan tanda terima ini \n")
            print("sebagai bukti transaksi anda.")
            print("\nNo. Rekord:", random.randint(100000, 1000000))
            print("Tanggal: ", datetime.datetime.now())
            print("Saldo Akhir: ", atm.checkBalance())
            print("\nTerima kasih telah menggunakan ATM Progate!")
            print("========================================")
            exit()
        
        else:
            print("Error. Maaf menu anda tidak tersedia")
