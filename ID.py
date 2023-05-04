from DFS import DFS
class ID(DFS):
    def __init__(self, grafo, base, meta, cota):
        super().__init__(grafo, base, meta)
        self.cota = cota
    def expand(self):
        n = self.pila.pop()
        val = False
        try:
            if self.nivel(n)<self.cota:
                val = self.agenda(n)
        except:
            val = self.agenda(n)
        return val
    def agenda(self, n):
        val = False
        if n[0] not in self.expandidos:
            self.expandidos[n[0]] = n[1]
            for a in self.grafo[n[0]]:
                self.pila.add((a, n[0]))
                if a==self.meta:
                    val=True
                    break
        return val
    def nivel(self, t):
        a = self.expandidos[t[1]]
        n=1
        while a!=self.expandidos[a]:
            n+=1
            a = self.expandidos[a]
        return n
