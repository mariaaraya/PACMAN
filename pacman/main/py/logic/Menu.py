import pygame
import os


class Menu:
    def __init__(self, screen, background_image_path):
        self.screen = screen
        self.background_image = pygame.image.load(background_image_path)
        self.background_image = pygame.transform.scale(self.background_image, (screen.get_width(), screen.get_height()))
        self.font = pygame.font.SysFont(None, 50)
        self.small_font = pygame.font.SysFont(None, 25)  # Fuente más pequeña para el mensaje

        # Colores para las opciones del menú
        self.color_active = (255, 182, 193)  # Amarillo
        self.color_inactive = (255, 255, 255)  # Blanco

        # Opciones del menú
        self.options = ["Iniciar Juego", "Cargar Juego"]
        self.selected_option = 0

    def draw(self):
        # Dibujar la imagen de fondo
        self.screen.blit(self.background_image, (0, 0))

        # Dibujar las opciones del menú
        for i, option in enumerate(self.options):
            color = self.color_active if i == self.selected_option else self.color_inactive
            text_surface = self.font.render(option, True, color)
            x = (self.screen.get_width() - text_surface.get_width()) // 2
            y = (self.screen.get_height() // 2) + i * 60  # Espacio entre las opciones
            self.screen.blit(text_surface, (x, y))

        # Dibujar el mensaje de cierre debajo de "Cargar Juego"
        message_text = self.small_font.render("Cerrar con X para guardar la partida", True, (200, 200, 200))
        message_x = (self.screen.get_width() - message_text.get_width()) // 2
        message_y = (self.screen.get_height() // 2) + len(self.options) * 60 + 20  # Debajo de las opciones
        self.screen.blit(message_text, (message_x, message_y))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_option = (self.selected_option - 1) % len(self.options)
            elif event.key == pygame.K_DOWN:
                self.selected_option = (self.selected_option + 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                return self.options[self.selected_option]  # Devolver la opción seleccionada
        return None
