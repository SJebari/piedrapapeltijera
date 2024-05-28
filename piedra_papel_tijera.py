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
        nombreUsuario = str(input('Nombre del usuario: '))

        if len(nombreUsuario) < 3:
            raise Exception('El nombre del usuario no puede tener menos de 3 caracteres')

        opcionMovimientoOrdenador = opcionOrdenador()
        opcionMovimientoUsuario = input(
            "Selecciona un movimiento ('p' para piedra / 'a' para papel / 't' para tijeras): ").lower()
        print(f"Elección del ordenador: {opcionMovimientoOrdenador}")
        if 'p' in opcionMovimientoUsuario or 'a' in opcionMovimientoUsuario or 't' in opcionMovimientoUsuario:
            if 'p' in opcionMovimientoUsuario and 'p' in opcionMovimientoUsuario:
                opcionMovimientoUsuario = piedra
            elif 'a' in opcionMovimientoUsuario and 'a' in opcionMovimientoUsuario:
                opcionMovimientoUsuario = papel
            elif 't' in opcionMovimientoUsuario and 't' in opcionMovimientoUsuario:
                opcionMovimientoUsuario = tijera
            print(f"Elección del usuario {nombreUsuario}: {opcionMovimientoUsuario}")
            if ganadorMovimiento(opcionMovimientoUsuario, opcionMovimientoOrdenador) == 1:
                print(f"Gana el usuario {nombreUsuario}!!!")
            elif ganadorMovimiento(opcionMovimientoUsuario, opcionMovimientoOrdenador) == -1:
                print("Gana el ordenador !!!")
            elif ganadorMovimiento(opcionMovimientoUsuario, opcionMovimientoOrdenador) == 0:
                print("Empate !!!")
        else:
            print("Entrada incorrecta. Vuelve a intentar.")
    elif 'n' in opcionJugar.lower():
        break
    else:
        print('Entrada incorrecta. Vuelve a intentar.')