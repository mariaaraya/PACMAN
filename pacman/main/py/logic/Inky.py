from pacman.main.py.logic.Fantasma import Fantasma


class Inky(Fantasma):
    def __init__(self, posicion_inicial, blinky, velocidad=1):
        super().__init__("cian", posicion_inicial, velocidad)
        self.blinky = blinky  # Referencia a Blinky

    def mover_hacia_objetivo(self, pacman_posicion):
        # Lógica para que Inky use la posición de Pac-Man y Blinky
        blinky_pos = self.blinky.posicion_inicial
        objetivo_x = pacman_posicion.get_x() + (blinky_pos.get_x() - pacman_posicion.get_x())
        objetivo_y = pacman_posicion.get_y() + (blinky_pos.get_y() - pacman_posicion.get_y())

        self.objetivo = Posicion(objetivo_x, objetivo_y)
        self._mover_hacia(self.objetivo)

    def _mover_hacia(self, objetivo):
        # Lógica para mover a Inky hacia el objetivo
        super()._mover_hacia(objetivo)