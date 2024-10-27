
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

    def verificar_colisiones(self, pacman):
        """Verifica colisiones y elimina elementos que no sean 'atajos'."""
        colisiones = []
        for key, elemento in self.elementos.items():
            if elemento.colisionar(pacman):
                colisiones.append(key)
        for key in colisiones:
            if key != "atajos":  # Verifica que el elemento no se llame 'atajos'
                self.eliminar_elemento(key)

    def obtener_elemento(self, key):
        return self.elementos.get(key, None)

    def obtener_todos_los_elementos(self):
        return list(self.elementos.values())

    def imprimir_elementos(self):
        for key, elemento in self.elementos.items():
            print(
                f"Clave: {key}, Nombre: {elemento.get_nombre()}, Posición: {elemento.get_posicion()}, Duración: {elemento.get_duracion()}")