import os
import random

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
        self.first_move_to_target = True

    def mover_hacia_objetivo(self, pacman_posicion, grafo, delta_time):

            # Calcular el objetivo adelantado en la dirección de Pac-Man
            anticipacion_x = pacman_posicion.get_x()
            anticipacion_y = pacman_posicion.get_y()
            direccion = pacman_posicion.get_direccion()  # Dirección de Pac-Man

            # Ajustar la posición anticipada según la dirección de Pac-Man
            anticipacion_distancia = 4  # Distancia en tiles que Pinky intentará anticipar
            if direccion == "derecha":
                anticipacion_x += anticipacion_distancia
            elif direccion == "izquierda":
                anticipacion_x -= anticipacion_distancia
            elif direccion == "arriba":
                anticipacion_y -= anticipacion_distancia
            elif direccion == "abajo":
                anticipacion_y += anticipacion_distancia

            # Verificar si el camino anticipado está disponible y cerca de Pac-Man
            camino_anticipado = grafo.bfs((round(self.posicion_inicial.get_x()), round(self.posicion_inicial.get_y())),
                                          (round(anticipacion_x), round(anticipacion_y)))

            # Si el camino anticipado no es viable o está lejos, ir directamente hacia Pac-Man
            if len(camino_anticipado) <= 1 or len(camino_anticipado) > anticipacion_distancia + 3:
                # Seguir a Pac-Man directamente
                camino = grafo.bfs((round(self.posicion_inicial.get_x()), round(self.posicion_inicial.get_y())),
                                   (round(pacman_posicion.get_x()), round(pacman_posicion.get_y())))
            else:
                # Usar el camino anticipado para interceptar
                camino = camino_anticipado

            # Control de movimiento y velocidad
            movimiento = self.velocidad * delta_time
            if len(camino) > 1:
                siguiente_x, siguiente_y = camino[1]
                distancia_x = siguiente_x - self.posicion_inicial.get_x()
                distancia_y = siguiente_y - self.posicion_inicial.get_y()

                # Movimiento en la dirección del siguiente paso
                if abs(distancia_x) > abs(distancia_y):
                    desplazamiento = movimiento if distancia_x > 0 else -movimiento
                    self.posicion_inicial.set_x(self.posicion_inicial.get_x() + desplazamiento)
                    self._direccion = "derecha" if distancia_x > 0 else "izquierda"
                else:
                    desplazamiento = movimiento if distancia_y > 0 else -movimiento
                    self.posicion_inicial.set_y(self.posicion_inicial.get_y() + desplazamiento)
                    self._direccion = "abajo" if distancia_y > 0 else "arriba"

    # gracias al codigo de blinky y clyde, pudimos guiarnos en la parte del movimiento, pero nos apoyamos en chatgpt para adaptar sus nuevos movimientos, e incluso mejorar codigo viejo

    def set_posicion(self, nueva_posicion):
        # Este método establece la nueva posición de Pinky.
        self.posicion_inicial = nueva_posicion

    def draw_persecucion(self, screen):
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
