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
        # Verificar si el objetivo está asignado
        if self.objetivo is None:
            # Si no hay objetivo asignado, usar una imagen estática (fantasma quieto)
            image_frame_1 = "tile144.png"
            image_frame_2 = "tile145.png"
        else:
            # Verificar si el fantasma se está moviendo hacia alguna dirección
            if self.posicion_inicial == self.objetivo:
                # Si el fantasma está quieto, usa la imagen estática
                image_frame_1 = "tile144.png"
                image_frame_2 = "tile145.png"
            else:
                # Verifica la dirección en la que se está moviendo
                if self.posicion_inicial[0] > self.objetivo[0]:  # Se mueve hacia la izquierda
                    image_frame_1 = "tile1448.png"
                    image_frame_2 = "tile1449png"
                elif self.posicion_inicial[0] < self.objetivo[0]:  # Se mueve hacia la derecha
                    image_frame_1 = "tile144.png"
                    image_frame_2 = "tile145.png"
                elif self.posicion_inicial[1] > self.objetivo[1]:  # Se mueve hacia arriba
                    image_frame_1 = "tile150.png"
                    image_frame_2 = "tile151.png"
                elif self.posicion_inicial[1] < self.objetivo[1]:  # Se mueve hacia abajo
                    image_frame_1 = "tile146.png"
                    image_frame_2 = "tile147.png"

        # Alternar entre las dos imágenes para simular movimiento
        if self.changeFeetCount % 2 == 0:
            ghostImage = pygame.image.load(os.path.join(BoardPath, image_frame_1))
        else:
            ghostImage = pygame.image.load(os.path.join(BoardPath, image_frame_2))

        self.changeFeetCount += 1

        # Escalar la imagen para adaptarla al tamaño de la celda del laberinto
        ghostImage = pygame.transform.scale(ghostImage, (int(self.square_size * 0.9), int(self.square_size * 0.9)))

        # Dibujar la imagen en la posición actual de Blinky
        screen.blit(ghostImage, (self.posicion_inicial.get_x() * self.square_size,
                                 self.posicion_inicial.get_y() * self.square_size))

