import os
from .ElementoJuego import ElementoJuego

# Obtener la ruta absoluta del directorio raíz del proyecto (subiendo más niveles)
current_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Construir la ruta correcta hacia las imágenes
BoardPath = os.path.join(current_dir, "resorces", "ElementImages")

class Fruta(ElementoJuego):
    def __init__(self, posicion, nombre, duracion, punto ):
        super().__init__(posicion,  nombre , duracion, punto)# Llama al constructor de la clase padre

    def colisionar(self, pacman):
        """Lógica específica para la colisión de la fruta"""
        if self.posicion == pacman.get_posicion():
            pacman.colision(self.punto)
            return True
        return False




    """Cereza: 100 puntos (Nivel 1)
    Fresa: 300 puntos (Nivel 2)
    Naranja: 500 puntos (Niveles 3 y 4)
    Manzana: 700 puntos (Niveles 5 y 6)
    Uvas: 1000 puntos (Niveles 7 y 8) 1."""
