from BFS import BFS
class BD(BFS):
    def __init__(self, grafo, meta, base):
        super().__init__(grafo, meta, base)
        self.pila = cola()
    def run(self):
        t=''
        while t[:t.find('-')]!=self.base or t[t.rfind('-'):]!=self.meta:
            self

