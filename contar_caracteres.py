def contar(s):
    
    if len(s) >= 50:
        print("Tente novamente")
        contar(s)
    else:
        return s

if __name__ == "__main__":
    
    maximo = 50
    s = (input(""))
    print(len(s[:maximo]))