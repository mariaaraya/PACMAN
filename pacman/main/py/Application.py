# Las imágenes fueron conseguidas desde https://github.com/DevinLeamy/Pacman

from pacman.main.py.logic.Fruta import Fruta
from pacman.main.py.logic.Pacdot import Pacdot
from pacman.main.py.logic.Pacman import Pacman
from pacman.main.py.logic.SistemaHashing import SistemaHashing
from pacman.main.py.presentation.Controller import Controller
from pacman.main.py.presentation.Model import Model
from pacman.main.py.presentation.View import View
if __name__ == "__main__":
    model = Model()
    view = View()
    controller = Controller(model, view)
    controller.run()  # Ejecuta el juego directamente en el nivel 1
