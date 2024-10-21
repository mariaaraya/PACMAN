from pacman.main.py.logic.Fantasma import Fantasma
from pacman.main.py.logic.Posicion import Posicion


class Pinky(Fantasma):
    def __init__(self, posicion_inicial, velocidad=1):
        super().__init__("rosa", posicion_inicial, velocidad)

    def mover_hacia_objetivo(self, pacman_posicion):
        # Lógica para que Pinky intente predecir la posición futura de Pac-Man
        futuro_x = pacman_posicion.get_x() + (
                    pacman_posicion.get_velocidad() * (1 if pacman_posicion.get_direccion() == "derecha" else -1))
        futuro_y = pacman_posicion.get_y() + (
                    pacman_posicion.get_velocidad() * (1 if pacman_posicion.get_direccion() == "abajo" else -1))

        # Establecer objetivo
        self.objetivo = Posicion(futuro_x, futuro_y)
        self._mover_hacia(self.objetivo)

    def _mover_hacia(self, objetivo):
        # Lógica para mover a Pinky hacia el objetivo
        super()._mover_hacia(objetivo)