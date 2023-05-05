from ID import ID
from DFS import DFS
class DFBB(DFS):
    def __init__(self, grafo, base, meta):
        super().__init__(grafo, base, meta)
    def run(self):
        t=DFS(self.grafo, self.base, self.meta).run()
        cota = len(t.split(' '))-1
        while True:
            try:
                t=ID(self.grafo, self.base, self.meta, cota).run()
                cota -=1
            except:
                break
        return t
