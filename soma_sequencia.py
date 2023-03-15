def entrada():
    contents = []
    valores = []
    while True:
        try:
            line = input()
            contents.append(line)
        except EOFError:
            break
    for val in contents:
        valores.append(int(val))
        
    somar(valores)

def somar(valores):

    qtd = valores[0]

    print(sum(valores[1:qtd+1]))

entrada()