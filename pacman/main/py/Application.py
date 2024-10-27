# Las imágenes fueron conseguidas desde https://github.com/DevinLeamy/Pacman
from pacman.main.py.logic.Laberinto import Laberinto

if __name__ == "__main__":
    #model = Model()
    #view = View()
    #controller = Controller(model, view)
    #controller.run()  # Ejecuta el juego directamente en el nivel 1
    laberinto = Laberinto()
    laberinto.run()

