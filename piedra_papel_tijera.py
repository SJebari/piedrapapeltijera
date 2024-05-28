import random

piedra = 'piedra'
papel = 'papel'
tijera = 'tijera'
opcionesMovimientos = [piedra, papel, tijera]
ganaUsuario = [[papel, piedra], [tijera, papel], [piedra, tijera]]
ganaOrdenador = [[piedra, papel], [papel, tijera], [tijera, piedra]]


def opcionOrdenador():
    movimientoOrdenador = random.choice(opcionesMovimientos)
    return movimientoOrdenador


def ganadorMovimiento(usuarioMovimiento, ordenadorMovimiento):
    if [usuarioMovimiento, ordenadorMovimiento] in ganaUsuario:
        return 1
    elif [usuarioMovimiento, ordenadorMovimiento] in ganaOrdenador:
        return -1
    return 0


print("JUEGO : Piedra, papel y tijera")
while True:
    opcionJugar = input("Quieres jugar? (s/n): ")
    if 's' in opcionJugar.lower():
        opcionMovimientoOrdenador = opcionOrdenador()
        opcionMovimientoUsuario = input(
            "Selecciona un movimiento ('p' para piedra / 'a' para papel / 't' para tijeras / 'TERMINAR' para "
            "terminar): ").lower()
        if opcionMovimientoUsuario == 'p' or opcionMovimientoUsuario == 'a' or opcionMovimientoUsuario == 't':
            if 'p' in opcionMovimientoUsuario and 'p' in opcionMovimientoUsuario:
                opcionMovimientoUsuario = piedra
            elif 'a' in opcionMovimientoUsuario and 'a' in opcionMovimientoUsuario:
                opcionMovimientoUsuario = papel
            elif 't' in opcionMovimientoUsuario and 't' in opcionMovimientoUsuario:
                opcionMovimientoUsuario = tijera
            print(f"Elección del usuario: {opcionMovimientoUsuario}")
            print(f"Elección del ordenador: {opcionMovimientoOrdenador}")
            if ganadorMovimiento(opcionMovimientoUsuario, opcionMovimientoOrdenador) == 1:
                print("Gana el usuario !!!")
            elif ganadorMovimiento(opcionMovimientoUsuario, opcionMovimientoOrdenador) == -1:
                print("Gana el ordenador !!!")
            elif ganadorMovimiento(opcionMovimientoUsuario, opcionMovimientoOrdenador) == 0:
                print("Empate !!!")
        elif opcionMovimientoUsuario == 'terminar':
            print('Tienes miedo?')
            break
        else:
            print("Entrada incorrecta. Vuelve a intentar.")
    elif 'n' in opcionJugar.lower():
        break
    else:
        print('Entrada incorrecta. Vuelve a intentar.')
