import os

import pygame

from pacman.main.py.logic.Fantasma import Fantasma
from pacman.main.py.logic.Posicion import Posicion

# Obtener la ruta absoluta del directorio raíz del proyecto (subiendo más niveles)
current_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Construir la ruta correcta hacia las imágenes
BoardPath = os.path.join(current_dir, "resorces", "ElementImages")

class Pinky(Fantasma):
    def __init__(self, posicion_inicial,square):
        super().__init__("rosa", posicion_inicial, square,1)

    def mover_hacia_objetivo(self, pacman_posicion):
        # Lógica para que Pinky intente predecir la posición futura de Pac-Man
        futuro_x = pacman_posicion.get_x() + (
                    pacman_posicion.get_velocidad() * (1 if pacman_posicion.get_direccion() == "derecha" else -1))
        futuro_y = pacman_posicion.get_y() + (
                    pacman_posicion.get_velocidad() * (1 if pacman_posicion.get_direccion() == "abajo" else -1))

        # Establecer objetivo
        self.objetivo = Posicion(futuro_x, futuro_y)
        self._mover_hacia(self.objetivo)

    def _mover_hacia(self, objetivo):
        # Lógica para mover a Pinky hacia el objetivo
        super()._mover_hacia(objetivo)

    def draw(self, screen):
        # Verificar si el objetivo está asignado
        if self.objetivo is None:
            # Si no hay objetivo asignado, usar una imagen estática (fantasma quieto)
            image_frame_1 = "tile128.png"
            image_frame_2 = "tile129.png"
        else:
            # Verificar si el fantasma se está moviendo hacia alguna dirección
            if self.posicion_inicial == self.objetivo:
                # Si el fantasma está quieto, usa la imagen estática
                image_frame_1 = "tile128.png"
                image_frame_2 = "tile129.png"
            else:
                # Verifica la dirección en la que se está moviendo
                if self.posicion_inicial[0] > self.objetivo[0]:  # Se mueve hacia la izquierda
                    image_frame_1 = "tile132.png"
                    image_frame_2 = "tile133.png"
                elif self.posicion_inicial[0] < self.objetivo[0]:  # Se mueve hacia la derecha
                    image_frame_1 = "tile128.png"
                    image_frame_2 = "tile129.png"
                elif self.posicion_inicial[1] > self.objetivo[1]:  # Se mueve hacia arriba
                    image_frame_1 = "tile134.png"
                    image_frame_2 = "tile135.png"
                elif self.posicion_inicial[1] < self.objetivo[1]:  # Se mueve hacia abajo
                    image_frame_1 = "tile130.png"
                    image_frame_2 = "tile131.png"

        # Alternar entre las dos imágenes para simular movimiento
        if self.changeFeetCount % 2 == 0:
            ghostImage = pygame.image.load(os.path.join(BoardPath, image_frame_1))
        else:
            ghostImage = pygame.image.load(os.path.join(BoardPath, image_frame_2))

        self.changeFeetCount += 1

        # Escalar la imagen para adaptarla al tamaño de la celda del laberinto
        ghostImage = pygame.transform.scale(ghostImage, (int(self.square_size * 0.9), int(self.square_size * 0.9)))

        # Dibujar la imagen en la posición actual de Blinky
        screen.blit(ghostImage, (self.posicion_inicial[0] * self.square_size,
                                 self.posicion_inicial[1] * self.square_size))