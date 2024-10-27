
class Posicion:
    def __init__(self, x=0, y=0, direccion="derecha"):
        self._x = x  # Coordenada en el eje X
        self._y = y  # Coordenada en el eje Y
        self._direccion = direccion  # Dirección de movimiento


    # Getters
    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_direccion(self):
        return self._direccion


    # Setters
    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def set_direccion(self, direccion):
        self._direccion = direccion



    def __str__(self):
        return f"Posición: ({self._x}, {self._y}) Dirección: {self._direccion} "
