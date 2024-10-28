import os

import pygame

from pacman.main.py.logic.Fantasma import Fantasma

# Obtener la ruta absoluta del directorio raíz del proyecto (subiendo más niveles)
current_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Construir la ruta correcta hacia las imágenes
BoardPath = os.path.join(current_dir, "resorces", "ElementImages")

class Blinky(Fantasma):
    def __init__(self, posicion_inicial, square  ):
        super().__init__("rojo",posicion_inicial,1)
        self.square_size = square

    def mover_hacia_objetivo(self, pacman_posicion):
        # Lógica para que Blinky persiga a Pac-Man
        self.objetivo = pacman_posicion
        # Aquí podrías agregar la lógica para moverlo hacia el objetivo
        self._mover_hacia(self.objetivo)

    """def _mover_hacia(self, objetivo):
        # Lógica para mover al fantasma hacia el objetivo (Pac-Man)
        if self.posicion_inicial.get_x() < objetivo.get_x():
            self.posicion_inicial.set_x(self.posicion_inicial.get_x() + self.velocidad)
        elif self.posicion_inicial.get_x() > objetivo.get_x():
            self.posicion_inicial.set_x(self.posicion_inicial.get_x() - self.velocidad)

        if self.posicion_inicial.get_y() < objetivo.get_y():
            self.posicion_inicial.set_y(self.posicion_inicial.get_y() + self.velocidad)
        elif self.posicion_inicial.get_y() > objetivo.get_y():
            self.posicion_inicial.set_y(self.posicion_inicial.get_y() - self.velocidad)"""

    def _mover_hacia(self, objetivo):
        # Lógica para mover al fantasma hacia el objetivo (Pac-Man)
        if self.posicion_inicial[0] < objetivo[0]:
            self.posicion_inicial[0] += self.velocidad
        elif self.posicion_inicial[0] > objetivo[0]:
            self.posicion_inicial[0] -= self.velocidad

        if self.posicion_inicial[1] < objetivo[1]:
            self.posicion_inicial[1] += self.velocidad
        elif self.posicion_inicial[1] > objetivo[1]:
            self.posicion_inicial[1] -= self.velocidad


    def draw(self, screen):
        # Cargar la imagen correspondiente a Blinky
        ghostImage = pygame.image.load(os.path.join(BoardPath, "tile096.png"))  # Asegúrate de que la imagen exista
        # Escalar la imagen para adaptarla al tamaño de la celda del laberinto
        ghostImage = pygame.transform.scale(ghostImage, (int(self.square_size * 0.9), int(self.square_size * 0.9)))

        # Dibujar la imagen en la posición actual de Blinky
        screen.blit(ghostImage, (self.posicion_inicial[0] * self.square_size,
                                 self.posicion_inicial[1] * self.square_size))

