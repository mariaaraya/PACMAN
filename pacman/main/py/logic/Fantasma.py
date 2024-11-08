from abc import ABC, abstractmethod
import random
from pacman.main.py.logic.Posicion import Posicion

class Fantasma (ABC):
    MODO_PERSECUCION = "persecucion"
    MODO_DISPERSION = "dispersión"
    MODO_ASUSTADO = "asustado"

    def __init__(self, color, posicion_inicial, square , velocidad):
        self.color = color
        self._direccion = "derecha"
        self.posicion_inicial = posicion_inicial
        self.posicion_actual = posicion_inicial  # Posición actual del fantasma
        self.velocidad = velocidad
        self.objetivo = None
        self.modo = self.MODO_PERSECUCION
        self.square_size = square
        self.changeFeetCount = 0
        self.path_to_target = []  # Camino actual hacia el objetivo
        self.objetivo_aleatorio = None  # Inicializa el objetivo aleatorio como None


    def actualizar_modo(self, nuevo_modo):
        self.modo = nuevo_modo


    def mover(self, pacman_posicion , grafo, delta_time):
        print("Modo es " , self.modo)
        if self.modo == self.MODO_PERSECUCION:
            self.mover_hacia_objetivo(pacman_posicion, grafo, delta_time)
        elif self.modo == self.MODO_DISPERSION:
            self.mover_hacia_esquina()  # Implementa este método
        elif self.modo == self.MODO_ASUSTADO:
            self.mover_aleatoriamente(grafo, delta_time)  # Implementa este método

    def mover_aleatoriamente(self, grafo, delta_time):
        print("Se mueve aletoriamente ")

    def mover_aleatoriamente(self, grafo, delta_time):
        # Generar un nuevo objetivo aleatorio si no tiene uno o si ya lo alcanzó
        if not self.objetivo_aleatorio or (
                round(self.posicion_inicial.get_x()), round(self.posicion_inicial.get_y())) == (
                round(self.objetivo_aleatorio.get_x()), round(self.objetivo_aleatorio.get_y())):
            # Generar una posición aleatoria en el laberinto
            self.objetivo_aleatorio = self.generar_posicion_aleatoria(grafo)

        # Encuentra el camino en el grafo hacia el objetivo aleatorio
        camino = grafo.bfs((round(self.posicion_inicial.get_x()), round(self.posicion_inicial.get_y())),
                           (round(self.objetivo_aleatorio.get_x()), round(self.objetivo_aleatorio.get_y())))

        # Si hay un camino válido, mueve al fantasma en dirección al siguiente nodo del camino
        if len(camino) > 1:
            siguiente_x, siguiente_y = camino[1]
            dx = siguiente_x - self.posicion_inicial.get_x()
            dy = siguiente_y - self.posicion_inicial.get_y()
            distancia = (dx ** 2 + dy ** 2) ** 0.5

            # Calcula los incrementos de posición proporcional a la velocidad
            if distancia > 0:
                desplazamiento_x = (dx / distancia) * self.velocidad * delta_time
                desplazamiento_y = (dy / distancia) * self.velocidad * delta_time

                # Actualiza la posición del fantasma de forma gradual
                nueva_x = self.posicion_inicial.get_x() + desplazamiento_x
                nueva_y = self.posicion_inicial.get_y() + desplazamiento_y
                self.posicion_inicial.set_x(nueva_x)
                self.posicion_inicial.set_y(nueva_y)

        # Si no hay un camino válido, generar una nueva posición aleatoria
        else:
            self.objetivo_aleatorio = self.generar_posicion_aleatoria(grafo)

    @staticmethod
    def generar_posicion_aleatoria(grafo):
        """Genera una posición aleatoria en el laberinto."""
        max_x, max_y = grafo.obtener_limites()  # Obtener los límites del laberinto
        x_aleatorio = random.randint(0, max_x)
        y_aleatorio = random.randint(0, max_y)
        return Posicion(x_aleatorio, y_aleatorio)

    @abstractmethod
    def mover_hacia_objetivo(self, pacman_posicion, grafo, delta_time):
        pass

    def mover_hacia_esquina(self):
        pass

    def draw(self, screen):
        """Método  para dibijar el elemento."""
        pass


