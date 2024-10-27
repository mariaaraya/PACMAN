from .ElementoJuego import ElementoJuego


class AtajoLaberinto(ElementoJuego):
    def __init__(self, posicion, nombre):
        super().__init__(posicion, nombre , -1,0)  # Llama al constructor de la clase padre

    def colisionar(self, pacman ):
        """Lógica específica para la colisión de la píldora de poder"""
        if self.posicion == pacman.get_posicion():
            # Aqui va el metodo de PACMAN Cuado como un pildora de poder
            return True
        return False