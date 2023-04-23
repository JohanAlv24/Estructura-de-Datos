class nodo():
    def __init__(self, dato, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente
    def __str__(self):
        return self.dato