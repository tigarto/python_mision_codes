"""
Una necesidad frecuente e importante en la vida diaria es conocer el número de combinaciones que se 
pueden construir con n elementos tomados en grupos de a r. Por ejemplo, si se tiene un equipo 
de baloncesto y se dispone de 8 jugadores, se busca determinar cuántas formaciones diferentes se 
pueden hacer. 
"""
import misfunciones as mf

''' Programa principal '''

n = int (input("Entre valor de n "))
r = int (input("Entre valor de r "))
fn = mf.factorial(n)
fr = mf.factorial(r)
fnr = mf.factorial(n - r)
nc = fn // fr // fnr
print("n =", n, " r =", r)
print("Factorial de n =", fn) 
print("Factorial de r =", fr)
print("Factorial de n - r =", fnr)
print("Número de combinaciones =", nc)