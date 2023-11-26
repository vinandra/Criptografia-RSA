#title : Criptografi-RSA

print("++++++ Criptografi RSA ++++++++++")

plaintex = input("masukan simbol = ") 
p = int(input("masukan nilai p (bilangan prima)= "))
q = int(input("masukan nilai q (bilangan prima)= "))
e = int(input("masukan kunci umum (bilangan yang lebih prima)= "))

n = p*q

teta = (p-1)*(q-1)

nilai_ascii = ord(plaintex)

binary_representation = bin(nilai_ascii)[2:]

for k in range(1, 100):
    d = (1 + k * teta) / e
    if d.is_integer():
        print(f"Nilai d yang memenuhi kondisi untuk k = {k}: {int(d)}")
        break

c = pow(nilai_ascii, e, teta)

ascii_symbol = chr(c)

#output
print("\n++++++ Answer ++++++")
print(f"Plaintext {plaintex}, Biner = {binary_representation}, Decimal = {nilai_ascii}")
print(f"Nilai n = {n}, Nilai teta = {teta}")
print(f"chiper  = {c}, uabh menjadi simbol => {ascii_symbol}")