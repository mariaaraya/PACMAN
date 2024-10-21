class Pacman:
    def __init__(self, velocidad, vidas , posicion):
        self.velocidad = velocidad  # Velocidad de movimiento
        self.vidas = vidas  # Número de vidas
        self.posicion = posicion

    # Getters
    def get_posicion(self):
        return self.posicion

    # Setters
    def set_posicion(self, posicion):
        self.posicion = posicion
