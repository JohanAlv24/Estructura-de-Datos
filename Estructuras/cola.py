from Nodos import nodo
class cola():
    def __init__(self):
        self.primer = None
        self.ultimo = None
        self.size = 0
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
            a="Cola vacía"
        elif self.primer==self.ultimo:
            a = self.primer.dato
            self.primer=self.ultimo=None
        else:
            a = self.primer.dato
            self.primer = self.primer.siguiente   
        return a
    def show(self):
        aux = self.primer
        while aux!=None:
            print(aux.dato, end=" ")
            aux = aux.siguiente