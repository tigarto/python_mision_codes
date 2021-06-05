"""
Una necesidad frecuente e importante en la vida diaria es conocer el número de combinaciones que se 
pueden construir con n elementos tomados en grupos de a r. Por ejemplo, si se tiene un equipo 
de baloncesto y se dispone de 8 jugadores, se busca determinar cuántas formaciones diferentes se 
pueden hacer. 
"""

''' Programa principal '''

n = int(input("Entre valor de n "))
r = int(input("Entre valor de r "))

fn = 1
for i in range(1, n + 1):
    fn = fn * i
    fr = 1

for i in range(1, r + 1):
    fr = fr * i
    fnr = 1

for i in range(1, n - r + 1):
    fnr = fnr * i
    nc = fn // fr // fnr

print("n =", n, " r =", r)
print("Factorial de n =", fn) 
print("Factorial de r =", fr)
print("Factorial de n - r =", fnr)
print("Número de combinaciones =", nc)