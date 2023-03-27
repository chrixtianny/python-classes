# Criando a matriz da cidade
cidade = [[0 for i in range(4)] for j in range(4)]

# Definindo a posi��o inicial de Pedro
x = 0 # linha
y = 0 # coluna

# Lendo a sequ�ncia de movimentos
movimentos = input("").split(" ")
maximo = 20
movimentos = movimentos[:maximo]

# Atualizando a matriz da cidade com os passos de Pedro
for m in movimentos:
    if m == 'c': # cima
        x -= 1 # diminui a linha
    elif m == 'b': # baixo
        x += 1 # aumenta a linha
    elif m == 'e': # esquerda
        y -= 1 # diminui a coluna
    elif m == 'd': # direita
        y += 1 # aumenta a coluna
    
    # Verificando se Pedro est� dentro dos limites da cidade
    if x < 0 or x > 3 or y < 0 or y > 3:
        break
    
    # Adicionando um passo na posi��o atual de Pedro
    cidade[x][y] += 1

# Encontrando o local com mais passos de Pedro
max_passos = 0 # n�mero m�ximo de passos
max_x = 0 # linha do local com mais passos
max_y = 0 # coluna do local com mais passos

for i in range(4):
    for j in range(4):
        if cidade[i][j] > max_passos:
            max_passos = cidade[i][j]
            max_x = j
            max_y = i

# Imprimindo o local que Pedro n�o deve ir
print(f"Coordenada X:{max_x}, Y:{max_y}")
