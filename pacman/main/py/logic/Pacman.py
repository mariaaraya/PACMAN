import os
import threading

import pygame
# Obtener la ruta absoluta del directorio raíz del proyecto (subiendo más niveles)
current_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Construir la ruta correcta hacia las imágenes
BoardPath = os.path.join(current_dir, "resorces", "ElementImages")
# Esto se podría agregar al ciclo principal del juego


MODO_PERSECUCION = "persecucion"
MODO_NORMAL = "normal"
class Pacman:
    def __init__(self, velocidad, posicion, punto, square_size):
        self.velocidad = velocidad
        self.vidas = 3
        self.posicion = posicion  # Debe ser un objeto de la clase Posicion
        self.punto = punto
        self.modo = MODO_NORMAL
        self.changeFeetCount = 0  # Contador para alternar imágenes
        self.square_size = square_size  # Tamaño del sprite
    # Getters
    def get_posicion(self):
        return self.posicion

    def get_velocidad(self):
        return self.velocidad

    def get_vidas(self):
        return self.vidas

    def get_punto(self):
        return self.punto

    def get_modo(self):
        return self.modo

    # Setters
    def set_posicion(self, posicion):
        self.posicion = posicion

    def set_velocidad(self, velocidad):
        self.velocidad = velocidad

    def set_vidas(self, vidas):
        self.vidas = vidas

    def set_punto(self, punto):
        self.punto = punto

    def set_modo(self, modo):
        self.modo = modo

    def colision(self , punto):
        self.punto+= punto

    def colision_atajo(self , posicion):
       self.posicion= posicion

    def colision_pildora(self, duracion):
        self.set_modo(MODO_PERSECUCION)
        timer = threading.Timer(duracion, self.set_modo, [MODO_NORMAL])
        timer.start()

    def mover(self, direccion):
        self.posicion.set_direccion(direccion)
        if direccion == "derecha":
            self.posicion.set_x(self.posicion.get_x() + self.velocidad)
        elif direccion == "izquierda":
            self.posicion.set_x(self.posicion.get_x() - self.velocidad)
        elif direccion == "arriba":
            self.posicion.set_y(self.posicion.get_y() - self.velocidad)
        elif direccion == "abajo":
            self.posicion.set_y(self.posicion.get_y() + self.velocidad)

    def draw(self, screen):
        # Obtener la dirección actual
        direccion = self.posicion.get_direccion()

        # Elegir la imagen de Pac-Man en función de la dirección
        if direccion == "izquierda":
            image_frame_1 = "tile048.png"
            image_frame_2 = "tile059.png"
        elif direccion == "derecha":
            image_frame_1 = "tile052.png"
            image_frame_2 = "tile054.png"
        elif direccion == "arriba":
            image_frame_1 = "tile051.png"
            image_frame_2 = "tile050.png"  # Puedes ajustar el segundo frame si es diferente
        elif direccion == "abajo":
            image_frame_1 = "tile053.png"
            image_frame_2 = "tile055.png"

        # Alternar entre las dos imágenes para simular movimiento
        if self.changeFeetCount % 2 == 0:
            pacmanImage = pygame.image.load(os.path.join(BoardPath, image_frame_1))
        else:
            pacmanImage = pygame.image.load(os.path.join(BoardPath, image_frame_2))

        self.changeFeetCount += 1

        # Escalar la imagen para adaptarla al tamaño de la celda del laberinto
        pacmanImage = pygame.transform.scale(pacmanImage, (int(self.square_size * 0.9), int(self.square_size * 0.9)))

        # Dibujar la imagen en la posición actual de Pac-Man
        screen.blit(pacmanImage, (self.posicion.get_x() * self.square_size,
                                  self.posicion.get_y() * self.square_size))





