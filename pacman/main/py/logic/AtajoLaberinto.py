import pygame

from .ElementoJuego import ElementoJuego
from .Posicion import Posicion


class AtajoLaberinto(ElementoJuego):
    def __init__(self, posicion, nombre):
        super().__init__(posicion, nombre , -1,0)  # Llama al constructor de la clase padre

    def colisionar(self, pacman):
        tiempo_actual = pygame.time.get_ticks()

        # Verificar si Pac-Man ha sido teletransportado recientemente
        if tiempo_actual - pacman.ultimo_teletransporte < 1000:  # 1 segundo de cooldown
            return False

        # Obtener la posición actual de Pac-Man y convertir a enteros
        pacman_x = int(pacman.get_posicion().get_x())
        pacman_y = int(pacman.get_posicion().get_y())

        # Definir las posiciones de los atajos (izquierdo y derecho)
        atajo_izquierdo_x, atajo_izquierdo_y = 0, 17
        atajo_derecho_x, atajo_derecho_y = 27, 17

        # Verificar si Pac-Man colisiona con el atajo izquierdo
        if pacman_x == atajo_izquierdo_x and pacman_y == atajo_izquierdo_y:

            # Si está en el atajo izquierdo, teletransportarlo al atajo derecho
            pacman.colision_atajo(Posicion(atajo_derecho_x, atajo_derecho_y))
            pacman.ultimo_teletransporte = tiempo_actual  # Actualizar el tiempo del teletransporte

            return True
        # Verificar si Pac-Man colisiona con el atajo derecho
        elif pacman_x == atajo_derecho_x and pacman_y == atajo_derecho_y:

            # Si está en el atajo derecho, teletransportarlo al atajo izquierdo
            pacman.colision_atajo(Posicion(atajo_izquierdo_x, atajo_izquierdo_y))
            pacman.ultimo_teletransporte = tiempo_actual  # Actualizar el tiempo del teletransporte

            return True
        return False

"""representación de un atajo en el laberinto en el juego de Pacman.
 Los atajos permiten a Pacman teletransportarse entre dos puntos del laberinto, 
 y esta clase se encarga de gestionar esa mecánica."""