from abc import ABC, abstractmethod

class Fantasma (ABC):
    MODO_PERSECUCION = "persecucion"
    MODO_DISPERSION = "dispersión"
    MODO_ASUSTADO = "asustado"

    def __init__(self, color, posicion_inicial, velocidad = 1):
        self.color = color
        self.posicion_inicial = posicion_inicial
        self.velocidad = velocidad
        self.objetivo = None
        self.modo = self.MODO_PERSECUCION

    @abstractmethod
    def mover_hacia_objetivo(self, pacman_posicion):
        pass

    def actualizar_modo(self, nuevo_modo):
        self.objetivo = nuevo_modo

    def mover(self, pacman_posicion):
        if self.modo == self.MODO_PERSECUCION:
            self.mover_hacia_objetivo(pacman_posicion)
        elif self.modo == self.MODO_DISPERSION:
            self.mover_hacia_esquina()  # Implementa este método
        elif self.modo == self.MODO_ASUSTADO:
            self.mover_aleatoriamente()  # Implementa este método

    def mover_aleatoriamente(self):
        pass

    def mover_hacia_esquina(self):

        pass