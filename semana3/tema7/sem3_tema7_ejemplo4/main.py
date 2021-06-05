"""
Leer dos enteros y determinar:
1. Si alguno de ellos es número primo.
2. El máximo común divisor de ellos.
3. El mínimo común múltiplo de ellos.
4. El dígito con el que comienza cada uno de ellos.
"""

import misFunciones as mf

a = int(input("Entre valor de a"))
b = int(input("Entre valor de b"))
if mf.esPrimo(a):
    print(a, "es primo")
else:
    print (a, "NO es primo")

if mf.esPrimo(b):
    print(b, "es primo")
else:
    print (b, "NO es primo")

mcd = mf.mcd(a,b)
print("El máximo común divisor de", a, " y", b, " es", mcd)
mcm = mf.mcm(a,b)
print("El mínimo común múltiplo de", a, " y", b, " es", mcm)
da = mf.comienzaCon(a)
print("El primer dígito de", a, " es")
db = mf.comienzaCon(b)
print("El primer dígito de", b, " es", db)