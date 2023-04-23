from Nodos import nodo
class lista():
    def __init__(self):
        self.primer=None
        self.ultimo=None
        self.size=0
    def empty(self):
        return self.primer==None
    def insertprimero(self, dato):
        n = nodo()
        if self.empty():
            self.primer=self.ultimo=n
        else:
            n.siguiente = self.primer
            self.primer = n