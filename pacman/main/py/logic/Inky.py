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

    def mover_hacia_objetivo(self, pacman_pos, blinky_pos, grafo):
        objetivo_x = pacman_pos.get_x() + (blinky_pos.get_x() - pacman_pos.get_x())
        objetivo_y = pacman_pos.get_y() + (blinky_pos.get_y() - pacman_pos.get_y())

        camino = grafo.bfs(self.posicion_inicial, (objetivo_x, objetivo_y))
        if camino:
            self.posicion_inicial = camino[1]

    def _mover_hacia(self, objetivo):
        # Lógica para mover a Inky hacia el objetivo
        super()._mover_hacia(objetivo)

    def draw(self, screen):
        # Verificar si el objetivo está asignado
        if self.objetivo is None:
            # Si no hay objetivo asignado, usar una imagen estática (fantasma quieto)
            image_frame_1 = "tile136.png"
            image_frame_2 = "tile137.png"
        else:
            # Verificar si el fantasma se está moviendo hacia alguna dirección
            if self.posicion_inicial == self.objetivo:
                # Si el fantasma está quieto, usa la imagen estática
                image_frame_1 = "tile136.png"
                image_frame_2 = "tile137.png"
            else:
                # Verifica la dirección en la que se está moviendo
                if self.posicion_inicial[0] > self.objetivo[0]:  # Se mueve hacia la izquierda
                    image_frame_1 = "tile140.png"
                    image_frame_2 = "tile141.png"
                elif self.posicion_inicial[0] < self.objetivo[0]:  # Se mueve hacia la derecha
                    image_frame_1 = "tile136.png"
                    image_frame_2 = "tile1367.png"
                elif self.posicion_inicial[1] > self.objetivo[1]:  # Se mueve hacia arriba
                    image_frame_1 = "tile142.png"
                    image_frame_2 = "tile143.png"
                elif self.posicion_inicial[1] < self.objetivo[1]:  # Se mueve hacia abajo
                    image_frame_1 = "tile138.png"
                    image_frame_2 = "tile139.png"

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

