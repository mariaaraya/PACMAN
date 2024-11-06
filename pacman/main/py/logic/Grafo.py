class Grafo:
    def __init__(self, laberinto):
        self.vertices = {}  # Diccionario de vértices
        self.laberinto = laberinto
        self.crear_grafo_laberinto()

    def agregar_vertice(self, valor):
        self.vertices[valor] = []

    def agregar_arista(self, desde, hasta):
        if desde in self.vertices and hasta in self.vertices:
            self.vertices[desde].append(hasta)  # Cambié 'todestino' a 'hasta'
            self.vertices[hasta].append(desde)

    def crear_grafo_laberinto(self):
        # Crea los vértices para cada celda libre en el laberinto y agrega aristas entre ellas
        for y, fila in enumerate(self.laberinto):
            for x, celda in enumerate(fila):
                # Definir posiciones específicas que queremos incluir aunque sean paredes
                posiciones_especiales = [(13, 15)]
                posicion = (x, y)

                # Agregar vértice si no es pared o si es una posición especial
                if celda != 3 or posicion in posiciones_especiales:
                    self.agregar_vertice(posicion)
                    if posicion in posiciones_especiales:
                        print(f"Nodo {posicion} añadido al grafo como posición especial.")

                    # Crear aristas para posiciones adyacentes sin paredes o posiciones especiales
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        adyacente = (x + dx, y + dy)
                        if 0 <= adyacente[1] < len(self.laberinto) and \
                                0 <= adyacente[0] < len(self.laberinto[0]) and \
                                (self.laberinto[adyacente[1]][adyacente[0]] != 3 or adyacente in posiciones_especiales):
                            self.agregar_arista(posicion, adyacente)
                            if posicion in posiciones_especiales:
                                print(f"Arista añadida entre {posicion} y {adyacente}")

    def bfs(self, inicio, objetivo):
        if inicio not in self.vertices or objetivo not in self.vertices:
            print(f"Uno de los puntos {inicio} o {objetivo} no está en el grafo.")
            return []

        visitados = {inicio}
        cola = [(inicio, [inicio])]

        while cola:
            actual, camino = cola.pop(0)
            if actual == objetivo:
                return camino

            for vecino in self.vertices[actual]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append((vecino, camino + [vecino]))
        print(f"No se encontró un camino entre {inicio} y {objetivo}.")
        return []