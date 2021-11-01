def verifica_ganhador(num_jog):
    #num_jogadores = {numero: lista_peças}
    #return posicao do jogador sem peças
    for jogador, pecas in num_jog.items():
        if pecas == []:
            return jogador
        
    return -1