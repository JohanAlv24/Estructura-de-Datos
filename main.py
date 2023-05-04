from BFS import BFS
from DFS import DFS
grafo = {
    1: [2, 11],
    2 : [3, 12],
    3 : [2, 4],
    4 : [3, 5],
    5 : [4, 6],
    6 : [5, 7, 14],
    7 : [6, 8],
    8 : [7, 9],
    9 : [8, 10],
    10 : [9, 11],
    11 : [1, 10],
    12 : [2, 13],
    13 : [12, 14],
    14 : [13, 6]
}
BFS = BFS(grafo, 1, 12)
print(BFS.run()+"\n")
#1 2 12
DFS = DFS(grafo, 1, 12)
print(DFS.run()+"\n")
#1 11 10 9 8 7 6 14 13 12


