import copy
import os
import time
from abc import ABC, abstractmethod
import random

import pygame

from pacman.main.py.logic.Posicion import Posicion
# Obtener la ruta absoluta del directorio raíz del proyecto (subiendo más niveles)
current_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Construir la ruta correcta hacia las imágenes
BoardPath = os.path.join(current_dir, "resorces", "ElementImages")

class Fantasma (ABC):
    MODO_PERSECUCION = "persecucion"
    MODO_DISPERSION = "dispersión"
    MODO_ASUSTADO = "asustado"

    def __init__(self, color, posicion_inicial, square , velocidad):
        self.color = color
        self._direccion = "derecha"
        self.posicion_inicial = posicion_inicial
        self.posicion_aux = copy.deepcopy(posicion_inicial)  # Posición actual del fantasma
        self.velocidad = velocidad
        self.objetivo = None
        self.modo = self.MODO_PERSECUCION
        self.square_size = square
        self.changeFeetCount = 0
        self.path_to_target = []  # Camino actual hacia el objetivo
        self.objetivo_aleatorio = None  # Inicializa el objetivo aleatorio como None
        self.inicio_colision = None  # Almacena el tiempo de inicio de colisión
        self.en_colision = False  # Bandera para verificar si está en colisión
        self.first_move_to_target = True


    def actualizar_modo(self, nuevo_modo):
        self.modo = nuevo_modo

    def get_posicion(self):
       return self.posicion_inicial

    def colision_Pacman(self):
        """Cambia el modo del fantasma a dispersión al colisionar con Pac-Man en modo persecución."""
        self.modo = self.MODO_DISPERSION


    def mover_posicon_inical(self, grafo, delta_time):
        if self.modo == self.MODO_DISPERSION and (
                round(self.posicion_inicial.get_x()), round(self.posicion_inicial.get_y())) == (
                round(self.posicion_aux.get_x()), round(self.posicion_aux.get_y())):
            # Cambia a MODO_PERSECUCION cuando alcance la posición inicial
            self.modo = self.MODO_PERSECUCION

            return

            # Obtén el camino hacia Pac-Man usando BFS
        camino = grafo.bfs((round(self.posicion_inicial.get_x()), round(self.posicion_inicial.get_y())),
                           (round(self.posicion_aux.get_x()), round(self.posicion_aux.get_y())))
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
            self.posicion_inicial.set_x(self.objetivo[0])
            self.posicion_inicial.set_y(self.objetivo[1])
            self.first_move_to_target = True


    def mover(self, pacman_posicion , grafo, delta_time):
        if self.modo == self.MODO_PERSECUCION:
            self.mover_hacia_objetivo(pacman_posicion, grafo, delta_time)
        elif self.modo == self.MODO_DISPERSION:
            self.mover_posicon_inical(grafo, delta_time)
        elif self.modo == self.MODO_ASUSTADO:
            self.mover_aleatoriamente(grafo, delta_time)  # Implementa este método

    def reiniciar_posicion(self):
        """Restablece la posición del fantasma a su posición inicial."""
        self.posicion_inicial = copy.deepcopy(self.posicion_aux)
        self.modo = self.MODO_PERSECUCION

    def mover_aleatoriamente(self, grafo, delta_time):

        if not self.objetivo_aleatorio or (
                    round(self.posicion_inicial.get_x()), round(self.posicion_inicial.get_y())) == (
                    round(self.objetivo_aleatorio.get_x()), round(self.objetivo_aleatorio.get_y())):
                # Generar una posición aleatoria en el laberinto
                self.objetivo_aleatorio = self.generar_posicion_aleatoria(grafo)

                # Encuentra el camino en el grafo hacia el objetivo aleatorio
        camino = grafo.bfs((round(self.posicion_inicial.get_x()), round(self.posicion_inicial.get_y())),
                     (round(self.objetivo_aleatorio.get_x()), round(self.objetivo_aleatorio.get_y())))

        # Si hay un camino válido, mueve al fantasma en dirección al siguiente nodo del camino
        if len(camino) > 1:
            siguiente_x, siguiente_y = camino[1]
            dx = siguiente_x - self.posicion_inicial.get_x()
            dy = siguiente_y - self.posicion_inicial.get_y()
            distancia = (dx ** 2 + dy ** 2) ** 0.5

            # Calcula los incrementos de posición proporcional a la velocidad
            if distancia > 0:
                desplazamiento_x = (dx / distancia) * self.velocidad * delta_time
                desplazamiento_y = (dy / distancia) * self.velocidad * delta_time

                # Actualiza la posición del fantasma de forma gradual
                nueva_x = self.posicion_inicial.get_x() + desplazamiento_x
                nueva_y = self.posicion_inicial.get_y() + desplazamiento_y
                self.posicion_inicial.set_x(nueva_x)
                self.posicion_inicial.set_y(nueva_y)
                # Actualiza la dirección en función de dx y dy
                if abs(dx) > abs(dy):  # Movimiento horizontal
                    self._direccion = "derecha" if dx > 0 else "izquierda"
                else:  # Movimiento vertical
                    self._direccion = "abajo" if dy > 0 else "arriba"

        # Si no hay un camino válido, generar una nueva posición aleatoria
        else:
            self.objetivo_aleatorio = self.generar_posicion_aleatoria(grafo)

    @staticmethod
    def generar_posicion_aleatoria(grafo):
        """Genera una posición aleatoria en el laberinto dentro del grafo."""
        # Obtener todas las posiciones accesibles (nodos) del grafo
        posiciones_accesibles = list(grafo.vertices.keys())

        # Seleccionar una posición aleatoria de las posiciones accesibles
        posicion_aleatoria = random.choice(posiciones_accesibles)

        # Retornar la posición como objeto Posicion
        return Posicion(posicion_aleatoria[0], posicion_aleatoria[1])


    @abstractmethod
    def mover_hacia_objetivo(self, pacman_posicion, grafo, delta_time):
        pass

    def mover_hacia_esquina(self):
        pass

    def draw(self, screen):
        if self.modo == self.MODO_PERSECUCION:
            self.draw_persecucion(screen)
        elif self.modo == self.MODO_DISPERSION:
            self.draw_dispersion(screen)
        elif self.modo == self.MODO_ASUSTADO:
            self.draw_asustado(screen)


    def draw_persecucion(self, screen):
        pass

    def draw_dispersion(self, screen):
        # Selecciona las imágenes de movimiento según la dirección
        if self._direccion == "izquierda":
            image_frame_1 = "tile157.png"
            image_frame_2 = "tile156.png"
        elif self._direccion == "derecha":
            image_frame_1 = "tile152.png"
            image_frame_2 = "tile153.png"
        elif self._direccion == "arriba":
            image_frame_1 = "tile158.png"
            image_frame_2 = "tile159.png"
        elif self._direccion == "abajo":
            image_frame_1 = "tile154.png"
            image_frame_2 = "tile155.png"
        else:
            image_frame_1 = "tile154.png"
            image_frame_2 = "tile155.png"

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



    def draw_asustado(self, screen):
        # Selecciona las imágenes de movimiento según la dirección
        if self._direccion == "izquierda" or self._direccion =="derecha":
            image_frame_1 = "tile070.png"
            image_frame_2 = "tile071.png"
        elif self._direccion == "arriba" or self._direccion =="abajo" :
            # Si no hay dirección (por defecto o quieto)
            image_frame_1 = "tile072.png"
            image_frame_2 = "tile073.png"
        else:
            image_frame_1 = "tile072.png"

        # Alternar entre las dos imágenes para simular movimiento
        if self.changeFeetCount % 2 == 0:
            ghostImage = pygame.image.load(os.path.join(BoardPath, image_frame_1))
        else:
            ghostImage = pygame.image.load(os.path.join(BoardPath, image_frame_2))

        self.changeFeetCount += 1

        # Escalar la imagen para adaptarla al tamaño de la celda del laberinto
        ghostImage = pygame.transform.scale(ghostImage, (int(self.square_size * 0.9), int(self.square_size * 0.9)))

        screen.blit(ghostImage, (self.posicion_inicial.get_x() * self.square_size,
                                 self.posicion_inicial.get_y() * self.square_size))


