import pygame
from .ElementoJuego import ElementoJuego


class PildoraPoder(ElementoJuego):
    def __init__(self, posicion, nombre, duracion):
        super().__init__(posicion,  nombre , duracion, 50)  # Llama al constructor de la clase padre

    def colisionar(self, pacman):
        """Lógica específica para la colisión del Pacdot"""
        # Convertir la posición de Pac-Man a píxeles
        pacman_x = pacman.get_posicion().get_x() * pacman.square_size
        pacman_y = pacman.get_posicion().get_y() * pacman.square_size

        # Obtener la posición del Pacdot en píxeles
        objeto_x = self.posicion.get_x()
        objeto_y = self.posicion.get_y()

        # Ajustar la tolerancia de colisión
        tolerancia_colision = 11  # Ajustar según el tamaño del sprite

        # Verificar si las coordenadas de Pac-Man y el objeto están dentro de la tolerancia
        if abs(pacman_x - objeto_x) < tolerancia_colision and abs(pacman_y - objeto_y) < tolerancia_colision:
            pacman.colision_pildora(self.duracion)
            print("¡Colisión detectada con Pidora de Poder !")
            return True
        return False

    def draw(self, screen):
        """Método para dibujar la Pildora de poder en la pantalla."""
        # Define el color del Pacdot (por ejemplo, amarillo)
        color = (255, 255, 0)  # Color amarillo
        # Tamaño del Pacdot (radio del círculo)
        radio = 7 # Ajusta el tamaño
        # Dibuja un círculo en la pantalla en la posición del Pacdot
        pygame.draw.circle(screen, color,
                           (self.posicion.get_x(), self.posicion.get_y()), radio)