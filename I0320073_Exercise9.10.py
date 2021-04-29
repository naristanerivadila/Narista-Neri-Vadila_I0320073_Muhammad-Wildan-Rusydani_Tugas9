print("EXERCISE 9.10")
print()

import array
A = array.array('i', [100,200,300,400,500])
A[1] = -700
A[4] = 800
print(A)

# membalik urutan elemen array
A.reverse()

#nilai akhir (setelah dibalik)
print(A)