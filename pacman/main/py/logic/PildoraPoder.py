from .ElementoJuego import ElementoJuego


class PildoraPoder(ElementoJuego):
    def __init__(self, posicion, nombre, duracion):
        super().__init__(posicion,  nombre , duracion)  # Llama al constructor de la clase padre

    def colisionar(self, Pacman):
        """Lógica específica para la colisión de la píldora de poder"""
        if self.posicion == Pacman.get_posicion():
            # Aqui va el metodo de PACMAN Cuado como un pildora de poder
            return True
        return False