destinos = {}

def resultado(escolhido):
    print(escolhido.upper())

if __name__ == "__main__":
    while True:
        destino = input("")
        if destino.upper() == "FIM":
            if destinos == {}:
                print("SEM DESTINO")
                break
            else:
                escolhido = max(destinos, key=destinos.get)
                resultado(escolhido)
            break
        elif destino == '' and destinos == {}:
            print("SEM DESTINO")
            break
        else:
            km = int(input())
            preco = float(input())
            if preco*2 <= 300.00:
                destinos[destino] = km