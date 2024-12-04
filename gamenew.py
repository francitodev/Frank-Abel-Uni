import random

def mostrar_tablero(tablero):
    print("-------------")
    for fila in tablero:
        print("|", end=" ")
def comprobar_victoria(tablero, jugador):
    for fila in tablero:
        if all(celda == jugador for celda in fila):
            return True
    for col in range(3):
        if all(tablero[fila][col] == jugador for fila in range(3)):
            return True
    if all(tablero[i][i] == jugador for i in range(3)):
        return True
    if all(tablero[i][2 - i] == jugador for i in range(3)):
        return True
    return False

def comprobar_empate(tablero):
    for fila in tablero:
        for celda in fila:
            if celda == " ":
                return False
    return True

def obtener_movimiento_jugador(tablero):
    while True:
        try:
            fila = int(input("Ingresa el número de fila (1-3): ")) - 1
            col = int(input("Ingresa el número de columna (1-3): ")) - 1
            if 0 <= fila < 3 and 0 <= col < 3 and tablero[fila][col] == " ":
                return fila, col
            else:
                print("Movimiento inválido. Intenta de nuevo.")
        except ValueError:
            print("Entrada inválida. Ingresa números del 1 al 3.")

def obtener_movimiento_computadora(tablero):
    for jugador in ["O", "X"]:
        for fila in range(3):
            for col in range(3):
                if tablero[fila][col] == " ":
                    tablero[fila][col] = jugador
                    if comprobar_victoria(tablero, jugador):
                        return fila, col
                    tablero[fila][col] = " "

    movimientos_disponibles = [(fila, col) for fila in range(3) for col in range(3) if tablero[fila][col] == " "]
    if movimientos_disponibles:
        return random.choice(movimientos_disponibles)
    return None


def jugar_juego():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    turno = "X" 

    while True:
        mostrar_tablero(tablero)
        if turno == "X":
            fila, col = obtener_movimiento_jugador(tablero)
        else:
            print("Turno de la computadora...")
            fila, col = obtener_movimiento_computadora(tablero)
            if fila is None: #No hay movimientos disponibles
                print("Empate!")
                return

        tablero[fila][col] = turno
        if comprobar_victoria(tablero, turno):
            mostrar_tablero(tablero)
            print(f"¡{turno} gana!")
            return
        if comprobar_empate(tablero):
            mostrar_tablero(tablero)
            print("Empate!")
            return
        turno = "O" if turno == "X" else "X"

if __name__ == "__main__":
    jugar_juego()