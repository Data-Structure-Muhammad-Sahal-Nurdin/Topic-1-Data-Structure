from bag import Bag
# Membuat sebuah instance dari Bag
myBag = Bag()
# Operasi add(nilai) digunakan untuk menambahkan nilai-nilai ke bag.
myBag.add(19)
myBag.add(74)
myBag.add(23)
myBag.add(19)
myBag.add(12)
# Operasi length() digunakan untuk mengetahui berapa banyak data dalam bag.
# Operasi ini diakses menggunakan fungsi len().
print('Banyak data di dalam bag:')
print(len(myBag))
# Operasi remove(nilai) digunakan untuk menghapus nilai tertentu dari bag.
myBag.remove(74) # Menghapus nilai 74 dari bag
nilai = int(input("Tebak nilai yang disimpan dalam bag: "))
# Operasi contains() digunakan untuk mengetahui apakah suatu nilai berada dalam
bag.
# Operasi ini diakses dengan operator in.
if nilai in myBag:
print("Bag berisi nilai", nilai)
else:
print("Bag tidak berisi nilai", nilai)
# Operasi iterator() diguankan untuk meng-traverse atau mengiterasi
# semua nilai-nilai dalam bag.
# Operasi ini diakses dengan loop for.
for elm in myBag:
print(elm)