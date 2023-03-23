caracteres = {}
def contagem():
    entrada = input("")
    entrada = [ch for ch in entrada]
    entrada = sorted(entrada, reverse=True)
    #print(entrada)

    count = 1
    for i in (entrada):
        
        if i not in caracteres:
            count = 1
            caracteres[i] = count
            #caracteres.get(i, count)
        elif i in caracteres:
            count +=1
        caracteres[i] = count
        #print(caracteres)
    for k, v in caracteres.items():
        print(k, v)
''' também funcionou com:   
    for k in caracteres.keys():
        print("{} {}".format(k, caracteres[k]))'''

contagem()