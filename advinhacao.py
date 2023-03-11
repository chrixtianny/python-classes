import random
numeroSecreto = random.randint(1, 10)
acertou = False
chutes = []
numeroTentativas = 1

print("Jogo de Adivinhação com chutes até acertar")
print("Descubra o número secreto de 1 a 10")

while acertou == False:      
    print("Tentativa número", numeroTentativas)
    chute = int(input("Digite o seu chute: "))  
    if chute < 1 or chute > 10:
        print("Número inválido, tente novamente")
    
    else:
            if chute == numeroSecreto:
                print("ACERTOU!")
                acertou = True
                print("Parabéns!!")
                break
            
            else:   
                if chute > numeroSecreto:
                    print("Chute foi MAIOR que o número secreto!")

                    if chute in chutes:
                        print("E você já deu esse chute!")
                    else:
                        chutes.append(chute) 
                    
                elif chute < numeroSecreto:
                    print("Chute foi MENOR que o número secreto!")
                    
                    if chute in chutes:
                        print("E você já deu esse chute!")
                    else:
                        chutes.append(chute)
                    

    numeroTentativas +=1
