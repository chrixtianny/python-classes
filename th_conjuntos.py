entrada = []

while True:
    try:
        elemento = input()
        entrada.append(elemento)
    except:
        break

v1_size = entrada.pop(0)
v2_size = entrada.pop(0)

#print(v1_size)

v1_size = int(v1_size)
v2_size = int(v2_size)

v1 = entrada[0:v1_size]
v2 = entrada[v1_size:]

uniao = v2.copy()

#print(uniao)

for elemento in v1:
    if elemento not in uniao:
        uniao.append(elemento)

intersecao = []
for elemento in v1:
    if elemento in v2:
        intersecao.append(elemento)

diferenca = []
for elemento in v1:
    if elemento not in v2:
        diferenca.append(elemento)

print(uniao)
print(intersecao)
print(diferenca)