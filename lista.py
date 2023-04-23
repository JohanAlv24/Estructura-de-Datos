from Nodos import nodo
class lista():
    def __init__(self):
        self.primer=None
        self.ultimo=None
        self.size=0
    def empty(self):
        return self.primer==None
    def insertprimero(self, dato):
        n = nodo(dato)
        if self.empty():
            self.primer=self.ultimo=n
        else:
            n.siguiente = self.primer
            self.primer = n
    def eliminar(self):
        if self.empty():
            print("No es posible eliminar de una lista vacía")
    def srec(self, n):
        aux = n
        if aux!=None:
            print(aux.dato, end=" ")
            self.srec(aux.siguiente)
    def show(self):
        self.srec(self.primer)