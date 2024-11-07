import os
import random

import pygame

from pacman.main.py.logic.Fantasma import Fantasma
from pacman.main.py.logic.Posicion import Posicion
# Obtener la ruta absoluta del directorio raíz del proyecto (subiendo más niveles)
current_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Construir la ruta correcta hacia las imágenes
BoardPath = os.path.join(current_dir, "resorces", "ElementImages")

class Clyde(Fantasma):
    def __init__(self, posicion_inicial,square):
        super().__init__("naranja", posicion_inicial,square,-2)
        self.square_size = square
        self._direccion = "derecha"  # Dirección inicial, similar a Pac-Man}
        self.cambio_estado_cada = 100  # Número de frames antes de cambiar el estado (perseguir/alejarse)
        self.contador_frames = 0       # Contador de frames para alternar el estado
        self.estado_actual = "perseguir"  # Clyde empieza persiguiendo a Pac-Man
        self.objetivo_aleatorio = None  # Posición aleatoria en estado de alejamiento


    def mover_hacia_objetivo(self, pacman_posicion, grafo, delta_time):
        # Cada cierto número de frames, Clyde cambia su comportamiento
        self.contador_frames += 1
        if self.contador_frames >= self.cambio_estado_cada:
            self.contador_frames = 0
            # Alterna entre perseguir y alejarse de Pac-Man
            if self.estado_actual == "perseguir":
                self.estado_actual = "alejarse"
                # Genera una nueva posición aleatoria como objetivo al cambiar a "alejarse"
                self.objetivo_aleatorio = self.generar_posicion_aleatoria(grafo)
            else:
                self.estado_actual = "perseguir"

        # Define el objetivo según el estado actual de Clyde
        if self.estado_actual == "alejarse" and self.objetivo_aleatorio:
            objetivo = self.objetivo_aleatorio  # Se mueve a una posición aleatoria en el laberinto
            # Si ya llegó a la posición aleatoria, genera otra para seguir moviéndose erráticamente
            if (round(self.posicion_inicial.get_x()), round(self.posicion_inicial.get_y())) == (
            objetivo.get_x(), objetivo.get_y()):
                self.objetivo_aleatorio = self.generar_posicion_aleatoria(grafo)
        else:
            objetivo = pacman_posicion  # Persigue a Pac-Man en modo de persecución

        # Encuentra el camino en el grafo hacia el objetivo
        camino = grafo.bfs((round(self.posicion_inicial.get_x()), round(self.posicion_inicial.get_y())),
                           (round(objetivo.get_x()), round(objetivo.get_y())))

        # Si hay un camino, mueve a Clyde al siguiente paso
        if len(camino) > 1:
            siguiente_posicion = camino[1]
            self.posicion_inicial.set_x(siguiente_posicion[0])
            self.posicion_inicial.set_y(siguiente_posicion[1])

    def generar_posicion_aleatoria(self, grafo):
        """Genera una posición aleatoria en el laberinto."""
        max_x, max_y = grafo.obtener_limites()  # Obtener los límites del laberinto
        x_aleatorio = random.randint(0, max_x)
        y_aleatorio = random.randint(0, max_y)
        return Posicion(x_aleatorio, y_aleatorio)

    def _mover_hacia(self, objetivo):
        # Lógica para mover a Clyde hacia el objetivo
        super()._mover_hacia(objetivo)

    def draw(self, screen):
            # Selecciona las imágenes de movimiento según la dirección
            if self._direccion == "izquierda":
                image_frame_1 = "tile1448.png"
                image_frame_2 = "tile1449.png"
            elif self._direccion == "derecha":
                image_frame_1 = "tile144.png"
                image_frame_2 = "tile145.png"
            elif self._direccion == "arriba":
                image_frame_1 = "tile150.png"
                image_frame_2 = "tile151.png"
            elif self._direccion == "abajo":
                image_frame_1 = "tile146.png"
                image_frame_2 = "tile147.png"
            else:
                # Si no hay dirección (por defecto o quieto)
                image_frame_1 = "tile144.png"
                image_frame_2 = "tile145.png"

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