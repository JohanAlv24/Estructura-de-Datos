from Nodos import nodo
class pila():
    def __init__(self):
        self.primer=None
        self.ultimo=None
        self.size=0
    def empty(self):
        return self.primer==None
    def add(self, dato):
        n = nodo(dato)
        if self.empty:
            self.primer=self.ultimo=n
        else:
            self.ultimo.siguiente = n
            self.ultimo = n
