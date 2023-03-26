nomePresentes = {}

def entrada():
    x = int(input(""))

    for i in range (x):
        n = input("").split()
        nomePresentes[n[0]] = n[1:]
        print(nomePresentes)
        continue
    consulta(nomePresentes)

def consulta(nomePresentes):
    acertou = False
    while True:
        try:
            entrada = input().split()
            nome, presente = entrada[0], entrada[1]
            for i,j in nomePresentes.items():
                if i == nome and presente in j:
                    acertou == True
                    print ("Uhuuul!!! ela vai gostar")
            else:
                print("tente novamente")

        except:
            pass

        finally:
            if nome.upper() == "FIM":
                break

entrada()