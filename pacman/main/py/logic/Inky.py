import os

import pygame

from pacman.main.py.logic.Fantasma import Fantasma
from pacman.main.py.logic.Posicion import Posicion

# Obtener la ruta absoluta del directorio raíz del proyecto (subiendo más niveles)
current_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Construir la ruta correcta hacia las imágenes
BoardPath = os.path.join(current_dir, "resorces", "ElementImages")

class Inky(Fantasma):
    def __init__(self, posicion_inicial, square, blinky ):
        super().__init__("cian", posicion_inicial, square,  1)
        self.blinky = blinky  # Referencia a Blinky

    def mover_hacia_objetivo(self, pacman_posicion):
        # Lógica para que Inky use la posición de Pac-Man y Blinky
        blinky_pos = self.blinky.posicion_inicial
        objetivo_x = pacman_posicion.get_x() + (blinky_pos.get_x() - pacman_posicion.get_x())
        objetivo_y = pacman_posicion.get_y() + (blinky_pos.get_y() - pacman_posicion.get_y())

        self.objetivo = Posicion(objetivo_x, objetivo_y)
        self._mover_hacia(self.objetivo)

    def _mover_hacia(self, objetivo):
        # Lógica para mover a Inky hacia el objetivo
        super()._mover_hacia(objetivo)

    def draw(self, screen):
        # Cargar la imagen correspondiente a Blinky
        ghostImage = pygame.image.load(os.path.join(BoardPath, "tile136.png"))  # Asegúrate de que la imagen exista
        # Escalar la imagen para adaptarla al tamaño de la celda del laberinto
        ghostImage = pygame.transform.scale(ghostImage, (int(self.square_size * 0.9), int(self.square_size * 0.9)))

        # Dibujar la imagen en la posición actual de Blinky
        screen.blit(ghostImage, (self.posicion_inicial[0] * self.square_size,
                                 self.posicion_inicial[1] * self.square_size))
