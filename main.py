from BFS import BFS
from DFBB import DFBB
from DFS import DFS
from ID import ID
grafo = {
    'Amazonas': ['Caquetá', 'Guainía', 'Putumayo', 'Vaupés'],
    'Antioquia': ['Bolívar', 'Boyacá', 'Caldas', 'Cesar', 'Córdoba', 'Chocó', 'Sucre'],
    'Arauca': ['Boyacá', 'Casanare', 'Vichada'],
    'Atlántico': ['Bolívar', 'Magdalena'],
    'Bolívar': ['Antioquia', 'Atlántico', 'Cesar', 'Magdalena', 'Sucre'],
    'Boyacá': ['Antioquia', 'Arauca', 'Casanare', 'Cundinamarca', 'Santander', 'Norte de Santander'],
    'Caldas': ['Antioquia', 'Cundinamarca', 'Risaralda', 'Quindío', 'Tolima'],
    'Caquetá': ['Amazonas', 'Cauca', 'Huila', 'Meta', 'Putumayo'],
    'Casanare': ['Arauca', 'Boyacá', 'Meta', 'Vichada'],
    'Cauca': ['Caquetá', 'Huila', 'Nariño', 'Tolima', 'Valle del Cauca'],
    'Cesar': ['Antioquia', 'Bolívar', 'La Guajira', 'Magdalena', 'Santander'],
    'Chocó': ['Antioquia', 'Risaralda', 'Valle del Cauca'],
    'Córdoba': ['Antioquia', 'Sucre'],
    'Cundinamarca': ['Boyacá', 'Caldas', 'Huila', 'Meta', 'Tolima'],
    'Guainía': ['Amazonas', 'Vaupés', 'Vichada'],
    'Guaviare': ['Caquetá', 'Meta', 'Vaupés'],
    'Huila': ['Caquetá', 'Cauca', 'Cundinamarca', 'Meta', 'Tolima'],
    'La Guajira': ['Cesar', 'Magdalena'],
    'Magdalena': ['Atlántico', 'Bolívar', 'Cesar', 'La Guajira'],
    'Meta': ['Caquetá', 'Casanare', 'Cundinamarca', 'Guaviare', 'Huila', 'Vaupés', 'Vichada'],
    'Nariño': ['Cauca', 'Putumayo'],
    'Norte de Santander': ['Boyacá', 'Cesar', 'Santander'],
    'Putumayo': ['Amazonas', 'Caquetá', 'Nariño'],
    'Quindío': ['Caldas', 'Risaralda', 'Valle del Cauca'],
    'Risaralda': ['Caldas', 'Chocó', 'Quindío', 'Valle del Cauca'],
    'Santander': ['Boyacá', 'Cesar', 'Norte de Santander'],
    'Sucre': ['Antioquia', 'Bolívar', 'Córdoba'],
    'Tolima': ['Caldas', 'Cauca', 'Cundinamarca', 'Huila'],
    'Valle del Cauca': ['Cauca', 'Chocó'],
    'Vichada': ['Arauca', 'Casanare', 'Guainía', 'Meta'],
    'Vaupés': ['Guainía', 'Guaviare']

}
n = ('Antioquia', 'Cundinamarca')
DFBB = DFBB(grafo, n[0], n[1])
print(DFBB.run())
print()
DFS = DFS(grafo, n[0], n[1])
print(DFS.run())
print()
BFS = BFS(grafo, n[0], n[1])
print(BFS.run())




