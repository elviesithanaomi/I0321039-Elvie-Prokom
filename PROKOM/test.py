matriksA = [[1,2,5], [3,4,9], [6,7,2]]
matriksB = [[5,8,7], [2,4,1], [8,4,1]]
matriksC = []

print("mulai mengali dua matriks: ")
for x in range(0, len(matriksA)):
    print()
    baris = []
    for y in range(0, len(matriksA[0])):
        total=0;
        for z in range(0, len(matriksA)):
            total = total + (matriksA [x][y] * matriksB[z][y])
#menghasilkan baris
for x in range(0, len(matriksA)):
    print( )
#menghasilkan kolom
for y in range(0, len(matriksA[0])):
    print(matriksA [x] [y] + matriksB[x] [y], end=' ')
print( )