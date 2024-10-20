# Las imágenes fueron conseguidas desde https://github.com/DevinLeamy/Pacman

from pacman.main.py.logic.Fruta import Fruta
from pacman.main.py.logic.Pacdot import Pacdot
from pacman.main.py.logic.Pacman import Pacman
from pacman.main.py.logic.SistemaHashing import SistemaHashing


def main():
    fruta = Fruta(posicion=(1, 1),  nombre="Manzana", duracion=10)
    pera = Fruta(posicion=(10, 1), nombre="Pera", duracion=10)
    pacdot = Pacdot(posicion=(2, 2) , nombre="Pacdot")
    pacman = Pacman(1,2 ,(1,1))

    # Crear el sistema de hashing y agregar elementos
    sistema_hashing = SistemaHashing()
    sistema_hashing.agregar_elemento(fruta)
    sistema_hashing.agregar_elemento(pera)
    sistema_hashing.agregar_elemento(pacdot)

    # Verificar colisiones
    colisiones = sistema_hashing.verificar_colisiones(pacman)
    print(f"Elementos colisionados: {colisiones}")

  # Imprimir todos los elementos en el sistema de hashing
    sistema_hashing.imprimir_elementos()


if __name__ == "__main__":
    main()