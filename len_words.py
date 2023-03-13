
nomes = []
names_dict = {} # estrutura que irá armazenar o número de letras de cada nome

def contagem():
    
    while True:
        name = input("")
        if not name:
            break
        nomes.append(name) 
        for nome in nomes: # calcula o tamanho de cada nome (em número de letras) e armazena o valor na estrutura
            names_dict[nome] = len(nome)
    
    print({nome: len(nome) for nome in nomes})

contagem()

