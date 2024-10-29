import os
import threading

import pygame
# Obtener la ruta absoluta del directorio raíz del proyecto (subiendo más niveles)
current_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Construir la ruta correcta hacia las imágenes
BoardPath = os.path.join(current_dir, "resorces", "ElementImages")
# Esto se podría agregar al ciclo principal del juego


MODO_PERSECUCION = "persecucion" # Para cuandso se pued apcomer la fantsma
MODO_NORMAL = "normal"
class Pacman:
    def __init__(self, velocidad, posicion, punto, square_size, laberinto):
        self.velocidad = velocidad
        self.vidas = 3
        self.posicion = posicion  # Debe ser un objeto de la clase Posicion
        self.punto = punto
        self.modo = MODO_NORMAL
        self.changeFeetCount = 0  # Contador para alternar imágenes
        self.square_size = square_size  # Tamaño del sprite
        self.laberinto = laberinto  # Referencia al laberinto
        self.colision_desactivada = False  # Nueva bandera para desactivar la colisión temporalmente
        self.ultimo_teletransporte = 0  # Guardar el tiempo del último teletransporte

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

    def colision_atajo(self, nueva_posicion):
        """Teletransporta a Pac-Man a la nueva posición del atajo."""
        self.posicion.set_x(nueva_posicion.get_x())
        self.posicion.set_y(nueva_posicion.get_y())
        self.posicion.set_direccion("derecha")  # Ajusta la dirección si es necesario
        self.colision_desactivada = True  # Desactivar colisiones temporalmente
        self.tiempo_colision_desactivada = pygame.time.get_ticks()  # Guardar el tiempo actual

    def colision_pildora(self, duracion):
        self.set_modo(MODO_PERSECUCION)
        timer = threading.Timer(duracion, self.set_modo, [MODO_NORMAL])
        timer.start()

    def mover(self, direccion, delta_time):
        """Mueve a Pac-Man en la dirección dada, teniendo en cuenta su velocidad y el tiempo transcurrido."""

        # Obtener la posición actual de Pac-Man
        x_actual = self.posicion.get_x()
        y_actual = self.posicion.get_y()

        # Crear variables para la nueva posición
        nuevo_x = x_actual
        nuevo_y = y_actual

        # Ajustar la cantidad de movimiento basado en la velocidad y el tiempo delta
        movimiento = self.velocidad * delta_time

        # Predecir la nueva posición basada en la dirección, sin cambiarla aún
        if direccion == "derecha":
            nuevo_x += movimiento
        elif direccion == "izquierda":
            nuevo_x -= movimiento
        elif direccion == "arriba":
            nuevo_y -= movimiento
        elif direccion == "abajo":
            nuevo_y += movimiento

        # Redondear la nueva posición a números enteros para asegurar que estén en la cuadrícula
        nuevo_x = round(nuevo_x)
        nuevo_y = round(nuevo_y)

        # Verificar si la nueva posición está dentro de los límites y no hay una pared
        if 0 <= nuevo_y < len(self.laberinto) and 0 <= nuevo_x < len(self.laberinto[0]):
            if self.laberinto[int(nuevo_y)][int(nuevo_x)] not in [3, 4]:  # Verificar que no haya una pared
                # Si la nueva posición es válida, actualizarla
                self.posicion.set_x(nuevo_x)
                self.posicion.set_y(nuevo_y)
                # Actualizar la dirección solo si el movimiento fue exitoso
                self.posicion.set_direccion(direccion)
            else:
                # Si hay una pared, Pac-Man sigue en la misma dirección, pero no cambia su posición
                pass
        else:
            # Si la nueva posición está fuera de los límites, no hacer nada
            pass

    def draw(self, screen):
        # Obtener la dirección actual
        direccion = self.posicion.get_direccion()

        # Elegir la imagen de Pac-Man en función de la dirección
        if direccion == "izquierda":
            image_frame_1 = "tile048.png"
            image_frame_2 = "tile050.png"
        elif direccion == "derecha":
            image_frame_1 = "tile052.png"
            image_frame_2 = "tile054.png"
        elif direccion == "arriba":
            image_frame_1 = "tile051.png"
            image_frame_2 = "tile049.png"
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
        pacmanImage = pygame.transform.scale(pacmanImage, (int(self.square_size * 1.15), int(self.square_size * 1.15)))

        # Dibujar la imagen en la posición actual de Pac-Man
        screen.blit(pacmanImage, (self.posicion.get_x() * self.square_size ,
                                  self.posicion.get_y() * self.square_size ))





