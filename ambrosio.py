n = int(input())

posicao_jogador = 1

jogadas = 0
dado = 6

while posicao_jogador != n:
    for d in range (1, dado+1):
        posicao_jogador += d
        jogadas +=1
        if posicao_jogador > n:
            posicao_jogador = posicao_jogador % n
            continue
        elif posicao_jogador == n:
            print(jogadas)
            break
