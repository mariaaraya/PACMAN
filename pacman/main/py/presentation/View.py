import pygame
import os

# Obtener la ruta absoluta del directorio raíz del proyecto (subiendo más niveles)
current_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Construir la ruta correcta hacia las imágenes
BoardPath = os.path.join(current_dir, "resorces", "BoardImages")
ElementPath = os.path.join(current_dir, "resorces", "ElementImages")

# Imprimir las rutas para verificar
print(f"Ruta BoardPath: {BoardPath}")
print(f"Ruta ElementPath: {ElementPath}")

# Inicializar pygame
pygame.init()

class View:
    def __init__(self):
        self.model = None
        self.controller = None
        self.square = 25  # Tamaño de cada cuadrado ajustado al tamaño de las imágenes
        self.width, self.height = (28 * self.square, 31 * self.square)  # Ajustar al tamaño del laberinto y las imágenes
        self.screen = pygame.display.set_mode((self.width, self.height))

    def set_Model(self, model):
        self.model = model

    def set_Controller(self, controller):
        self.controller = controller

    def draw(self):
        self.screen.fill((0, 0, 0))  # Limpiar pantalla
        self.drawMaze()
        pygame.display.flip()  # Actualizar la pantalla

    def drawMaze(self):
        for row in range(len(self.model.laberinto)):
            for col in range(len(self.model.laberinto[row])):
                if self.model.laberinto[row][col] == 3:  # Dibujar paredes
                    # Construir la ruta completa de la imagen de forma segura
                    image_path = os.path.join(BoardPath, "tile003.png")

                    # Verificar si el archivo existe
                    if not os.path.exists(image_path):
                        print(f"Archivo no encontrado: {image_path}")
                    else:
                        print(f"Archivo encontrado: {image_path}")
                        image = pygame.image.load(image_path)  # Cargar la imagen desde la ruta ajustada
                        image = pygame.transform.scale(image, (self.square, self.square))
                        self.screen.blit(image, (col * self.square, row * self.square))
                elif self.model.laberinto[row][col] == 2:  # Dibujar caminos
                    pygame.draw.rect(self.screen, (0, 0, 0),
                                     (col * self.square, row * self.square, self.square, self.square))
