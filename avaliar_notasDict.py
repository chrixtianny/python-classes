respostas = {}
notas_maximas = {}
def entrada():
    
    while True:
        try:
            nome, resposta = input().split()
            respostas[nome] = resposta
            if nome == "*" or resposta == "*":
                break
        except:
            break

    gabarito = input()

    for key in respostas:
        resultado = 0
        for i in range(len(gabarito)):
            #print(respostas[key][i], gabarito[i])
            if respostas[key][i] == gabarito[i]:
                
                resultado += 1
        nota = resultado

        if key in notas_maximas:
            if nota > notas_maximas[key]:
                notas_maximas[key] = nota
        else:
            notas_maximas[key] = nota

    t = float(len(notas_maximas))
    media = (float(sum(notas_maximas.values())) / t)
    maiorNota = (max(notas_maximas.values()))
    menorNota = (min(notas_maximas.values()))

    print("Maior:", maiorNota)
    print("Menor:", menorNota)
    print("Media:","{:.2f}".format(media))
    
entrada()