from pacman.main.py.logic.SistemaHashing import SistemaHashing

class Data:
    def __init__(self):
        self.elementos = SistemaHashing()  # Crear una nueva instancia de SistemaHashing

    # Getters
    def get_Elementos(self):
        return self.elementos

    # Setters
    def set_Elementos(self, elementos):
        self.elementos = elementos

"""clase de gestión de datos que encapsula una instancia de SistemaHashing"""