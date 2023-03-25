custo_internet = 0
custo_revista = 0
custo_outdoor = 0
custo_radio = 0
custo_tv = 0
nome_anterior = ""

while True:
    entrada = input().split()

    if len(entrada) > 1:
        if nome_anterior != "":
            custo_total = custo_internet + custo_revista + custo_outdoor + custo_radio + custo_tv
            print(nome_anterior + ": {:.2f}".format(custo_total))

        nome_anterior = entrada[0]
        n_midias = int(entrada[1])

        custo_internet = 0
        custo_revista = 0
        custo_outdoor = 0
        custo_radio = 0
        custo_tv = 0

    else:
        midia = entrada[0].lower()

        if midia == "internet":
            custo_internet = 3000
        elif midia == "revista":
            custo_revista = 750
        elif midia == "outdoor":
            custo_outdoor = 1500
        elif midia == "radio":
            tipo_radio = input().lower()
            if tipo_radio == "fm":
                custo_radio += 500
            elif tipo_radio == "am":
                custo_radio += 300
        elif midia == "tv":
            horario = int(input())
            if horario <= 20:
                custo_tv += 1200
            else:
                custo_tv += 2000

    if nome_anterior != "" and entrada[0].lower() == "fim":
        custo_total = custo_internet + custo_revista + custo_outdoor + custo_radio + custo_tv
        print(nome_anterior + ": {:.2f}".format(custo_total))
        break