from lsl import LSL

class pila(LSL):
     def __init__(self):
         LSL.__init__(self)
         
     def apilar(self, d):
         self.insertar(d)

     def muestraPila(self):
         self.recorrerLista()

     def desapilar(self):
         p = self.primerNodo()
         d = p.retornarDato()
         self.borrar(p)
         return d

a = pila()
a.apilar("a")
a.apilar("e")
a.apilar("i")
a.apilar("o")
a.recorrerLista()
b = a.esVacia()
print("\n Está vacía?", b)
d = a.desapilar()
print("\ndato desapilado", d)
a.recorrerLista()