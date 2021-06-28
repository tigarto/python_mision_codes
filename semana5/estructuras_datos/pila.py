from vector import vector

class pila(vector):
    def __init__(self, n):
        vector.__init__(self, n)
    
    def apilar(self, d):
        self.agregarDato(d)
        
    def muestraPila(self):
        self.imprimeVector()

    def desapilar(self):
        if self.V[0] == 0:
            print("Pila vacía")
            return None
        d = self.V[self.V[0]]
        self.V[0] = self.V[0] - 1
        return d


st = pila(10)
st.apilar("a")
st.apilar("b")
st.apilar(316)
st.muestraPila()
d = st.desapilar()
print(d)