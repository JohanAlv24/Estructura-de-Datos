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
        if self.empty():
            self.primer=self.ultimo=n
        elif self.primer==self.ultimo:
            self.primer.siguiente=n
            self.ultimo = n
        else:
            self.ultimo.siguiente = n
            self.ultimo = n
    def pop(self):
        if self.empty():
            print("No es posible eliminar de una pila vacía")
        elif self.primer==self.ultimo:
            self.primer=self.ultimo=None
        else:
            aux = self.primer
            while aux.siguiente!=self.ultimo:
                aux=aux.siguiente
            self.ultimo = aux
            self.ultimo.siguiente = None
    def show(self):
        aux = self.primer
        while aux!=None:
            print(aux.dato, end=" ")
            aux = aux.siguiente
    
