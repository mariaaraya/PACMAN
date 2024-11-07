# Las imágenes fueron conseguidas desde https://github.com/DevinLeamy/Pacman
from pacman.main.py.logic.Laberinto import Laberinto
from pacman.main.py.logic.Pacman import Pacman
from pacman.main.py.logic.Posicion import Posicion



# Llama a esta función en tu código principal


if __name__ == "__main__":

    #model = Model()
    #view = View()
    #controller = Controller(model, view)
    #controller.run()  # Ejecuta el juego directamente en el nivel 1
    laberinto = Laberinto()
    #laberinto.visualizar_grafo()
    laberinto.run()

    """posiciones_libres = laberinto.obtener_posiciones_libres()
    for posicion in posiciones_libres:
        print("Poeicion libre:",posicion)

    pacman = Pacman(velocidad=1, posicion=Posicion(5, 4, "derecha"), punto=0, square_size=20,
                   laberinto=laberinto.laberinto)
    posicion_actual_pacman = pacman.get_posicion()

    print("Posición actual de Pac-Man:", (posicion_actual_pacman.get_x(), posicion_actual_pacman.get_y()))"""

