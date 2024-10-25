# Las imágenes fueron conseguidas desde https://github.com/DevinLeamy/Pacman

from pacman.main.py.logic.Fruta import Fruta
from pacman.main.py.logic.Pacdot import Pacdot
from pacman.main.py.logic.Pacman import Pacman
from pacman.main.py.logic.SistemaHashing import SistemaHashing
from pacman.main.py.presentation.Controller import Controller
from pacman.main.py.presentation.Model import Model
from pacman.main.py.presentation.View import View
"""import pygame

from pacman.main.py.logic.Fruta import Fruta
from pacman.main.py.logic.Pacdot import Pacdot
from pacman.main.py.logic.Pacman import Pacman
from pacman.main.py.logic.SistemaHashing import SistemaHashing
from pacman.main.py.presentation.Controller import Controller
from pacman.main.py.presentation.Model import Model
from pacman.main.py.presentation.View import View

def main():
    fruta = Fruta(posicion=(1, 1),  nombre="Manzana", duracion=10)
    pera = Fruta(posicion=(10, 1), nombre="Pera", duracion=10)
    pacdot = Pacdot(posicion=(2, 2) , nombre="Pacdot")
    pacman = Pacman(1,2 ,(1,1))

    # Crear el sistema de hashing y agregar elementos
    sistema_hashing = SistemaHashing()
    sistema_hashing.agregar_elemento(fruta)
    sistema_hashing.agregar_elemento(pera)
    sistema_hashing.agregar_elemento(pacdot)

    # Verificar colisiones
    colisiones = sistema_hashing.verificar_colisiones(pacman)
    print(f"Elementos colisionados: {colisiones}")

  # Imprimir todos los elementos en el sistema de hashing
    sistema_hashing.imprimir_elementos()

    # Inicializar el modelo


    model = Model()

    # Inicializar la vista
    view = View()

    # Inicializar el controlador con el modelo y la vista
    controller = Controller(model, view)

    # Asignar el modelo y el controlador a la vista
    view.set_Model(model)
    view.set_Controller(controller)

    # Puedes agregar algunos elementos iniciales si lo deseas
    view.agregar_elementos_pacdot()  # Agregar pacdots en toda la ventana

    running = True
    while running:
        for event in pygame.event.get():
            controller.handle_event(event)
        model.update()
        view.draw()

if __name__ == "__main__":
    main()"""

if __name__ == "__main__":
    model = Model()
    view = View()
    controller = Controller(model, view)
    controller.run()  # Ejecuta el juego directamente en el nivel 1
