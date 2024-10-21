from pacman.main.py.logic.Fantasma import Fantasma


class Blinky(Fantasma):
    def __init__(self, posicion_inicial, velocidad = 1):
        super().__init__("rojo",posicion_inicial, velocidad)

    def mover_hacia_objetivo(self, pacman_posicion):
        # Lógica para que Blinky persiga a Pac-Man
        self.objetivo = pacman_posicion
        # Aquí podrías agregar la lógica para moverlo hacia el objetivo
        self._mover_hacia(self.objetivo)

    def _mover_hacia(self, objetivo):
        # Lógica para mover al fantasma hacia el objetivo (Pac-Man)
        if self.posicion_inicial.get_x() < objetivo.get_x():
            self.posicion_inicial.set_x(self.posicion_inicial.get_x() + self.velocidad)
        elif self.posicion_inicial.get_x() > objetivo.get_x():
            self.posicion_inicial.set_x(self.posicion_inicial.get_x() - self.velocidad)

        if self.posicion_inicial.get_y() < objetivo.get_y():
            self.posicion_inicial.set_y(self.posicion_inicial.get_y() + self.velocidad)
        elif self.posicion_inicial.get_y() > objetivo.get_y():
            self.posicion_inicial.set_y(self.posicion_inicial.get_y() - self.velocidad)