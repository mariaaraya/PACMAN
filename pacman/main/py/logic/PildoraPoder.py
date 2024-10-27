import pygame
from .ElementoJuego import ElementoJuego


class PildoraPoder(ElementoJuego):
    def __init__(self, posicion, nombre, duracion):
        super().__init__(posicion,  nombre , duracion, 50)  # Llama al constructor de la clase padre

    def colisionar(self, pacman):
        """Lógica específica para la colisión de la píldora de poder"""
        if self.posicion == pacman.get_posicion():
            pacman.colision_pildora(self.duracion)
            return True
        return False

    def draw(self, screen):
        """Método para dibujar la Pildora de poder en la pantalla."""
        # Define el color del Pacdot (por ejemplo, amarillo)
        color = (255, 255, 0)  # Color amarillo
        # Tamaño del Pacdot (radio del círculo)
        radio = 8  # Ajusta el tamaño
        # Dibuja un círculo en la pantalla en la posición del Pacdot
        pygame.draw.circle(screen, color, self.posicion, radio)