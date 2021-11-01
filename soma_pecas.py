def soma_pecas (l_pecas_jogador):

    soma = 0
    for peca in l_pecas_jogador:
        for num in peca:
            soma += num
    return soma       