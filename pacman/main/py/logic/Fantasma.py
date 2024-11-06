from abc import ABC, abstractmethod

class Fantasma (ABC):
    MODO_PERSECUCION = "persecucion"
    MODO_DISPERSION = "dispersión"
    MODO_ASUSTADO = "asustado"

    def __init__(self, color, posicion_inicial, square , velocidad = 1):
        self.color = color
        self.posicion_inicial = posicion_inicial
        self.posicion_actual = posicion_inicial  # Posición actual del fantasma
        self.velocidad = velocidad
        self.objetivo = None
        self.modo = self.MODO_PERSECUCION
        self.square_size = square
        self.changeFeetCount = 0
        self.path_to_target = []  # Camino actual hacia el objetivo

    @abstractmethod
    def mover_hacia_objetivo(self, pacman_posicion , grafo, delta_time):
        pass

    def actualizar_modo(self, nuevo_modo):
        self.objetivo = nuevo_modo

    def mover(self, pacman_posicion , grafo, delta_time):
        if self.modo == self.MODO_PERSECUCION:
            self.mover_hacia_objetivo(pacman_posicion, grafo, delta_time)
        elif self.modo == self.MODO_DISPERSION:
            self.mover_hacia_esquina()  # Implementa este método
        elif self.modo == self.MODO_ASUSTADO:
            self.mover_aleatoriamente()  # Implementa este método

    def mover_aleatoriamente(self):
        pass

    def mover_hacia_esquina(self):
        pass

    def draw(self, screen):
        """Método  para dibijar el elemento."""
        pass

