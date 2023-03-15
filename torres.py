
t = 1
k = 0
dicionario = {}
while True:
    try:
        n = int(input())
        num = input().split()
        numbers = [int(i) for i in num]

        for numero in numbers:
            if numero in dicionario:
                dicionario[numero] += 1
            else:
                dicionario[numero] = 1
                
            for chave, valor in dicionario.items():
                if valor > 1:
                    t += 1
            
    except:
        break
#print(n, num, numbers, dicionario)
print(max(dicionario.values()), len(dicionario))
            