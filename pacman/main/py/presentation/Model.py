from pacman.main.py.logic.SistemaHashing import SistemaHashing


class Model:
    def __init__(self):
        self._elementos = SistemaHashing()
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self, event):
        for observer in self._observers:
            observer.update(event)

    @property
    def elementos(self):
        return self._elementos

    @elementos.setter
    def elementos(self, value):
        self._elementos = value
        self.notify_observers("elementos_changed")

    def update(self):
        # Lógica para actualizar los datos del juego
        pass
