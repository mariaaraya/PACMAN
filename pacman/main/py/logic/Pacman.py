import os
import pygame
# Obtener la ruta absoluta del directorio raíz del proyecto (subiendo más niveles)
current_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Construir la ruta correcta hacia las imágenes
BoardPath = os.path.join(current_dir, "resorces", "ElementImages")
# Esto se podría agregar al ciclo principal del juego


MODO_PERSECUCION = "persecucion" # Para cuandso se pued apcomer la fantsma
MODO_NORMAL = "normal"
class Pacman:
    def __init__(self, velocidad, posicion, punto, square_size, laberinto):
        self.velocidad = velocidad
        self.vidas = 3
        self.posicion = posicion  # Debe ser un objeto de la clase Posicion
        self.punto = punto
        self.modo = MODO_NORMAL
        self.changeFeetCount = 0  # Contador para alternar imágenes
        self.square_size = square_size  # Tamaño del sprite
        self.laberinto = laberinto  # Referencia al laberinto
        self.colision_desactivada = False  # Nueva bandera para desactivar la colisión temporalmente
        self.ultimo_teletransporte = 0  # Guardar el tiempo del último teletransporte

    # Getters
    def get_posicion(self):
        return self.posicion

    def get_velocidad(self):
        return self.velocidad

    def get_vidas(self):
        return self.vidas

    def get_punto(self):
        return self.punto

    def get_modo(self):
        return self.modo

    # Setters
    def set_posicion(self, posicion):
        self.posicion = posicion

    def set_velocidad(self, velocidad):
        self.velocidad = velocidad

    def set_vidas(self, vidas):
        self.vidas = vidas

    def set_punto(self, punto):
        self.punto = punto

    def set_modo(self, modo):
        self.modo = modo

    def colision(self , punto):
        self.punto+= punto

    def colision_atajo(self, nueva_posicion):
        """Teletransporta a Pac-Man a la nueva posición del atajo."""
        self.posicion.set_x(nueva_posicion.get_x())
        self.posicion.set_y(nueva_posicion.get_y())
        self.posicion.set_direccion("derecha")  # Ajusta la dirección si es necesario
        self.colision_desactivada = True  # Desactivar colisiones temporalmente
        self.tiempo_colision_desactivada = pygame.time.get_ticks()  # Guardar el tiempo actual
        #Aqui nos apoyamos con chatgpt para mejorar el metodo que teniamos inicialmente, por eso el tiempo de colision desativada

    def colision_pildora(self, duracion):
        """Activa el modo asustado en el laberinto para los fantasmas durante la duración de la pildora."""
        self.laberinto.activar_modo_asustado(duracion)

    def colision_fantasma(self, fantasma):
        # Obtener la posición de fantasma en la cuadrícula
        fantasma_x = fantasma.get_posicion().get_x()  # Coordenada X en la cuadrícula
        fantasma_y = fantasma.get_posicion().get_y()  # Coordenada Y en la cuadrícula
        # Obtener la posición del objeto (Pacdot o Fruta) en la cuadrícula
        objeto_x = self.posicion.get_x()  # Coordenada X del objeto en la cuadrícula
        objeto_y = self.posicion.get_y()  # Coordenada Y del objeto en la cuadrícula
        # Imprimir las posiciones de Pac-Man y el objeto
        # Definir una tolerancia en la distancia (por ejemplo, 1 celda de diferencia)
        tolerancia = 1  # Puedes ajustar la tolerancia según el tamaño de las celdas

        # Verificar si Pac-Man está en una posición cercana (dentro de la tolerancia)
        if abs(fantasma_x - objeto_x) <= tolerancia and abs(fantasma_y - objeto_y) <= tolerancia:
            if self.modo == MODO_NORMAL or fantasma.modo == MODO_PERSECUCION:
                self.vidas -= 1
                self.laberinto.posion_original()
            else:
                self.punto+=200
                fantasma.colision_Pacman()


    def mover(self, direccion, delta_time):
        """Mueve a Pac-Man en la dirección dada, teniendo en cuenta su velocidad y el tiempo transcurrido."""

        # Obtener la posición actual de Pac-Man
        x_actual = self.posicion.get_x()
        y_actual = self.posicion.get_y()

        # Crear variables para la nueva posición
        nuevo_x = x_actual
        nuevo_y = y_actual

        # Ajustar la cantidad de movimiento basado en la velocidad y el tiempo delta
        movimiento = (self.velocidad * delta_time)

        # Predecir la nueva posición basada en la dirección, sin cambiarla aún
        if direccion == "derecha":
            nuevo_x += movimiento
        elif direccion == "izquierda":
            nuevo_x -= movimiento
        elif direccion == "arriba":
            nuevo_y -= movimiento
        elif direccion == "abajo":
            nuevo_y += movimiento

        # Redondear la nueva posición a números enteros para asegurar que estén en la cuadrícula
        nuevo_x = round(nuevo_x)
        nuevo_y = round(nuevo_y)
        # Obtener la matriz del laberinto
        matriz_laberinto = self.laberinto.obtener_matriz()

        # Verificar si la nueva posición está dentro de los límites y no hay una pared
        if 0 <= nuevo_y < len(matriz_laberinto) and 0 <= nuevo_x < len(matriz_laberinto[0]):
            if matriz_laberinto[int(nuevo_y)][int(nuevo_x)] not in [3, 4]:  # Verificar que no haya una pared
                # Si la nueva posición es válida, actualizarla
                self.posicion.set_x(nuevo_x)
                self.posicion.set_y(nuevo_y)
                # Actualizar la dirección solo si el movimiento fue exitoso
                self.posicion.set_direccion(direccion)
            else:
                # Si hay una pared, Pac-Man sigue en la misma dirección, pero no cambia su posición
                pass
        else:
            # Si la nueva posición está fuera de los límites, no hacer nada
            pass
        #este metodo de mover, chatgpt nos ayudo en la guia, gracias a este pudimos basarnos para los fantasmas, con sus respectivos cambios de bfs

    def draw(self, screen):
        # Obtener la dirección actual
        direccion = self.posicion.get_direccion()

        # Elegir la imagen de Pac-Man en función de la dirección
        if direccion == "izquierda":
            image_frame_1 = "tile048.png"
            image_frame_2 = "tile050.png"
        elif direccion == "derecha":
            image_frame_1 = "tile052.png"
            image_frame_2 = "tile054.png"
        elif direccion == "arriba":
            image_frame_1 = "tile051.png"
            image_frame_2 = "tile049.png"
        elif direccion == "abajo":
            image_frame_1 = "tile053.png"
            image_frame_2 = "tile055.png"

        # Alternar entre las dos imágenes para simular movimiento
        if self.changeFeetCount % 2 == 0:
            pacmanImage = pygame.image.load(os.path.join(BoardPath, image_frame_1))
        else:
            pacmanImage = pygame.image.load(os.path.join(BoardPath, image_frame_2))

        self.changeFeetCount += 1

        # Escalar la imagen para adaptarla al tamaño de la celda del laberinto
        pacmanImage = pygame.transform.scale(pacmanImage, (int(self.square_size * 1.15), int(self.square_size * 1.15)))

        # Dibujar la imagen en la posición actual de Pac-Man
        screen.blit(pacmanImage, (self.posicion.get_x() * self.square_size ,
                                  self.posicion.get_y() * self.square_size ))
    #con chatgpt logramos mejorar el dibujo de los personajes (sus imagenes respectivas), de aqui nos basamos para los siguientes personajes (los fantasmas)