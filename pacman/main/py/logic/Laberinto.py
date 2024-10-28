import os

import pygame
from pacman.main.py.logic.Pacman import Pacman
from pacman.main.py.logic.Clyde import Clyde
from pacman.main.py.logic.Inky import Inky
from pacman.main.py.logic.Pacdot import Pacdot
from pacman.main.py.logic.PildoraPoder import PildoraPoder
from pacman.main.py.logic.Pinky import Pinky
from pacman.main.py.logic.Posicion import Posicion
from pacman.main.py.logic.SistemaHashing import SistemaHashing
from pacman.main.py.logic.Blinky import Blinky
# Obtener la ruta absoluta del directorio raíz del proyecto (subiendo más niveles)
current_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Construir la ruta correcta hacia las imágenes
BoardPath = os.path.join(current_dir, "resorces", "BoardImages")

class Laberinto:
    def __init__(self):
        self.laberinto = [
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3],
            [3, 2, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 2, 3],
            [3, 6, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 6, 3],
            [3, 2, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 2, 3],
            [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3],
            [3, 2, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 2, 3],
            [3, 2, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 2, 3],
            [3, 2, 2, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2, 2, 2, 3],
            [3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 1, 3, 3, 1, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 1, 3, 3, 1, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 3, 2, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 2, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 3, 2, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 2, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 3, 2, 3, 3, 1, 3, 4, 4, 4, 4, 4, 4, 3, 1, 3, 3, 2, 3, 3, 3, 3, 3, 3],
            [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 3, 4, 4, 4, 4, 4, 4, 3, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1],  # Middle Lane Row: 14
            [3, 3, 3, 3, 3, 3, 2, 3, 3, 1, 3, 4, 4, 4, 4, 4, 4, 3, 1, 3, 3, 2, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 3, 2, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 2, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 3, 2, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 2, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 3, 2, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 2, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 3, 2, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 2, 3, 3, 3, 3, 3, 3],
            [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3],
            [3, 2, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 2, 3],
            [3, 2, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 2, 3],
            [3, 6, 2, 2, 3, 3, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 2, 2, 6, 3],
            [3, 3, 3, 2, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 2, 3, 3, 3],
            [3, 3, 3, 2, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 2, 3, 3, 3],
            [3, 2, 2, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2, 2, 2, 3],
            [3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3],
            [3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3],
            [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3],
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        ]
        self.square_size = 20  # Tamaño de cada celda en píxeles
        self.width = len(self.laberinto[0]) * self.square_size
        self.height = len(self.laberinto) * self.square_size
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.elementos= SistemaHashing()
        self.blinky = Blinky([11, 12], self.square_size)
        self.clycde = Clyde([11, 11], self.square_size)
        self.inky = Inky([12, 12], self.square_size, self.blinky)
        self.pinky = Pinky([13, 13], self.square_size)
        self.pacman = Pacman(1, Posicion(14, 20), 0, self.square_size)

    def agregar_elementos(self):
        """Agrega los Pacdots, Pildoras de Poder al sistema basado en el laberinto. Los fantasmas se crean directamente."""
        # Inicializamos las variables que controlan si los fantasmas ya han sido agregados
        blinky_added = False
        clyde_added = False
        inky_added = False
        pinky_added = False

        self.fantasmas = []  # Lista para almacenar los fantasmas

        for row in range(len(self.laberinto)):
            for col in range(len(self.laberinto[row])):
                cell_value = self.laberinto[row][col]
                x = col * self.square_size + self.square_size // 2  # Centrar los objetos en la celda
                y = row * self.square_size + self.square_size // 2

                if cell_value == 2:  # Pacdot (camino)
                    pacdot = Pacdot((x, y), 'Pacdot')
                    self.elementos.agregar_elemento(pacdot)
                elif cell_value == 6:  # Pildora de Poder (especial)
                    pildora_poder = PildoraPoder((x, y), 'PildoraPoder', 10)
                    self.elementos.agregar_elemento(pildora_poder)
                elif cell_value == 4:  # Fantasmas
                    # Agregar cada fantasma solo si no ha sido agregado ya
                    if not blinky_added:
                        self.fantasmas.append(Blinky([col, row], self.square_size))
                        blinky_added = True
                    elif not clyde_added:
                        self.fantasmas.append(Clyde([col, row], self.square_size))
                        clyde_added = True
                    elif not inky_added:
                        self.fantasmas.append(
                            Inky([col, row], self.square_size, self.blinky))  # Pasamos referencia a Blinky si necesario
                        inky_added = True
                    elif not pinky_added:
                        self.fantasmas.append(Pinky([col, row], self.square_size))
                        pinky_added = True

    def draw(self):
        # Colores para los diferentes elementos del laberinto
        color_wall = (0, 0, 255)  # Azul para las paredes
        currentTile = 0  # Contador de casillas para numeración

        # Dibujar las paredes (con imágenes si es necesario)
        for row in range(3 , len(self.laberinto)-2):
            for col in range(len(self.laberinto[row])):
                cell_value = self.laberinto[row][col]
                x = col * self.square_size
                y = row * self.square_size

                if cell_value == 3:  # Pared
                    imageName = str(currentTile)
                    if len(imageName) == 1:
                        imageName = "00" + imageName
                    elif len(imageName) == 2:
                        imageName = "0" + imageName

                    imageName = "tile" + imageName + ".png"
                    tileImagePath = os.path.join(BoardPath, imageName)
                    try:
                        # Intentar cargar la imagen de la pared
                        tileImage = pygame.image.load(tileImagePath)
                        tileImage = pygame.transform.scale(tileImage, (self.square_size, self.square_size))
                        self.screen.blit(tileImage, (x, y, self.square_size, self.square_size))
                    except FileNotFoundError:
                        print(f"Imagen no encontrada: {tileImagePath}")
                        # O podrías dibujar un color por defecto para las paredes si falta la imagen:
                        pygame.draw.rect(self.screen, color_wall, (x, y, self.square_size, self.square_size))

                currentTile += 1  # Incrementar el número de la casilla

        # Dibujar todos los elementos del sistema de hashing
        for elemento in self.elementos.obtener_todos_los_elementos():
            elemento.draw(self.screen)
        # Dibujar los fantasmas
        for fantasma in self.fantasmas:
            fantasma.draw(self.screen)
        # Dibujar Pac-Man
        self.pacman.draw(self.screen)


    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        self.agregar_elementos()  # Agregar los elementos una vez al iniciar
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill((0, 0, 0))  # Limpiar pantalla
            self.draw()  # Dibujar el laberinto y los elementos
            pygame.display.update()  # Actualizar la pantalla

            clock.tick(60)
        pygame.quit()

