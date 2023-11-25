#title : Criptografi-RSA

print("++++++ Criptografi RSA ++++++++++")

plaintex = input("masukan simbol = ") 
p = int(input("masukan nilai p (bilangan prima)= "))
q = int(input("masukan nilai q (bilangan prima)= "))
e = int(input("masukan kunci umum (bilangan yang lebih prima)= "))

n = p*q

teta = (p-1)*(q-1)

nilai_ascii = ord(plaintex)

for k in range(1, 100):
    d = (1 + k * teta) / 19
    if d.is_integer():
        print(f"Nilai d yang memenuhi kondisi untuk k = {k}: {int(d)}")
        break

#output
print(f"Plaintex : {plaintex}\nNilai n = {n}")