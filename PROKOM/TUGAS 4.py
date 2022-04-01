totalbelanja = int(input("berapa nilai pembelian anda? ="))
membership = input("membership? yes or no: " )

if membership == ("yes"):
    if totalbelanja >= 500000:
        print("selamat anda mendapatkan discount 25%")
        potongan = totalbelanja * 25/100
        totalbayar = totalbelanja - potongan
    print("total pembayaran kamu setelah discount", totalbayar)
    if totalbelanja >= 100000:
        print("selamat anda mendapatkan discount 20%")
        potongan = totalbelanja * 20/100
        totalbayar = totalbelanja - potongan
    print("total pembayaran kamu setelah discount", totalbayar)
    if totalbelanja < 100000:
        potongan = totalbelanja * 10/100
        totalbayar = totalbelanja - potongan
    print("total pembayaran kamu setelah discount", totalbayar)
    
    
if membership == ("no"):
    if totalbelanja >= 100000:
        print("selamat anda mendapatkan discount 10%")
        potongan = totalbelanja * 10/100
        totalbayar = totalbelanja - potongan
    else:
        totalbayar = totalbelanja
    print("total pembayaran kamu setelah discount", totalbayar)

