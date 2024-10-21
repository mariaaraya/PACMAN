import pygame

from pacman.main.py.logic.Pacdot import Pacdot


class Controller:
    def __init__(self, model , view):
        self.model = model
        self.view = view
        view.set_Model(model)
        view.set_Controller(self)

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.model.elementos = "Nuevo valor de elementos"


    def agregarElemento(self, elemento):
        self.model.elementos.append(elemento)

    def agregar_elementos_pacdot(self):
        """Crea y agrega varios Pacdots en diferentes posiciones."""
        ancho_ventana, alto_ventana = 800, 600
        separacion = 50

        # Generar Pacdots por toda la ventana
        for x in range(0, ancho_ventana, separacion):
            for y in range(0, alto_ventana, separacion):
                pacdot = Pacdot((x, y), "pacdot")  # Crea un Pacdot en la posición (x, y)
                self.model.elementos.agregar_elemento(pacdot)  # Agrega el Pacdot al sistema de elementos