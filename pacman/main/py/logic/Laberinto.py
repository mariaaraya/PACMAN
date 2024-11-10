import os
import copy
import threading

import pygame
import random
from pacman.main.py.logic.AtajoLaberinto import AtajoLaberinto
from pacman.main.py.logic.Fruta import Fruta
from pacman.main.py.logic.Menu import Menu
from pacman.main.py.logic.Pacman import Pacman
from pacman.main.py.logic.Clyde import Clyde
from pacman.main.py.logic.Inky import Inky
from pacman.main.py.logic.Pacdot import Pacdot
from pacman.main.py.logic.PildoraPoder import PildoraPoder
from pacman.main.py.logic.Pinky import Pinky
from pacman.main.py.logic.Posicion import Posicion
from pacman.main.py.logic.SistemaHashing import SistemaHashing
from pacman.main.py.logic.Blinky import Blinky
from pacman.main.py.logic.Grafo import Grafo
# Obtener la ruta absoluta del directorio raíz del proyecto (subiendo más niveles)
current_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Construir la ruta correcta hacia las imágenes
BoardPath = os.path.join(current_dir, "resorces", "BoardImages")
SpriteSheets = os.path.join(current_dir, "resorces", "SpriteSheets")
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
        self.grafo = Grafo(self.laberinto)
        self.width = len(self.laberinto[0]) * self.square_size
        self.height = len(self.laberinto) * self.square_size
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.elementos= SistemaHashing()
        self.blinky = Blinky(Posicion(11, 12), self.square_size,1)
        self.clyde = Clyde(Posicion(11, 11), self.square_size,1,1)
        self.inky = Inky(Posicion(12, 12), self.square_size, 1, self.blinky)
        self.pinky = Pinky(Posicion(13, 13), self.square_size, 4)
        self.pacman = Pacman(15, Posicion(14, 26), 0, self.square_size, self)
        self.nivel = 1  # Nivel actual del juego
        self.max_nivel = 3  # Número máximo de niveles
        self.laberinto_original = copy.deepcopy(self.laberinto)
        self.laberinto_backup = copy.deepcopy(self.laberinto)  # Crea una copia de respaldo inicial
        self.agregar_elementos()

    def obtener_matriz(self):
        return self.laberinto

    def activar_modo_asustado(self, duracion):
        """Activa el modo asustado en todos los fantasmas y el modo persecución en Pac-Man por una duración específica."""
        # Cambiar el modo de los fantasmas a asustado
        for fantasma in self.fantasmas:
            fantasma.actualizar_modo("asustado")

        # Cambiar el modo de Pac-Man a persecución
        self.pacman.set_modo("persecucion")

        # Programar el regreso al modo normal después de la duración especificada
        threading.Timer(duracion, self.desactivar_modo_asustado).start()

    def desactivar_modo_asustado(self):
        """Vuelve todos los fantasmas al modo persecución y Pac-Man al modo normal."""
        # Cambiar el modo de los fantasmas a persecución
        for fantasma in self.fantasmas:
            fantasma.actualizar_modo("persecucion")

        # Cambiar el modo de Pac-Man a normal
        self.pacman.set_modo("normal")

    def obtener_posiciones_libres(self):
        posiciones = []
        for y, fila in enumerate(self.laberinto):
            for x, celda in enumerate(fila):
                if celda != 3:  # Verifica si la celda no es una pared
                    posiciones.append((x, y))
        return posiciones

    def crear_fruta_segun_nivel(self, nivel, posicion_fruta):
        # Definir la fruta y los puntos según el nivel
        if nivel == 1:
            nombre_fruta = "Cereza"
            puntos_fruta = 100
        elif nivel == 2:
            nombre_fruta = "Fresa"
            puntos_fruta = 300
        elif nivel in [3]:
            nombre_fruta = "Naranja"
            puntos_fruta = 500
        else:
            nombre_fruta = "Cereza"  # Por defecto
            puntos_fruta = 100

        # Crear el objeto Fruta pasando el square_size
        fruta = Fruta(Posicion(posicion_fruta[0], posicion_fruta[1]), nombre_fruta, 15, puntos_fruta, self.square_size)
        # Actualizar la matriz en la posición donde se coloca la fruta
        self.laberinto[posicion_fruta[1]][posicion_fruta[0]] = 2  # Cambia el valor de la celda a 2
        return fruta

    def generar_posicion_fruta(self):
        posiciones_validas = []
        for row in range(len(self.laberinto)):
            for col in range(len(self.laberinto[row])):
                if self.laberinto[row][col] == 1:  # Solo posiciones con valor 1
                    posiciones_validas.append((col, row))

        if posiciones_validas:
            return random.choice(posiciones_validas)  # Devolver una posición aleatoria
        return None

    def reiniciar_laberinto(self):
        self.elementos.vaciar()
        self.imprimir_elementos_restantes()
        self.pacman.set_posicion(Posicion(14, 26))
        self.laberinto = copy.deepcopy(self.laberinto_original)  # Reiniciar el laberinto con una copia profunda
        self.agregar_elementos()  # Reagregar los elementos del laberinto

    def posion_original(self):
         self.pacman.set_posicion(Posicion(14, 26))
         self.agregar_elementos()  # Reagregar los elementos del laberinto
         for fantasma in self.fantasmas:
           fantasma.reiniciar_posicion()


    def imprimir_elementos_restantes(self):
        """Imprime los elementos restantes en el sistema de hashing para debug."""
        print("Elementos restantes en el laberinto:")
        for elemento in self.elementos.obtener_todos_los_elementos():
            print(f"Elemento: {elemento.get_nombre()}, Posición: {elemento.get_posicion()}")

    def verificar_nivel_completado(self):
        """Verifica si todos los elementos 2 y 6 han sido recolectados."""
        for fila in self.laberinto:
            for celda in fila:
                if celda == 2 or celda == 6:  # Aún quedan elementos por recolectar
                    return False
        return True  # No quedan más elementos

    def avanzar_nivel(self):
        """Avanza al siguiente nivel si es posible."""
        if self.nivel < self.max_nivel:
            self.nivel += 1

            for fantasma in self.fantasmas:
                fantasma.velocidad += 1
            self.reiniciar_laberinto()  # Reiniciar el laberinto para el siguiente nivel

    def actualizar_matrizfruta(self, posicion):
        """Actualiza la matriz para indicar que la posición dada está vacía (1)."""
        # Convertir la posición a las coordenadas de la matriz
        x = posicion.get_x()
        y = posicion.get_y()
        # Cambiar el valor de la matriz a 1
        self.laberinto[y][x] = 1

    def actualizar_matriz(self, posicion):
        """Actualiza la matriz para indicar que la posición dada está vacía (1)."""
        # Convertir la posición a las coordenadas de la matriz
        x = posicion.get_x() // self.square_size
        y = posicion.get_y() // self.square_size
        # Cambiar el valor de la matriz a 1
        self.laberinto[y][x] = 1


    def agregar_elementos(self):
        """Agrega los Pacdots, Pildoras de Poder al sistema basado en el laberinto. Los fantasmas se crean directamente."""
        # Limpiar lista de fantasmas y otros elementos visuales
        self.fantasmas = []  # Lista para almacenar los fantasmas
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
                if cell_value == 1:  # Atajos
                    if col == 0:  # Es el atajo de la izquierda
                        atajo_izquierdo = AtajoLaberinto(Posicion(0, 17), "Atajo Izquierdo")
                        self.elementos.agregar_elemento(atajo_izquierdo)
                    elif col == 27:  # Es el atajo de la derecha
                        atajo_derecho = AtajoLaberinto(Posicion(27, 17), "Atajo Derecho")
                        self.elementos.agregar_elemento(atajo_derecho)
                if cell_value == 2:  # Pacdot (camino)
                    pacdot = Pacdot(Posicion(x, y), 'Pacdot')
                    self.elementos.agregar_elemento(pacdot)
                elif cell_value == 6:  # Pildora de Poder (especial)
                    pildora_poder = PildoraPoder(Posicion(x, y), 'PildoraPoder', 15)
                    self.elementos.agregar_elemento(pildora_poder)
                elif cell_value == 4:  # Fantasmas
                    # Agregar cada fantasma solo si no ha sido agregado ya
                    if not blinky_added:
                        self.fantasmas.append(Blinky(Posicion(col, row), self.square_size,4))
                        blinky_added = True
                    elif not clyde_added:
                        self.fantasmas.append(Clyde(Posicion(col, row), self.square_size, 4,4))
                        clyde_added = True
                    elif not inky_added:

                        self.fantasmas.append(Inky(Posicion(col, row), self.square_size, 4, self.blinky))

                        inky_added = True
                    elif not pinky_added:
                        self.fantasmas.append(Pinky(Posicion(col, row), self.square_size, 4))
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
        #fruta = Fruta(Posicion(0, 1),"", 15, "", self.square_size)
        pygame.init()
        clock = pygame.time.Clock()
        # Crear el menú de inicio con la imagen de fondo
        background_path = os.path.join(SpriteSheets, "GameBoardSheet.png")
        menu = Menu(self.screen, background_path)
        running = True
        menu_active = True  # El menú está activo al inicio

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if menu_active:
                    option_selected = menu.handle_event(event)
                    if option_selected == "Iniciar Juego":
                        menu_active = False  # Dejar de mostrar el menú y empezar el juego
                        juego_empezado = True
                    elif option_selected == "Cargar Juego":
                        print("Cargar juego seleccionado")
                        # Lógica de carga...

            if menu_active:
                self.screen.fill((0, 0, 0))  # Limpiar pantalla
                menu.draw()  # Dibujar el menú
                pygame.display.update()
            else:
                self.agregar_elementos()  # Agregar los elementos al iniciar
                direccion_actual = None  # Variable para almacenar la dirección actual
                fruta_creada = False  # Controlar si ya se creó una fruta en este nivel
                juego_empezado = False  # Variable para indicar si el juego ha comenzado
                tiempo_inicio_juego = 0  # Variable para almacenar el tiempo de inicio

                # Configurar el temporizador para crear la fruta después de 5 segundos
                pygame.time.set_timer(pygame.USEREVENT + 1, 15000)

                # Configurar la fuente para mostrar el puntaje y las vidas
                font = pygame.font.SysFont(None, 30)

                while running and not menu_active:  # Añadir not menu_active para poder salir al menú
                    delta_time = clock.tick(40) / 1000.0  # Tiempo en segundos

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                        if event.type == pygame.KEYDOWN:
                            if not juego_empezado:  # Si el juego no ha empezado, cualquier tecla lo inicia
                                juego_empezado = True
                                tiempo_inicio_juego = pygame.time.get_ticks()  # Registrar el tiempo de inicio
                            else:
                                if event.key == pygame.K_RIGHT:
                                    direccion_actual = "derecha"
                                elif event.key == pygame.K_LEFT:
                                    direccion_actual = "izquierda"
                                elif event.key == pygame.K_UP:
                                    direccion_actual = "arriba"
                                elif event.key == pygame.K_DOWN:
                                    direccion_actual = "abajo"

                        # Evento personalizado para crear la fruta
                        if event.type == pygame.USEREVENT + 1 and not fruta_creada:
                            if self.nivel in [1, 2, 3]:  # Controla la aparición de la fruta en niveles 1, 2 y 3
                                posicion_fruta = self.generar_posicion_fruta()
                                if posicion_fruta:
                                    fruta = self.crear_fruta_segun_nivel(self.nivel, posicion_fruta)
                                    self.elementos.agregar_elemento(fruta)
                                    fruta_creada = True

                    if juego_empezado:
                        tiempo_actual = pygame.time.get_ticks()
                        if tiempo_actual - tiempo_inicio_juego > 2000:
                            if direccion_actual:
                                self.pacman.mover(direccion_actual, delta_time)

                            for fantasma in self.fantasmas:
                                fantasma.mover(self.pacman.get_posicion(), self.grafo, delta_time)

                            self.elementos.verificar_colisiones(self.pacman, self)
                            for fantasma in self.fantasmas:
                                self.pacman.colision_fantasma(fantasma)
                                vidas_restantes = self.pacman.get_vidas()
                                if vidas_restantes == 0:
                                        menu_active = True
                                        juego_empezado = False
                                        direccion_actual = None
                                        self.pacman.set_vidas(3)
                                        self.pacman.set_punto(0)  # Mantener puntaje acumulado
                                        self.reiniciar_laberinto()
                                        break

                        if self.verificar_nivel_completado():
                                self.avanzar_nivel()
                                self.pacman.set_posicion(Posicion(14, 26))
                                fruta_creada = False
                                if self.nivel > self.max_nivel:
                                    print("Juego completado. Volviendo al menú principal.")
                                    menu_active = True
                                    self.pacman.set_vidas(3)
                                    self.pacman.set_punto(0)

                                    juego_empezado = False
                                    direccion_actual = None
                                    break

                    self.screen.fill((0, 0, 0))  # Limpiar pantalla

                    puntaje_text = font.render(f"Puntaje: {self.pacman.get_punto()}", True, (255, 255, 255))
                    self.screen.blit(puntaje_text, (10, 10))

                    vidas_text = font.render(f"Vidas: {self.pacman.get_vidas()}", True, (255, 255, 255))
                    self.screen.blit(vidas_text, (10, self.height - 30))

                    self.draw()  # Dibujar el laberinto y los elementos
                    pygame.display.update()  # Actualizar la pantalla

    """def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        # Crear el menú de inicio con la imagen de fondo
        background_path = os.path.join(SpriteSheets , "GameBoardSheet.png")
        menu = Menu(self.screen, background_path)
        running = True
        menu_active = True  # El menú está activo al inicio

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if menu_active:
                    option_selected = menu.handle_event(event)
                    if option_selected == "Iniciar Juego":
                        menu_active = False  # Dejar de mostrar el menú y empezar el juego
                        juego_empezado = True
                    elif option_selected == "Cargar Juego":
                        # Implementar la lógica para cargar el juego aquí
                        print("Cargar juego seleccionado")
                        # Lógica de carga...

            if menu_active:
                self.screen.fill((0, 0, 0))  # Limpiar pantalla
                menu.draw()  # Dibujar el menú
                pygame.display.update()
            else:
                self.agregar_elementos()  # Agregar los elementos al iniciar
                running = True
                direccion_actual = None  # Variable para almacenar la dirección actual
                fruta_creada = False  # Controlar si ya se creó una fruta en este nivel
                juego_empezado = False  # Variable para indicar si el juego ha comenzado
                tiempo_inicio_juego = 0  # Variable para almacenar el tiempo de inicio

                # Configurar el temporizador para crear la fruta después de 5 segundos
                pygame.time.set_timer(pygame.USEREVENT + 1, 5000)

                # Configurar la fuente para mostrar el puntaje y las vidas
                font = pygame.font.SysFont(None, 30)

                while running:
                        delta_time = clock.tick(40) / 1000.0  # Tiempo en segundos

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                running = False
                            if event.type == pygame.KEYDOWN:
                                if not juego_empezado:  # Si el juego no ha empezado, cualquier tecla lo inicia
                                    juego_empezado = True
                                    tiempo_inicio_juego = pygame.time.get_ticks()  # Registrar el tiempo de inicio
                                else:
                                    if event.key == pygame.K_RIGHT:
                                        direccion_actual = "derecha"
                                    elif event.key == pygame.K_LEFT:
                                        direccion_actual = "izquierda"
                                    elif event.key == pygame.K_UP:
                                        direccion_actual = "arriba"
                                    elif event.key == pygame.K_DOWN:
                                        direccion_actual = "abajo"

                            # Evento personalizado para crear la fruta
                            if event.type == pygame.USEREVENT + 1 and not fruta_creada:
                                if self.nivel in [1, 2, 3]:  # Controla la aparición de la fruta en niveles 1, 2 y 3
                                    posicion_fruta = self.generar_posicion_fruta()
                                    if posicion_fruta:
                                        # Crear una fruta basada en el nivel actual y actualizar la matriz
                                        fruta = self.crear_fruta_segun_nivel(self.nivel, posicion_fruta)
                                        self.elementos.agregar_elemento(fruta)  # Agregar la fruta al SistemaHashing
                                        fruta_creada = True  # Marcar que ya se creó la fruta en este nivel


                        if juego_empezado:
                            tiempo_actual = pygame.time.get_ticks()
                            if tiempo_actual - tiempo_inicio_juego > 2000:  # Esperar 2 segundos antes de que el juego comience a moverse
                                if direccion_actual:
                                    self.pacman.mover(direccion_actual, delta_time)

                                for fantasma in self.fantasmas:
                                    fantasma.mover(self.pacman.get_posicion(), self.grafo, delta_time)


                                self.elementos.verificar_colisiones(self.pacman, self)
                                # Verificar colisión entre Pac-Man y cada fantasma
                                for fantasma in self.fantasmas:
                                    self.pacman.colision_fantasma(fantasma)
                                    # Verificar si Pac-Man ha perdido todas sus vidas
                                    if self.pacman.get_vidas() <= 0:
                                        print("Pac-Man ha perdido todas sus vidas.")
                                        menu_active = True  # Regresar al menú principal
                                        juego_empezado = False
                                        direccion_actual = None
                                        break  # Salir del ciclo para mostrar el menú

                                if self.verificar_nivel_completado():
                                    self.avanzar_nivel()
                                    self.pacman.set_posicion(Posicion(14, 26))  # Restaurar la posición inicial de Pac-Man
                                    fruta_creada = False  # Resetear la variable para que la fruta pueda crearse en el siguiente nivel
                                    # Verificar si se ha completado el juego
                                    if self.nivel > self.max_nivel:
                                        print("Juego completado. Volviendo al menú principal.")
                                        menu_active = True
                                        juego_empezado = False
                                        direccion_actual = None
                                        break

                        self.screen.fill((0, 0, 0))  # Limpiar pantalla

                        # Dibujar el puntaje en la parte superior de la pantalla
                        puntaje_text = font.render(f"Puntaje: {self.pacman.get_punto()}", True, (255, 255, 255))
                        self.screen.blit(puntaje_text, (10, 10))

                        # Dibujar las vidas en la parte inferior de la pantalla
                        vidas_text = font.render(f"Vidas: {self.pacman.get_vidas()}", True, (255, 255, 255))
                        self.screen.blit(vidas_text, (10, self.height - 30))

                        self.draw()  # Dibujar el laberinto y los elementos
                        pygame.display.update()  # Actualizar la pantalla
                        # 
                        """