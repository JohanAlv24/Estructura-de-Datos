import sys
sys.path.append('Estructuras')
sys.path.append('Búsquedas en Profundidad')
from cola import cola
from DFS import DFS
class BFS(DFS):
    def __init__(self, grafo, base, meta):
        super().__init__(grafo, base, meta)
        self.pila = cola()

    
