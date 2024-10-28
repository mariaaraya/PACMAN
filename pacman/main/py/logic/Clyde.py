import os

import pygame

from pacman.main.py.logic.Fantasma import Fantasma
from pacman.main.py.logic.Posicion import Posicion
# Obtener la ruta absoluta del directorio raíz del proyecto (subiendo más niveles)
current_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Construir la ruta correcta hacia las imágenes
BoardPath = os.path.join(current_dir, "resorces", "ElementImages")

class Clyde(Fantasma):
    def __init__(self, posicion_inicial,square):
        super().__init__("naranja", posicion_inicial,square,1)


    def mover_hacia_objetivo(self, pacman_posicion):
        if self.debe_alejarse(pacman_posicion):
            # Lógica para alejarse de Pac-Man
            self.objetivo = Posicion(
                self.posicion_inicial.get_x() - (pacman_posicion.get_x() - self.posicion_inicial.get_x()),
                self.posicion_inicial.get_y() - (pacman_posicion.get_y() - self.posicion_inicial.get_y()))
        else:
            self.objetivo = pacman_posicion

        self._mover_hacia(self.objetivo)

    def debe_alejarse(self, pacman_posicion):
        # Lógica para decidir si Clyde debe alejarse (ejemplo: basado en la distancia a Pac-Man)
        return True  # Puedes agregar tu lógica aquí para que Clyde se comporte de manera más errática.

    def _mover_hacia(self, objetivo):
        # Lógica para mover a Clyde hacia el objetivo
        super()._mover_hacia(objetivo)

    def draw(self, screen):
        # Cargar la imagen correspondiente a Blinky
        ghostImage = pygame.image.load(os.path.join(BoardPath, "tile144.png"))  # Asegúrate de que la imagen exista
        # Escalar la imagen para adaptarla al tamaño de la celda del laberinto
        ghostImage = pygame.transform.scale(ghostImage, (int(self.square_size * 0.9), int(self.square_size * 0.9)))
        # Dibujar la imagen en la posición actual de Blinky
        screen.blit(ghostImage, (self.posicion_inicial[0] * self.square_size,
                                 self.posicion_inicial[1] * self.square_size))
