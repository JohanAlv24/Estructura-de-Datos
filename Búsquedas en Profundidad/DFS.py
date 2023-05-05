import sys
sys.path.append('Estructuras')
from pila import pila
class DFS():
    def __init__(self, grafo, base, meta):
        self.base = base
        self.meta = meta
        self.grafo = grafo
        self.pila = pila()
        self.expandidos = dict()
    def run(self):
        if self.base==self.meta:
            return self.base
        else:
            self.pila.add((self.base, self.base))
            val = False
            while val==False:
                val = self.expand()
            return self.trayec(self.pila.ultimo.dato)
    def expand(self):
        val = False
        n = self.pila.pop()
        if n[0] not in self.expandidos:
            self.expandidos[n[0]] = n[1]
            for a in self.grafo[n[0]]:
                self.pila.add((a, n[0]))
                if a==self.meta:
                    val=True
                    break
        return val
    def trayec(self, n):
        t = str(n[0])+"-"
        x = n[1]
        while x!=self.expandidos[x]:
            t+=str(x)+"-"
            x = self.expandidos[x]
        t+=str(x)
        return self.reverse(t)
    def reverse(self, s):
        s = s.split('-')
        x=''
        for i in range(len(s)-1, -1, -1):
            if i==0:
                x+=s[i]
            else:
                x+=s[i]+"-"
        return x