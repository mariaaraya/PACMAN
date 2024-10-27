from abc import ABC, abstractmethod
import pygame
import os
ElementPath = "pacman/main/resorces/ElementImages/"
#ElementPath = os.path.abspath(os.path.dirname(__file__), '..', 'resorces', 'ElementImages')

# Clase abstracta
class ElementoJuego(ABC):
    def __init__(self, posicion  , nombre , duracion  , punto) :
        self.posicion = posicion  # Posicion del elemento en el Pacman
        self.key = posicion # Usar la posición como clave
        self.nombre = nombre #Nombre del elemento
        self.duracion = duracion
        self.punto = punto

    # Getters
    def get_posicion(self):
        return self.posicion

    def get_key(self):
        return self.key

    def get_nombre(self):
        return self.nombre

    def get_duracion(self):
        return self.duracion

    def get_punto(self):
        return self.punto

    # Setters
    def set_posicion(self, posicion):
        self.posicion = posicion

    def set_key(self, key):
        self.key = key

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_duracion(self, duracion):
        self.duracion = duracion

    def set_punto(self, punto):
        self.punto = punto


    def draw(self, screen):
        """Método  para dibijar el elemento."""
        pass

    def obtener_ruta_imagen(self):
        """Método  para obtener la ruta de la imagen."""
        pass

    @abstractmethod
    def colisionar(self , pacman):
        """Método booleano que devuelve True si hay colisión, False en caso contrario."""
        pass


