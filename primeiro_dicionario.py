def remover_especiais(palavra):
    replacements = [('(',' '), ('#', ' '), ('*', ' '), (':', ' '), ('"', ' '), ('.', ' ')]
    for char, replacement in replacements:
        if char in palavra:
            palavra = palavra.replace(char, replacement)
    return palavra.split()

def entrada():
    p_dicionario = {}
    while True:
        entrada = input().split()
        palavras = entrada[0:]
        for palavra in palavras:
            if palavra == '-1':
                break
            elif palavra.isalnum(): # check if the word only contains alphanumeric characters
                palavra = palavra.lower()
                if palavra in p_dicionario:   
                    p_dicionario[palavra] += 1
                else: 
                    p_dicionario[palavra] = 1
            else:
                # split the word into separate words using remover_especiais
                palavras_especiais = remover_especiais(palavra.lower())
                for palavra_especial in palavras_especiais:
                    if palavra_especial in p_dicionario:
                        p_dicionario[palavra_especial] += 1
                    else:
                        p_dicionario[palavra_especial] = 1
        if palavra == '-1':
            break
    p_dicionario = dict(sorted(p_dicionario.items()))
    for k, v in p_dicionario.items():
        print(k, v)

entrada()