#title : Criptografi-RSA

print("++++++ Criptografi RSA ++++++++++")

plaintex = input("masukan simbol = ") 
p = int(input("masukan nilai p = "))
q = int(input("masukan nilai q = "))
key = int(input("masukan key = "))

n = p*q

teta = (p-1)*(q-1)

# Mengonversi simbol ke nilai ASCII
nilai_ascii = ord(plaintex)

#output
print(f"Plaintex : {plaintex}\nNilai n = {n}")