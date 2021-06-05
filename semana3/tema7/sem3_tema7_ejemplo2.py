"""
Una necesidad frecuente e importante en la vida diaria es conocer el número de combinaciones que se 
pueden construir con n elementos tomados en grupos de a r. Por ejemplo, si se tiene un equipo 
de baloncesto y se dispone de 8 jugadores, se busca determinar cuántas formaciones diferentes se 
pueden hacer. 
"""


''' Funciones '''
def factorial(n):
    f = 1
    for i in range (1, n + 1):
        f = f * i
    return f

''' Programa principal '''

n = int (input("Entre valor de n "))
r = int (input("Entre valor de r "))
fn = factorial(n)
fr = factorial(r)
fnr = factorial(n - r)
nc = fn // fr // fnr
print("n =", n, " r =", r)
print("Factorial de n =", fn) 
print("Factorial de r =", fr)
print("Factorial de n - r =", fnr)
print("Número de combinaciones =", nc)