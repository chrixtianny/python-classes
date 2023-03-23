k = int(input())
t = 1 
def entrada():
    n = int(input())
    senhas = input()
    tentativas(t, k, n, senhas)

def tentativas(t, k, n, senhas):
    if not (0 <= n <= 8):
        return

    while t <= k:
        try:
            chute = input()
            excelente = 0
            bom = 0
            if chute == ('0'*n):
                if t == k:
                    break
                else: 
                    n = 0
                    entrada()
                
            elif chute == senhas:
                excelente = n
                print("({},{})".format(excelente, bom))
                if t == k:
                    quit()
                else:
                    t = t + 1
                    #chute.clear()
                    #senha.clear()
                    #digitos_senha.clear()
                    entrada()
                    return
            else:
                chute = list(chute)
                senha = list(senhas)
    
                digitos_senha = senha.copy()
                #print(digitos_senha)
                for i, (ch, sn) in enumerate(zip(chute, senha)):
                    if ch == sn:
                        excelente += 1
                        digitos_senha.remove(ch)
                        #print(digitos_senha)
        
                for ch in chute:
                    if ch in digitos_senha:
                        bom += 1
                        digitos_senha.remove(ch)      

                print("({},{})".format(excelente, bom))
                      
        except:
            break
        
        
if k != 0*k:
    entrada()
else:
    pass
        