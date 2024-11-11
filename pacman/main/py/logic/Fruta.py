import os
import pygame
from .ElementoJuego import ElementoJuego

# Obtener la ruta absoluta del directorio raíz del proyecto (subiendo más niveles)
current_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Construir la ruta correcta hacia las imágenes
BoardPath = os.path.join(current_dir, "resorces", "ElementImages")

class Fruta(ElementoJuego):
    def __init__(self, posicion, nombre, duracion, punto , square_size):
        super().__init__(posicion,  nombre , duracion, punto)# Llama al constructor de la clase padre
        self.square_size = square_size  # Añadir el atributo square_size

    def colisionar(self, pacman):
        # Obtener la posición de Pac-Man en la cuadrícula
        pacman_x = pacman.get_posicion().get_x()  # Coordenada X en la cuadrícula
        pacman_y = pacman.get_posicion().get_y()  # Coordenada Y en la cuadrícula
        # Obtener la posición del objeto (Pacdot o Fruta) en la cuadrícula
        objeto_x = self.posicion.get_x()  # Coordenada X del objeto en la cuadrícula
        objeto_y = self.posicion.get_y()  # Coordenada Y del objeto en la cuadrícula
        # Imprimir las posiciones de Pac-Man y el objeto
        # Definir una tolerancia en la distancia (por ejemplo, 1 celda de diferencia)
        tolerancia = 1  # Puedes ajustar la tolerancia según el tamaño de las celdas

        # Verificar si Pac-Man está en una posición cercana (dentro de la tolerancia)
        if abs(pacman_x - objeto_x) <= tolerancia and abs(pacman_y - objeto_y) <= tolerancia:
            pacman.colision(self.punto)
            return True
        return False

    def draw(self, screen):
        if self.nombre == "Cereza":
            image_frame = "tile080.png"
        elif self.nombre == "Fresa":
            image_frame = "tile081.png"
        elif self.nombre == "Naranja":
            image_frame = "tile082.png"
        elif self.nombre == "Manzana":
            image_frame = "tile084.png"
        elif self.nombre == "Uvas":
            image_frame = "tile085.png"

        frutImage = pygame.image.load(os.path.join(BoardPath, image_frame))
        frutImage = pygame.transform.scale(frutImage, (int(self.square_size * 0.9), int(self.square_size * 0.9)))

        screen.blit(frutImage, (self.posicion.get_x() * self.square_size, self.posicion.get_y() * self.square_size))

    """Cereza: 100 puntos (Nivel 1)
    Fresa: 300 puntos (Nivel 2)
    Naranja: 500 puntos (Niveles 3 y 4)
    Manzana: 700 puntos (Niveles 5 y 6)
    Uvas: 1000 puntos (Niveles 7 y 8) 1."""
