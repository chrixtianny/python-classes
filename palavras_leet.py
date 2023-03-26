palavra = input()

def leet(palavra):
    
    if palavra == "":
        print("vazia")
        print("0")
        return
    elif any(char.isdigit() for char in palavra):
        print("numeros")
        print("0")
        return
    
    leet_dict = {'a': '@', 'A': '@', 'e': '3', 'E': '3', 'i': '1', 'I': '1', 'o': '0', 'O': '0', 't': '7', 'T': '7', 's': '5', 'S': '5'}
    
    substituicoes = 0
    
    palavra_invertida = palavra[::-1]
    nova_palavra = ""
    for char in palavra_invertida:
        if char in leet_dict:
            nova_palavra += leet_dict[char]
            substituicoes += 1
        else:
            nova_palavra += char
    
    #print(f"{palavra}")
    print(f"{nova_palavra}")
    print(f"{substituicoes}")
    return substituicoes

leet(palavra)
