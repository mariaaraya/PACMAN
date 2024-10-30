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

    def mover_hacia_objetivo(self, pacman_posicion, grafo):
        # Obtener el camino más corto hacia Pac-Man usando BFS
        camino = grafo.bfs(self.posicion_inicial, pacman_posicion)
        if camino:
            # Mover a la siguiente posición en el camino
            siguiente_posicion = camino[1]
            self.posicion_inicial = siguiente_posicion

    def _mover_hacia(self, objetivo):
        # Lógica para mover al fantasma hacia el objetivo (Pac-Man)
        if self.posicion_inicial.get_x() < objetivo.get_x():
            self.posicion_inicial.set_x(self.posicion_inicial.get_x() + self.velocidad)
        elif self.posicion_inicial.get_x() > objetivo.get_x():
            self.posicion_inicial.set_x(self.posicion_inicial.get_x() - self.velocidad)

        if self.posicion_inicial.get_y() < objetivo.get_y():
            self.posicion_inicial.set_y(self.posicion_inicial.get_y() + self.velocidad)
        elif self.posicion_inicial.get_y() > objetivo.get_y():
            self.posicion_inicial.set_y(self.posicion_inicial.get_y() - self.velocidad)

    def get_posicion(self):
        # Devuelve la posición actual de Blinky
        return self.posicion_inicial

    def draw(self, screen):
        # Verificar si el objetivo está asignado
        if self.objetivo is None:
            # Si no hay objetivo asignado, usar una imagen estática (fantasma quieto)
            image_frame_1 = "tile096.png"
            image_frame_2 = "tile097.png"
        else:
            # Verificar si el fantasma se está moviendo hacia alguna dirección
            if self.posicion_inicial == self.objetivo:
                # Si el fantasma está quieto, usa la imagen estática
                image_frame_1 = "tile096.png"
                image_frame_2 = "tile097.png"
            else:
                # Verifica la dirección en la que se está moviendo
                if self.posicion_inicial[0] > self.objetivo[0]:  # Se mueve hacia la izquierda
                    image_frame_1 = "tile100.png"
                    image_frame_2 = "tile101.png"
                elif self.posicion_inicial[0] < self.objetivo[0]:  # Se mueve hacia la derecha
                    image_frame_1 = "tile096.png"
                    image_frame_2 = "tile097.png"
                elif self.posicion_inicial[1] > self.objetivo[1]:  # Se mueve hacia arriba
                    image_frame_1 = "tile102.png"
                    image_frame_2 = "tile103.png"
                elif self.posicion_inicial[1] < self.objetivo[1]:  # Se mueve hacia abajo
                    image_frame_1 = "tile098.png"
                    image_frame_2 = "tile099.png"

        # Alternar entre las dos imágenes para simular movimiento
        if self.changeFeetCount % 2 == 0:
            ghostImage = pygame.image.load(os.path.join(BoardPath, image_frame_1))
        else:
            ghostImage = pygame.image.load(os.path.join(BoardPath, image_frame_2))

        self.changeFeetCount += 1

        # Escalar la imagen para adaptarla al tamaño de la celda del laberinto
        ghostImage = pygame.transform.scale(ghostImage, (int(self.square_size * 0.9), int(self.square_size * 0.9)))

        # Dibujar la imagen en la posición actual de Pac-Man
        screen.blit(ghostImage, (self.posicion_inicial.get_x() * self.square_size,
                                  self.posicion_inicial.get_y() * self.square_size))





