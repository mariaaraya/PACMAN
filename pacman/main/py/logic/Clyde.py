from pacman.main.py.logic.Fantasma import Fantasma
from pacman.main.py.logic.Posicion import Posicion


class Clyde(Fantasma):
    def __init__(self, posicion_inicial, velocidad=1):
        super().__init__("naranja", posicion_inicial, velocidad)

    def mover_hacia_objetivo(self, pacman_posicion):
        if self.debe_alejarse(pacman_posicion):
            # Lógica para alejarse de Pac-Man
            self.objetivo = Posicion(
                self.posicion_inicial.get_x() - (pacman_posicion.get_x() - self.posicion_inicial.get_x()),
                self.posicion_inicial.get_y() - (pacman_posicion.get_y() - self.posicion_inicial.get_y()))
        else:
            self.objetivo = pacman_posicion

        self._mover_hacia(self.objetivo)

    def debe_alejarse(self, pacman_posicion):
        # Lógica para decidir si Clyde debe alejarse (ejemplo: basado en la distancia a Pac-Man)
        return True  # Puedes agregar tu lógica aquí para que Clyde se comporte de manera más errática.

    def _mover_hacia(self, objetivo):
        # Lógica para mover a Clyde hacia el objetivo
        super()._mover_hacia(objetivo)