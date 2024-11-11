
from pacman.main.py.logic.AtajoLaberinto import AtajoLaberinto
from pacman.main.py.logic.Fruta import Fruta

class SistemaHashing:
    def __init__(self):
        self.elementos = {}

    def agregar_elemento(self, elemento):
        """Agrega un elemento en el diccionario self.elementos"""
        if elemento.get_key() in self.elementos:
          return
        self.elementos[elemento.get_key()] = elemento

    def eliminar_elemento(self, key):
        if key in self.elementos:
            del self.elementos[key]

        # Recorremos todos los elementos y verificamos si están cerca de Pac-Man

    def verificar_colisiones(self, pacman, laberinto):
        """
        Verifica si Pac-Man colisiona con algún elemento en su posición actual.
        Si hay colisión, realiza la acción correspondiente y elimina el elemento.
        """
        # Convertimos la posición de Pac-Man a píxeles
        pacman_x = pacman.get_posicion().get_x() * pacman.square_size
        pacman_y = pacman.get_posicion().get_y() * pacman.square_size
        for key, elemento in list(self.elementos.items()):
            # Verificar si el elemento es un AtajoLaberinto
            if isinstance(elemento, AtajoLaberinto):
                if elemento.colisionar(pacman):
                    continue  # No eliminar atajos
            if isinstance(elemento, (AtajoLaberinto, Fruta)):
                # En este caso, no usamos píxeles sino las posiciones de la cuadrícula
                if elemento.colisionar(pacman):  # Comparar directamente posiciones de la cuadrícula
                    if isinstance(elemento, Fruta):
                        print(f"Fruta eliminada en {elemento.get_posicion()}")
                        laberinto.actualizar_matrizfruta(elemento.get_posicion())
                        self.eliminar_elemento(key)

                    # No eliminamos los atajos
                    continue
            else:
                # Para los demás elementos, comparamos en píxeles
                objeto_x = elemento.get_posicion().get_x()
                objeto_y = elemento.get_posicion().get_y()
                # Ajustar la tolerancia de colisión
                tolerancia_colision = 11  # Ajustar según el tamaño del sprite
                # Verificar si las coordenadas de Pac-Man y el objeto están dentro de la tolerancia
                if abs(pacman_x - objeto_x) < tolerancia_colision and abs(pacman_y - objeto_y) < tolerancia_colision:
                    # Si hay colisión, realiza la acción correspondiente
                    if elemento.colisionar(pacman):
                        # Si el elemento no es un atajo, eliminarlo después de la colisión
                        laberinto.actualizar_matriz(elemento.get_posicion())
                        self.eliminar_elemento(key)



    def obtener_elemento(self, key):
        """Obtiene un elemento específico por su clave (posición)."""
        return self.elementos.get(key, None)


    def vaciar(self):
        """Elimina todos los elementos en el sistema de hashing."""
        self.elementos.clear()

    def obtener_todos_los_elementos(self):
        return list(self.elementos.values())


    def imprimir_elementos(self):
        for key, elemento in self.elementos.items():
            print(
                f"Clave: {key}, Nombre: {elemento.get_nombre()}, Posición: {elemento.get_posicion()}, Duración: {elemento.get_duracion()}")

"""La clase SistemaHashing es responsable de almacenar y gestionar los elementos del juego 
utilizando un diccionario para realizar búsquedas rápidas basadas en una clave 
(probablemente la posición de los elementos o algún identificador único). 
Permite agregar y eliminar elementos, verificar colisiones entre Pac-Man y estos elementos, 
vaciar el sistema de almacenamiento y obtener información de los elementos almacenados. 
La lógica de colisiones maneja diferentes tipos de elementos (como frutas y atajos de laberinto) 
y realiza acciones correspondientes cuando Pac-Man interactúa con ellos."""