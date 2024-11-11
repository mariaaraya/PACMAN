class Grafo:
    def __init__(self, laberinto):
        self.vertices = {}  # Diccionario de vértices
        self.laberinto = laberinto
        self.crear_grafo_laberinto()

    def agregar_vertice(self, valor):
        self.vertices[valor] = []

    def agregar_arista(self, desde, hasta):
        if desde in self.vertices and hasta in self.vertices:
            self.vertices[desde].append(hasta)
            self.vertices[hasta].append(desde)

    def crear_grafo_laberinto(self):
        # Crea los vértices para cada celda libre en el laberinto y agrega aristas entre ellas
        for y, fila in enumerate(self.laberinto):
            for x, celda in enumerate(fila):
                # Definir posiciones específicas que queremos incluir aunque sean paredes
                posiciones_especiales = [(13, 15),( 0, 17),( 27, 17)]
                posicion = (x, y)

                # Agregar vértice si no es pared o si es una posición especial
                if celda != 3 or posicion in posiciones_especiales:
                    self.agregar_vertice(posicion)


                    # Crear aristas para posiciones adyacentes sin paredes o posiciones especiales
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        adyacente = (x + dx, y + dy)
                        if 0 <= adyacente[1] < len(self.laberinto) and \
                                0 <= adyacente[0] < len(self.laberinto[0]) and \
                                (self.laberinto[adyacente[1]][adyacente[0]] != 3 or adyacente in posiciones_especiales):
                            self.agregar_arista(posicion, adyacente)


    def obtener_limites(self):
        max_x = len(self.laberinto[0]) - 1  # Máximo índice de columna
        max_y = len(self.laberinto) - 1  # Máximo índice de fila
        return max_x, max_y
    
    def bfs(self, inicio, objetivo):
        if inicio not in self.vertices or objetivo not in self.vertices:
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
        return []

    def es_posicion_libre(self, x, y):
        # Verifica si la posición (x, y) es libre en el laberinto (es decir, no es una pared)
        if 0 <= y < len(self.laberinto) and 0 <= x < len(self.laberinto[0]):
            return self.laberinto[y][x] != 3  # Asumiendo que 3 representa una pared
        return False