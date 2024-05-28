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

nombreUsuario = str(input('Nombre del usuario: '))

if len(nombreUsuario) < 3:
    raise Exception('El nombre del usuario no puede tener menos de 3 caracteres')

numeroIntentos = int(input('Numero de intentos: '))
if numeroIntentos < 1:
    raise Exception('El numero de intentos no puede ser menor que 1')

while True:
    opcionJugar = input("Quieres jugar? (s/n): ")
    if 's' in opcionJugar.lower():
        usuarioGana = 0
        ordenadorGana = 0
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
                usuarioGana += 1
            elif ganadorMovimiento(opcionMovimientoUsuario, opcionMovimientoOrdenador) == -1:
                print("Gana el ordenador !!!")
                ordenadorGana += 1
            elif ganadorMovimiento(opcionMovimientoUsuario, opcionMovimientoOrdenador) == 0:
                print("Empate !!!")
            numeroIntentos -= 1
            if numeroIntentos == 0:
                if usuarioGana > ordenadorGana and ordenadorGana < usuarioGana:
                    print(f'\nEl usuario {nombreUsuario} gana el juego !!!\nCon {usuarioGana} partidas ganadas !!!')
                    break
                elif ordenadorGana > usuarioGana and usuarioGana < ordenadorGana:
                    print(f'\nEl ordenador gana el juego !!!\nCon {ordenadorGana} partidas ganadas !!!')
                    break
                elif usuarioGana == ordenadorGana:
                    print(f'\nHa habido un empate !!!\nCon {usuarioGana} partidas ganadas del {nombreUsuario}'
                          f' y {ordenadorGana} partidas ganadas del ordenador')
                    break
        else:
            print("Entrada incorrecta. Vuelve a intentar.")
    elif 'n' in opcionJugar.lower():
        break
    else:
        print('Entrada incorrecta. Vuelve a intentar.')
