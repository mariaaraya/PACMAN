from abc import ABC, abstractmethod
import pygame
ElementPath = "pacman/main/resorces/ElementImages/"

# Clase abstracta
class ElementoJuego(ABC):
    def __init__(self, posicion  , nombre , duracion ) :
        self.posicion = posicion  # Posicion del elemento en el Pacman
        self.key = posicion # Usar la posición como clave
        self.nombre = nombre #Nombre del elemento
        self.duracion = duracion

    # Getters
    def get_posicion(self):
        return self.posicion

    def get_key(self):
        return self.key

    def get_nombre(self):
        return self.nombre

    def get_duracion(self):
        return self.duracion

    # Setters
    def set_posicion(self, posicion):
        self.posicion = posicion

    def set_key(self, key):
        self.key = key

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_duracion(self, duracion):
        self.duracion = duracion

    def draw(self, screen):
        ruta_imagen = self.obtener_ruta_imagen()  # Obtener la ruta de la imagen
        image = pygame.image.load(ruta_imagen)  # Cargar la imagen usando la ruta
        screen.blit(image, self.posicion)  # Dibujar la imagen en la posición especificada

    def obtener_ruta_imagen(self):
        # Asigna la ruta de la imagen en función del nombre del objeto
        if self.nombre == "cereza":
            return ElementPath + "tile081.png"
        elif self.nombre == "naranja":
            return ElementPath + "tile082.png"
        elif self.nombre == "manzana":
            return ElementPath + "tile084.png"
        elif self.nombre == "uva":
            return ElementPath + "tile085.png"
        elif self.nombre == "pacdot":
            return ElementPath + "tile002.png"
        elif self.nombre == "pildora":
            return ElementPath + "tile010.png"
        else:
            return ElementPath + "tile001.png"  # Imagen por defecto en caso de que no haya coincidencia

    @abstractmethod
    def colisionar(self , pacman):
        """Método booleano que devuelve True si hay colisión, False en caso contrario."""
        pass


