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
    def __init__(self, posicion_inicial,square,velocidad_persiguiendo, velocidad_alejarse):
        super().__init__("naranja", posicion_inicial,square,velocidad_persiguiendo)
        self.square_size = square
        self.cambio_estado_cada = 200  # Número de frames antes de cambiar el estado (perseguir/alejarse)
        self.contador_frames = 0  # Contador de frames para alternar el estado
        self.estado_actual = "asustado"  # Clyde empieza persiguiendo a Pac-Man
        self.velocidad_persiguiendo = velocidad_persiguiendo
        self.velocidad_alejarse = velocidad_alejarse
        self.distancia_minima_alejamiento = 5  # Distancia mínima en la que Clyde comenzará a alejarse



    def mover_hacia_objetivo(self, pacman_posicion, grafo, delta_time):
        # Calcula la distancia entre Clyde y Pac-Man
        dx = pacman_posicion.get_x() - self.posicion_inicial.get_x()
        dy = pacman_posicion.get_y() - self.posicion_inicial.get_y()
        distancia_a_pacman = (dx ** 2 + dy ** 2) ** 0.5


        # Cambia el estado según la distancia a Pac-Man y el contador de frames
        self.contador_frames += 1
        if self.contador_frames >= self.cambio_estado_cada:
            self.contador_frames = 0
            # Cambia el estado si Clyde está suficientemente cerca de Pac-Man
            if distancia_a_pacman < self.distancia_minima_alejamiento:
                self.estado_actual = "alejarse"
                self.objetivo_aleatorio = self.generar_posicion_aleatoria(grafo)
            else:
                self.estado_actual = "perseguir"

        # Define el objetivo y la velocidad según el estado actual de Clyde
        objetivo = self.objetivo_aleatorio if self.estado_actual == "alejarse" else pacman_posicion
        velocidad_actual = self.velocidad_alejarse if self.estado_actual == "alejarse" else self.velocidad_persiguiendo

        # Encuentra el camino en el grafo hacia el objetivo
        camino = grafo.bfs((round(self.posicion_inicial.get_x()), round(self.posicion_inicial.get_y())),
                           (round(objetivo.get_x()), round(objetivo.get_y())))

        # Si hay un camino válido, mueve a Clyde en dirección al siguiente nodo del camino
        if len(camino) > 1:
            siguiente_x, siguiente_y = camino[1]
            dx = siguiente_x - self.posicion_inicial.get_x()
            dy = siguiente_y - self.posicion_inicial.get_y()
            distancia = (dx ** 2 + dy ** 2) ** 0.5

            # Calcula los incrementos de posición proporcional a la velocidad
            if distancia > 0:
                desplazamiento_x = (dx / distancia) * velocidad_actual * delta_time
                desplazamiento_y = (dy / distancia) * velocidad_actual * delta_time

                # Actualiza la posición de Clyde de forma gradual
                nueva_x = self.posicion_inicial.get_x() + desplazamiento_x
                nueva_y = self.posicion_inicial.get_y() + desplazamiento_y
                self.posicion_inicial.set_x(nueva_x)
                self.posicion_inicial.set_y(nueva_y)

            # Si no hay un camino y Clyde está en modo alejarse, genera una nueva posición aleatoria
        elif self.estado_actual == "alejarse":
            self.objetivo_aleatorio = self.generar_posicion_aleatoria(grafo)




    def camino_valido(self, grafo, objetivo):
        """Verifica si hay un camino válido hacia el objetivo."""
        camino = grafo.bfs((round(self.posicion_inicial.get_x()), round(self.posicion_inicial.get_y())),
                           (round(objetivo.get_x()), round(objetivo.get_y())))
        return len(camino) > 1


    def draw_persecucion(self, screen):
        # Selecciona las imágenes de movimiento según la dirección
        if self._direccion == "izquierda":
            image_frame_1 = "tile148.png"
            image_frame_2 = "tile149.png"
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
            # Imagen por defecto si no hay dirección
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

        # Verificar y actualizar la posición actual en cada ciclo
        current_x = self.posicion_inicial.get_x() * self.square_size
        current_y = self.posicion_inicial.get_y() * self.square_size

        # Dibujar la imagen en la posición actual de Clyde
        screen.blit(ghostImage, (current_x, current_y))
