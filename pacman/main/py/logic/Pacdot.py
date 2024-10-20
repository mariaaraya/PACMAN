from .ElementoJuego import ElementoJuego


class Pacdot(ElementoJuego):
    def __init__(self, posicion, nombre):
        super().__init__(posicion,  nombre , -1)  # Llama al constructor de la clase padre

    def colisionar(self, Pacman):
        """Lógica específica para la colisión de la píldora de poder"""
        if self.posicion == Pacman.get_posicion():
            # Aqui va el metodo de PACMAN cuando colisiona con una Pacdot
            return True
        return False