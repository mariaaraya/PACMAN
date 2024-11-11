import os
import random

import pygame

from pacman.main.py.logic.Fantasma import Fantasma
from pacman.main.py.logic.Posicion import Posicion

# Obtener la ruta absoluta del directorio raíz del proyecto (subiendo más niveles)
current_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Construir la ruta correcta hacia las imágenes
BoardPath = os.path.join(current_dir, "resorces", "ElementImages")

class Blinky(Fantasma):
    def __init__(self, posicion_inicial, square,velocidad):
        super().__init__("rojo",posicion_inicial,1, velocidad)
        self.square_size = square
        self.velocidad=velocidad

    def mover_hacia_objetivo(self, pacman_posicion, grafo, delta_time):

        # Obtén el camino hacia Pac-Man usando BFS
        camino = grafo.bfs((round(self.posicion_inicial.get_x()), round(self.posicion_inicial.get_y())),
                               (round(pacman_posicion.get_x()), round(pacman_posicion.get_y())))
        # Imprime el camino completo para depuración


        movimiento = self.velocidad * delta_time

        # Verifica si hay un camino y un siguiente paso
        if len(camino) > 1:
            # Establece el siguiente paso como objetivo temporal
            self.objetivo = camino[1]  # Actualiza el objetivo al siguiente nodo en el camino
            # Calcular la distancia en cada eje
            distancia_x = self.objetivo[0] - self.posicion_inicial.get_x()
            distancia_y = self.objetivo[1] - self.posicion_inicial.get_y()

            # Definir la dirección en función del siguiente paso
            # Movimiento gradual hacia el objetivo según la velocidad
            if abs(distancia_x) > abs(distancia_y):
                self.posicion_inicial.set_x(
                    self.posicion_inicial.get_x() + (movimiento if distancia_x > 0 else -movimiento))
                self._direccion = "derecha" if distancia_x > 0 else "izquierda"
            else:
                self.posicion_inicial.set_y(
                    self.posicion_inicial.get_y() + (movimiento if distancia_y > 0 else -movimiento))
                self._direccion = "abajo" if distancia_y > 0 else "arriba"

            # Mueve directamente al siguiente paso
            #self.posicion_inicial.set_x(self.objetivo[0])
            #self.posicion_inicial.set_y(self.objetivo[1])

    def set_posicion(self, nueva_posicion):
        """
        Este método establece la nueva posición de Blinky.
        :param nueva_posicion: Un objeto que contiene las nuevas coordenadas.
        """
        self.posicion_inicial = nueva_posicion

    def draw_persecucion(self, screen):
        # Selecciona las imágenes de movimiento según la dirección
        if self._direccion == "izquierda":
            image_frame_1 = "tile100.png"
            image_frame_2 = "tile101.png"
        elif self._direccion == "derecha":
            image_frame_1 = "tile096.png"
            image_frame_2 = "tile097.png"
        elif self._direccion == "arriba":
            image_frame_1 = "tile102.png"
            image_frame_2 = "tile103.png"
        elif self._direccion == "abajo":
            image_frame_1 = "tile098.png"
            image_frame_2 = "tile099.png"
        else:
            # Si no hay dirección (por defecto o quieto)
            image_frame_1 = "tile096.png"
            image_frame_2 = "tile097.png"

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








