from ..data.Data import Data


class Service:
    _instance = None

    @staticmethod
    def instance():
        if Service._instance is None:
            Service._instance = Service()
        return Service._instance

    def __init__(self):
        if Service._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            #Falta hacer lo metodo o clase para cargar el PACMAN
            self.data = Data()



    # Sistema Hashing
    def agregar_elemento(self, elemento):
        self.data.elementos.agregar_elemento(elemento)

    def eliminar_elemento(self, key):
        self.data.elementos.eliminar_elemento(key)

    def verificar_colisiones(self, pacman):
        return self.data.elementos.verificar_colisiones(pacman)

