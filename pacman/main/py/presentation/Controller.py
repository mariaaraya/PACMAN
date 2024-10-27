import pygame

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.set_Model(model)
        self.view.set_Controller(self)
        self.running = True
        self.clock = pygame.time.Clock()

    def run(self):
        while self.running:
            self.clock.tick(40)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.view.draw()

