import os
import random

import pygame

from pacman.main.py.logic.Fantasma import Fantasma
from pacman.main.py.logic.Posicion import Posicion

# Obtener la ruta absoluta del directorio raíz del proyecto (subiendo más niveles)
current_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Construir la ruta correcta hacia las imágenes
BoardPath = os.path.join(current_dir, "resorces", "ElementImages")

class Inky(Fantasma):
    def __init__(self, posicion_inicial, square, velocidad, blinky ):
        super().__init__("cian", posicion_inicial, square,  velocidad)
        self.blinky = blinky  # Referencia a Blinky
        self.square_size=square




    def mover_hacia_objetivo(self, pacman_posicion, grafo, delta_time):
            if round(self.posicion_inicial.get_x()) == self.posicion_aux.get_x() and round(self.posicion_inicial.get_y()) == self.posicion_aux.get_y():
                self.first_move_to_target = True
            if self.first_move_to_target  :
                objetivo_x, objetivo_y = 13, 14
                objetivo = Posicion(objetivo_x, objetivo_y)

                # Obtener el camino hacia el objetivo inicial
                camino = grafo.bfs(
                    (round(self.posicion_inicial.get_x()), round(self.posicion_inicial.get_y())),
                    (round(objetivo.get_x()), round(objetivo.get_y()))
                )

                # Verifica si ya ha llegado exactamente a [13, 14]
                if round(self.posicion_inicial.get_x()) == objetivo_x and round(
                        self.posicion_inicial.get_y()) == objetivo_y:
                    self.first_move_to_target = False  # Desactiva la bandera si ya llegó a (13, 14)
                elif len(camino) > 1:
                    # Continuar hacia el objetivo inicial [13, 14] si aún no ha llegado
                    siguiente_x, siguiente_y = camino[1]
                    self.posicion_inicial.set_x(siguiente_x)
                    self.posicion_inicial.set_y(siguiente_y)

                    # Redondea la posición después del movimiento
                    self.posicion_inicial.set_x(round(self.posicion_inicial.get_x()))
                    self.posicion_inicial.set_y(round(self.posicion_inicial.get_y()))
                    return

                    # Verifica que self.blinky tenga una posición válida
            if self.blinky and hasattr(self.blinky, "get_posicion"):
                # Calcula el objetivo reflejando la posición de Pac-Man en relación con Blinky
                objetivo_x = pacman_posicion.get_x() + 2 * (
                            self.blinky.get_posicion().get_x() - pacman_posicion.get_x())
                objetivo_y = pacman_posicion.get_y() + 2 * (
                            self.blinky.get_posicion().get_y() - pacman_posicion.get_y())

                # Verifica si el objetivo está en una posición libre
                if grafo.es_posicion_libre(objetivo_x, objetivo_y):
                    objetivo = Posicion(objetivo_x, objetivo_y)
                else:
                    # Si el objetivo está bloqueado, establece otro objetivo (por ejemplo, Pac-Man)
                    objetivo = pacman_posicion


                # Obtiene el camino hacia el objetivo usando BFS
                camino = grafo.bfs(
                    (round(self.posicion_inicial.get_x()), round(self.posicion_inicial.get_y())),
                    (round(objetivo.get_x()), round(objetivo.get_y()))
                )


                # Establece la velocidad del fantasma (más lenta que la de Pac-Man)
                movimiento = self.velocidad * delta_time

                # Verifica si el camino tiene más de 1 punto
                if len(camino) > 1:
                    siguiente_x, siguiente_y = camino[1]
                    if grafo.es_posicion_libre(siguiente_x, siguiente_y):
                        self.objetivo = (siguiente_x, siguiente_y)
                        distancia_x = self.objetivo[0] - self.posicion_inicial.get_x()
                        distancia_y = self.objetivo[1] - self.posicion_inicial.get_y()

                        if abs(distancia_x) > abs(distancia_y):
                            self.posicion_inicial.set_x(
                                self.posicion_inicial.get_x() + (movimiento if distancia_x > 0 else -movimiento))
                            self._direccion = "derecha" if distancia_x > 0 else "izquierda"
                        else:
                            self.posicion_inicial.set_y(
                                self.posicion_inicial.get_y() + (movimiento if distancia_y > 0 else -movimiento))
                            self._direccion = "abajo" if distancia_y > 0 else "arriba"

                        # Redondeo solo cuando alcanza la posición objetivo en el camino
                        if round(self.posicion_inicial.get_x()) == self.objetivo[0] and round(
                                self.posicion_inicial.get_y()) == self.objetivo[1]:
                            self.posicion_inicial.set_x(round(self.posicion_inicial.get_x()))
                            self.posicion_inicial.set_y(round(self.posicion_inicial.get_y()))
                else:


                    self.objetivo = (pacman_posicion.get_x(), pacman_posicion.get_y())

                    # Continuar con el movimiento hacia Pac-Man si es necesario
                    distancia_x = self.objetivo[0] - self.posicion_inicial.get_x()
                    distancia_y = self.objetivo[1] - self.posicion_inicial.get_y()

                    # Mueve hacia el siguiente paso
                    if abs(distancia_x) > abs(distancia_y):
                        nueva_x = self.posicion_inicial.get_x() + (movimiento if distancia_x > 0 else -movimiento)
                        self.posicion_inicial.set_x(round(nueva_x))  # Redondea la posición en x
                        self._direccion = "derecha" if distancia_x > 0 else "izquierda"
                    else:
                        nueva_y = self.posicion_inicial.get_y() + (movimiento if distancia_y > 0 else -movimiento)
                        self.posicion_inicial.set_y(round(nueva_y))  # Redondea la posición en y
                        self._direccion = "abajo" if distancia_y > 0 else "arriba"


            else:
                print("Error: Blinky no está correctamente inicializado.")



    def draw_persecucion(self, screen):
        # Selecciona las imágenes de movimiento según la dirección
        if self._direccion == "izquierda":
            image_frame_1 = "tile140.png"
            image_frame_2 = "tile141.png"
        elif self._direccion == "derecha":
            image_frame_1 = "tile136.png"
            image_frame_2 = "tile137.png"
        elif self._direccion == "arriba":
            image_frame_1 = "tile142.png"
            image_frame_2 = "tile143.png"
        elif self._direccion == "abajo":
            image_frame_1 = "tile138.png"
            image_frame_2 = "tile139.png"
        else:
            # Si no hay dirección (por defecto o quieto)
            image_frame_1 = "tile136.png"
            image_frame_2 = "tile137.png"

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