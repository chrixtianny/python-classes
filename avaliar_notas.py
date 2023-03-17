notas = []
respostas = []
resultado_aluno = []
def entrada():
    while True:
        try:
            nome, resposta = input().split()
            respostas.append(resposta)
            if nome == ["*"] or resposta == ["*"]:
                break
        except:
                break 
    gabarito = input()
    gabarito = [ch for ch in gabarito]
    for r in respostas:
        resposta = [ch for ch in r]
        resultado = []
        for i in range (len(gabarito)):
            if gabarito[i] == resposta[i]:
                resultado.append(int(1))
            else:
                resultado.append(0)
        resultado_aluno.append(sum(resultado))
    t = float(len(resultado_aluno))
    media = (float(sum(resultado_aluno))/t)
    maiorNota = (max(resultado_aluno))
    menorNota= (min(resultado_aluno))
    print(maiorNota)
    print(menorNota)
    print("{:.2f}".format(media))
entrada()