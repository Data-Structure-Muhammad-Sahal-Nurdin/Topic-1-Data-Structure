# banyakTeks = len(input("Masukkan kalimat: "))
# print("Banyak teks adalah ", banyakTeks)

nilaiB = int(input("Masukkan nilai B:"))
nilaiS = int(input("Masukkan nilai S:"))
nilaiI = int(input("Masukkan nilai I:"))
nilaiJ = int(input("Masukkan nilai J:"))
nilaiL1 = int(input("Masukkan nilai L1:"))
nilaiU1 = int(input("Masukkan nilai U1:"))
nilaiL2 = int(input("Masukkan nilai L2:"))
nilaiU2 = int(input("Masukkan nilai U2:"))

# RUMUS ROW MAJOR
rowMajor = nilaiB + (nilaiI - nilaiL1 ) * (nilaiU2 - nilaiL2 + 1) * nilaiS + (nilaiJ-nilaiL2)*nilaiS
print("Maka nilai dari row major adalah: ", rowMajor)

# RUMUS COLUMN MAJOR
columnMajor = nilaiB + (nilaiJ - nilaiL2 ) * (nilaiU1 - nilaiL1 + 1) * nilaiS + (nilaiI-nilaiL1)*nilaiS
print("Maka nilai dari column major adalah: ", columnMajor)
