#ÁreaDoCirculo
#BootcampSocialTechEmbraer
#XPeducação
condicao = True
while condicao == True:
    
  print("\nBem vindo. Vamos calcular a área do círculo! Gostaria de utilizar o valor de pi padrão? \n 1 - Sim \n 2 - Não, gostaria de fornecer o valor exato de pi desejado \n 3 - Sair")
  
  opcao = int(input(" "))
    
  if opcao == 1:
    raio = float(input("Raio: "))
    valordepi = 3.14
    areaCirculoPiPadrao = lambda  raio: raio **2 * valordepi
  
    print("A área do circulo é: ", areaCirculoPiPadrao(raio))
  
  elif opcao == 2:
    
    raio = float(input("Raio: "))
    valordepi = float(input("Pi: "))
    areaCirculoPiInformado = lambda  raio: raio **2 * valordepi
  
    print("A área do circulo é: ", areaCirculoPiInformado(raio))
    
  elif opcao == 3:
    condicao = False
    print("Você saiu.")
  
  else:
    print("Opção inválida!")