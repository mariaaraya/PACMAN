from ElementoJuego import ElementoJuego
#from pacman.main.py.logic.ElementoJuego import ElementoJuego


class Fruta(ElementoJuego):
    def __init__(self, posicion, nombre, duracion):
        super().__init__(posicion,  nombre , duracion)  # Llama al constructor de la clase padre

    def colisionar(self, pacman):
        """Lógica específica para la colisión de la píldora de poder"""
        if self.posicion == pacman.get_posicion():
            # Aqui va el metodo de PACMAN cuando colisiona con una fruta
            return True
        return False