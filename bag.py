# Class Bag adalah implementasi dari ADT Bag
class Bag:
    # Constructor ADT Bag.
    # Mendefinisikan field _isi berupa list untuk menyimpan
    # nilai-nilai dalam bag.
    def __init__(self):
        self._isi = list()


    # Method length() mengembalikan banyaknya data dalam bag.
    # Method ini diakses dengan fungsi built-in len()
    def __len__(self):
        return len(self._isi)


    # Method contains(nilai) mencari apakah suatu nilai terdapat dalam bag.
    # Method ini mengembalikan True jika nilai terdapat dalam bag
    # dan False jika nilai tidak terdapat dalam bag.
    # Method ini diakses dengan operator in.
    def __contains__(self, nilai):
        return nilai in self._isi


    # Method add() digunakan untuk menambahkan nilai data ke bag.
    # Method ini tidak mengembalikan nilai.
    def add(self, nilai):
        self._isi.append(nilai)


    # Method remove() digunakan untuk menghapus suatu nilai dalam bag.
    # Jika nilai yang ingin dihapus tidak ada di dalam bag, method ini
    # meng-raise eksepsi ValueError. Jika nilai yang ingin dihapus
    # ada di dalam bag, method ini menghapus salah satu nilai (jika terdapat lebih
    # dari satu nilai.)
    # Method ini mengembalikan nilai yang dihapus.
    def remove(self, nilai):
        if nilai not in self._isi:
            raise ValueError('Nilai tidak ada di bag.')
        else:
            index = self._isi.index(nilai)
            return self._isi.pop(index)
    # Method iterator() digunakan untuk meng-traverse atau meng-iterasi setiap nilai


    # dalam bag. Method iterator() mengembalikan class iterator.
    def __iter__(self):
        return _BagIterator(self._isi)


    # Class _BagIterator adalah class iterator untuk membuat sebuah object
    # dapat diiterasi.
class _BagIterator:
    # Constructor
    # Field 1: struktur data yang diiterasi
    # Field 2: variabel indeks loop
    def __init__(self, isi):
        self._isiBag = isi
        self._curIndeks = 0


    # Method __iter__ mengembalikan object dari class iterator.
    def __iter__(self):
        return self
    # Method _next_ mengembalikan nilai dari elemen dengan indeks
    # variabel indeks loop dan menginkrementasi variabel indeks loop
    def __next__(self):
        if self._curIndeks < len(self._isiBag):
            item = self._isiBag[self._curIndeks]
            self._curIndeks += 1
            return item
        else:
            raise StopIteration
