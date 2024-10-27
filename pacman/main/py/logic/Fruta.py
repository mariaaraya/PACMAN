from .ElementoJuego import ElementoJuego
import pygame

class Fruta(ElementoJuego):
    def __init__(self, posicion, nombre, duracion, punto ):
        super().__init__(posicion,  nombre , duracion, punto)# Llama al constructor de la clase padre

    def colisionar(self, pacman):
        """Lógica específica para la colisión de la fruta"""
        if self.posicion == pacman.get_posicion():
            pacman.colision(self.punto)
            return True
        return False


    def draw(self, screen):
        """Método  para dibijar el elemento."""
        pass

    def obtener_ruta_imagen(self):
        """Método  para obtener la ruta de la imagen."""
        pass


    """Cereza: 100 puntos (Nivel 1)
    Fresa: 300 puntos (Nivel 2)
    Naranja: 500 puntos (Niveles 3 y 4)
    Manzana: 700 puntos (Niveles 5 y 6)
    Uvas: 1000 puntos (Niveles 7 y 8) 1."""
