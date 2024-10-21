import pygame

class View:
    def __init__(self):
        self.model = None
        self.controller = None
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))  # Ajusta los valores según el tamaño de tu ventana

    def set_Model(self, model):
        self.model = model
        self.model.add_observer(self)  # Añadir la vista como observador después de asignar el modelo

    def set_Controller(self, controller):
        self.controller = controller

    def update(self, event):
        if event == "elementos_changed":
            self.draw()

    def draw(self):
        self.screen.fill((0, 0, 0))  # Limpiar pantalla

        # Dibujar todos los elementos
        for elemento in self.model.elementos.obtener_todos_los_elementos():
           elemento.draw(self.screen)

        pygame.display.flip()  # Actualizar la pantalla
        pygame.display.set_caption('Pacman')

    def agregar_elementos_pacdot(self):
        """Llama al método del controlador para agregar Pacdots en diferentes posiciones."""
        self.controller.agregar_elementos_pacdot()  # Utiliza el método del controlador para agregar Pacdots

