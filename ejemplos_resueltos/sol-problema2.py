"""
Un color balanceado es aquel cuyos valores rojo (red), verde (gree) y azul (blue) suman 1.0. Escriba
una funcion llamada ìs_balanced que tome un diccionario cuyas claves (keys) son 'R', 'G', y 'B'
y cuyos valores (values) estan entre 0 y 1 y retorne True si estos representan un color balancedo.
"""

def ìs_balanced1(color):
    sumaColores = 0
    for c in color:
        sumaColores += color[c]
    if sumaColores == 1.0:
        return True
    else:
        return False

def ìs_balanced2(color):
    sumaColores = 0
    for p in color.values():
        sumaColores += p
    if sumaColores == 1.0:
        return True
    else:
        return False

def ìs_balanced3(color):
    sumaColores = sum(color.values())
    if sumaColores == 1.0:
        return True
    else:
        return False

""" Test de las funciones """
colorTest1 = {'R': 0.3, 'G': 0.2, 'B': 0.5}
print(colorTest1)
print(ìs_balanced1(colorTest1))
print(ìs_balanced2(colorTest1))
print(ìs_balanced3(colorTest1))


colorTest2 = {'R': 0.2, 'G': 0.2, 'B': 0.5}
print(colorTest2)
print(ìs_balanced1(colorTest2))
print(ìs_balanced2(colorTest2))
print(ìs_balanced3(colorTest2))