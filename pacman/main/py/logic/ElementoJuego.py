from abc import ABC, abstractmethod

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

    @abstractmethod
    def colisionar(self , Pacman):
        """Método booleano que devuelve True si hay colisión, False en caso contrario."""
        pass