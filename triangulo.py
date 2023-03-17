def sequencia():

    numero = int(input(""))
    
    if 1 <= numero <= 30:
        for i in range (1, numero+1):
            
            print(i*(str(i)), end="\n")
    
    else:
    
        sequencia()
        
def sequencia():

    numero = int(input(""))
    
    if 1 <= numero <= 30:
        for i in range (1, numero+1):
            
            print(i*(str(i)), end="\n")
    
    else:
    
        sequencia()
        
sequencia()