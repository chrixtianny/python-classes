ano_atual = 2152
bissexto = False

def contarDigitos():
    while True:
        ano = input("")
        if ano == '-1':
            break
        elif len(ano) != 4:
            print("Ano invalido")
        else:
            ano = int(ano)
            eh_bissexto = ehBissexto(ano)
            Mensagem(ano, eh_bissexto)

def ehBissexto(ano):
    if (ano % 4 == 0) and ((ano % 100 != 0) or (ano % 400 == 0)):
        return True
    else:
        return False
    
def Mensagem(ano, eh_bissexto):
    if eh_bissexto:
        if ano == ano_atual:
            print("O ano", ano,"eh bissexto")
        elif ano < ano_atual:
            print("O ano", ano,"foi bissexto")
        elif ano > ano_atual:
            print("O ano", ano, "serah bissexto")
    else:
        print("O ano", ano, "NAO eh bissexto")

contarDigitos()
