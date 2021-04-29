print("EXERCISE 9.7")
print()

import array

#mengonversi string ke dalam array.array
B = array.array('B')
B.fromstring("Python")

for karakter in B:
    print("%c " % karakter, end='')
