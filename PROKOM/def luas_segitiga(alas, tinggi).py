def faktorial_uns(n):
    if n == 0:
        return 1
    else:
        return n * faktorial_uns(n-1)

nilai = int(input("masukkan nilai untuk faktorial = "))

print("nilai faktorial dari ", nilai, "adalah :", faktorial_uns(nilai))

