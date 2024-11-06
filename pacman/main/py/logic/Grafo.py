import heapq  # Usado para implementar la cola de prioridad

class Grafo:
    def __init__(self, laberinto):
        self.vertices = {}  # Diccionario de vértices
        self.laberinto = laberinto
        self.crear_grafo_laberinto()

    def agregar_vertice(self, valor):
        self.vertices[valor] = []

    def agregar_arista(self, desde, hasta, peso=1):  # Peso por defecto 1
        if desde in self.vertices and hasta in self.vertices:
            self.vertices[desde].append((hasta, peso))
            self.vertices[hasta].append((desde, peso))

    def crear_grafo_laberinto(self):
        for y, fila in enumerate(self.laberinto):
            for x, celda in enumerate(fila):
                if celda != 3:  # No es una pared
                    posicion = (x, y)
                    self.agregar_vertice(posicion)
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        adyacente = (x + dx, y + dy)
                        if 0 <= adyacente[1] < len(self.laberinto) and \
                           0 <= adyacente[0] < len(self.laberinto[0]) and \
                           self.laberinto[adyacente[1]][adyacente[0]] != 3:
                            # Agregar arista con peso (puedes personalizar el peso aquí)
                            peso = self.calcular_peso(adyacente)
                            self.agregar_arista(posicion, adyacente, peso)

    def calcular_peso(self, posicion):
        # Ejemplo: Celda con menor peso si es una intersección (puedes ajustar según tu lógica)
        x, y = posicion
        if self.laberinto[y][x] == 2:  # Supón que '2' es una celda especial con peso bajo
            return 0.5
        return 1


    def calcular_peso(self, posicion):
        # Ejemplo: Celda con menor peso si es una intersección (puedes ajustar según tu lógica)
        x, y = posicion
        if self.laberinto[y][x] == 2:  # Supón que '2' es una celda especial con peso bajo
            return 0.5
        return 1

    def dijkstra(self, inicio, objetivo):
        if inicio not in self.vertices or objetivo not in self.vertices:
            return []

        distancias = {vertice: float('inf') for vertice in self.vertices}
        distancias[inicio] = 0
        cola_prioridad = [(0, inicio)]
        predecesores = {inicio: None}

        while cola_prioridad:
            distancia_actual, actual = heapq.heappop(cola_prioridad)

            if actual == objetivo:
                camino = []
                while actual:
                    camino.append(actual)
                    actual = predecesores[actual]
                return camino[::-1]

            for vecino, peso in self.vertices[actual]:
                distancia = distancia_actual + peso
                if distancia < distancias[vecino]:
                    distancias[vecino] = distancia
                    predecesores[vecino] = actual
                    heapq.heappush(cola_prioridad, (distancia, vecino))

        return []

