k = int(input()) # onde k é numero de jogos
tentativa = 1

def entrada():
    n = int(input()) # onde n é numero de digitos na senha
    while n<1 or n>7:
        n = int(input())
    senhas = input()
    while len(senhas) != n:
        senhas = input()
    tentativas(k, n, senhas)

def tentativas(k, n, senhas):

    while tentativa < k+1:
        try:
            excelente = 0
            bom = 0
            chute = input()

            if chute == ('0'*n):
                if tentativa == k:
                    break
                else: 
                    entrada()
                    return
                
            elif chute == senhas:
                excelente = n
                print("({},{})".format(excelente, bom))
                if tentativa == k:
                    return
                else:
                    entrada()
                    return
                    
            else:
    
                acertados = []
            for i in range(n):
                if chute[i] not in acertados:
                    if chute[i] == senhas[i]:
                        excelente += 1
                        acertados.append(chute[i])
                        
                    elif chute[i] in senhas and chute[i] not in acertados:
                        bom += 1
                           
                else:
                    continue

        except:
            break
            
        print(f'({excelente},{bom})')
    return

if k != 0:   
    entrada()