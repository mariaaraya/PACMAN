import os

import pygame

from pacman.main.py.logic.Fantasma import Fantasma
from pacman.main.py.logic.Grafo import Grafo
from pacman.main.py.logic.Posicion import Posicion

# Obtener la ruta absoluta del directorio raíz del proyecto (subiendo más niveles)
current_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Construir la ruta correcta hacia las imágenes
BoardPath = os.path.join(current_dir, "resorces", "ElementImages")

class Pinky(Fantasma):
    def __init__(self, posicion_inicial,square, velocidad):
        super().__init__("rosa", posicion_inicial, square,velocidad)
        self.square_size=square
        self.velocidad=velocidad

    def mover_hacia_objetivo(self, pacman_posicion, grafo, delta_time):
        # Calcular el objetivo adelantado en la dirección de Pac-Man
        anticipacion_x = pacman_posicion.get_x()
        anticipacion_y = pacman_posicion.get_y()
        direccion = pacman_posicion.get_direccion()  # Asumiendo que Pac-Man tiene un método para obtener la dirección

        # Ajuste de la posición anticipada según la dirección de Pac-Man
        if direccion == "derecha":
            anticipacion_x += 4
        elif direccion == "izquierda":
            anticipacion_x -= 4
        elif direccion == "arriba":
            anticipacion_y -= 4
        elif direccion == "abajo":
            anticipacion_y += 4

        # Obtén el camino hacia la posición anticipada
        camino = grafo.bfs((round(self.posicion_inicial.get_x()), round(self.posicion_inicial.get_y())),
                           (round(anticipacion_x), round(anticipacion_y)))

        # Control de movimiento y velocidad
        movimiento = self.velocidad * delta_time
        if len(camino) > 1:
            self.objetivo = camino[1]
            distancia_x = self.objetivo[0] - self.posicion_inicial.get_x()
            distancia_y = self.objetivo[1] - self.posicion_inicial.get_y()

            # Movimiento en la dirección del siguiente paso
            if abs(distancia_x) > abs(distancia_y):
                self.posicion_inicial.set_x(self.posicion_inicial.get_x() + (movimiento if distancia_x > 0 else -movimiento))
                self._direccion = "derecha" if distancia_x > 0 else "izquierda"
            else:
                self.posicion_inicial.set_y(self.posicion_inicial.get_y() + (movimiento if distancia_y > 0 else -movimiento))
                self._direccion = "abajo" if distancia_y > 0 else "arriba"

    def _mover_hacia(self, objetivo , grafo, delta_time):
        super()._mover_hacia(objetivo)

    def draw(self, screen):
        # Selecciona las imágenes de movimiento según la dirección
        if self._direccion == "izquierda":
            image_frame_1 = "tile132.png"
            image_frame_2 = "tile133.png"
        elif self._direccion == "derecha":
            image_frame_1 = "tile128.png"
            image_frame_2 = "tile129.png"
        elif self._direccion == "arriba":
            image_frame_1 = "tile134.png"
            image_frame_2 = "tile135.png"
        elif self._direccion == "abajo":
            image_frame_1 = "tile130.png"
            image_frame_2 = "tile131.png"
        else:
            # Si no hay dirección (por defecto o quieto)
            image_frame_1 = "tile128.png"
            image_frame_2 = "tile129.png"

        # Alternar entre las dos imágenes para simular movimiento
        if self.changeFeetCount % 2 == 0:
            ghostImage = pygame.image.load(os.path.join(BoardPath, image_frame_1))
        else:
            ghostImage = pygame.image.load(os.path.join(BoardPath, image_frame_2))

        self.changeFeetCount += 1

        # Escalar la imagen para adaptarla al tamaño de la celda del laberinto
        ghostImage = pygame.transform.scale(ghostImage, (int(self.square_size * 0.9), int(self.square_size * 0.9)))

        # Dibujar la imagen en la posición actual de Pinky
        screen.blit(ghostImage, (self.posicion_inicial.get_x() * self.square_size,
                                 self.posicion_inicial.get_y() * self.square_size))
