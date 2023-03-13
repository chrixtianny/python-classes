impares = []
pares = []
condicao = True   
def entrada():
    while condicao:
        try:
            numero = int(input())
            if numero % 2 != 0:
                impares.append(numero)
                for i in range(len(impares)):
                    for j in range(i+1, len(impares)):
                        if impares[i] > impares[j]:
                            if impares[i] > impares[j]:
                                impares[i], impares[j] = impares[j], impares[i]
        
            else:
                pares.append(numero)
                for i in range(len(pares)):
                    for j in range(i+1, len(pares)):
                        if pares[i] > pares[j]:
                            if pares[i] > pares[j]:
                                pares[i], pares[j] = pares[j], pares[i]
        except:
            break
    resultado(impares, pares)
        

def resultado(impares, pares):
    
    #print(impares,pares)

    if len(impares) > 0:
        print("O maior e menor impares são", impares[-1], "e", impares[0])
        if len(pares) > 0:
            print("O maior e menor impares são", pares[-1], "e", pares[0])


entrada()