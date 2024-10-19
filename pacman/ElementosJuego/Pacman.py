class Pacman:
    def __init__(self, velocidad, vidas):
        self.velocidad = velocidad  # Velocidad de movimiento
        self.vidas = vidas  # Número de vidas

    def comerPunto(self):
        print("Punto comido. Suma de puntos.")

    def comerFruta(self):
        print("Fruta comida. Ganancia de puntos extra.")

    def comerPildoraPoder(self):
        print("Pildora de poder comida. Ahora eres invencible por un tiempo.")
