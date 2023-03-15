n, m = input().split()
n, m = int(n), int(m)

voltas = {}

def corridas():
    for i in range(1, n+1):
        try:
            tempo = input().split()
            voltas[i] = [int(t) for t in tempo]
        except:
            break

    tempos_totais = {}
    for i in voltas:
        tempos_totais[i] = sum(voltas[i])

    vencedor = min(tempos_totais, key=tempos_totais.get)
    return vencedor

vencedor = corridas()
print(vencedor)
