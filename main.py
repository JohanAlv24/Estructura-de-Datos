from ABC import ABC
grafo = {
    'Argentina': ['Bolivia', 'Brasil', 'Chile', 'Paraguay', 'Uruguay'],
    'Bolivia': ['Argentina', 'Brasil', 'Chile', 'Paraguay', 'Perú'],
    'Brasil': ['Argentina', 'Bolivia', 'Colombia', 'Guyana', 'Paraguay', 'Perú', 'Surinam', 'Uruguay', 'Venezuela'],
    'Colombia': ['Venezuela', 'Ecuador', 'Panamá', 'Brasil', 'Perú'],
    'Chile': ['Argentina', 'Bolivia', 'Perú'],
    'Ecuador': ['Colombia', 'Perú'],
    'Guyana': ['Surinam', 'Venezuela', 'Brasil'],
    'Paraguay': ['Argentina', 'Bolivia', 'Brasil'],
    'Perú': ['Bolivia', 'Brasil', 'Chile', 'Colombia', 'Ecuador'],
    'Surinam': ['Brasil', 'Guyana'],
    'Uruguay': ['Argentina', 'Brasil'],
    'Venezuela': ['Brasil', 'Colombia', 'Guyana']

}
ABC = ABC(grafo, "Guyana", "Chile")
print(ABC.DFS())


'''
geographic_graph = {
    'Lima': {'Santiago': 2496, 'Buenos Aires': 3909, 'Bogotá': 1554},
    'Santiago': {'Lima': 2496, 'Buenos Aires': 1400},
    'Buenos Aires': {'Lima': 3909, 'Santiago': 1400, 'São Paulo': 2063},
    'Bogotá': {'Lima': 1554, 'Quito': 976, 'Caracas': 1069},
    'Quito': {'Bogotá': 976, 'Lima': 1318},
    'Caracas': {'Bogotá': 1069, 'Buenos Aires': 3923},
    'São Paulo': {'Buenos Aires': 2063, 'Rio de Janeiro': 357},
    'Rio de Janeiro': {'São Paulo': 357}
}

'''