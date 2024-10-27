import threading

MODO_PERSECUCION = "persecucion"
MODO_NORMAL = "normal"
class Pacman:
    def __init__(self, velocidad , posicion , punto ):
        self.velocidad = velocidad  # Velocidad de movimiento
        self.vidas = 3
        self.posicion = posicion
        self.punto = punto
        self.modo = MODO_NORMAL

    # Getters
    def get_posicion(self):
        return self.posicion

    def get_velocidad(self):
        return self.velocidad

    def get_vidas(self):
        return self.vidas

    def get_punto(self):
        return self.punto

    def get_modo(self):
        return self.modo

    # Setters
    def set_posicion(self, posicion):
        self.posicion = posicion

    def set_velocidad(self, velocidad):
        self.velocidad = velocidad

    def set_vidas(self, vidas):
        self.vidas = vidas

    def set_punto(self, punto):
        self.punto = punto

    def set_modo(self, modo):
        self.modo = modo

    def colision(self , punto):
        self.punto+= punto

    def colision_atajo(self , posicion):
       self.posicion= posicion

    def colision_pildora(self, duracion):
        self.set_modo(MODO_PERSECUCION)
        timer = threading.Timer(duracion, self.set_modo, [MODO_NORMAL])
        timer.start()

    def mover(self, direccion):
        self.posicion.set_direccion(direccion)
        if direccion == "derecha":
            self.posicion.set_x(self.posicion.get_x() + self.velocidad)
        elif direccion == "izquierda":
            self.posicion.set_x(self.posicion.get_x() - self.velocidad)
        elif direccion == "arriba":
            self.posicion.set_y(self.posicion.get_y() - self.velocidad)
        elif direccion == "abajo":
            self.posicion.set_y(self.posicion.get_y() + self.velocidad)