def posicoes_possiveis(mesa, pecas):
    #cada peca tem uma das duas faces abertas quando colocadas na mesa
    #se tiver ao menos uma face igual
    #Quando a mesa ta vazia qqr peca pode ser colocada
    posiveis_pos = []
    if mesa == []:
        i = 0
        while i < len(pecas):
            posiveis_pos.append(i)
            i += 1
    else:
        i=0
        while i < len(pecas):
            if mesa[0][0] == pecas[i][0] or mesa[-1][1] == pecas[i][0] or mesa[-1][1] == pecas[i][1] or mesa[0][0] == pecas[i][1]:
                posiveis_pos.append(i)
            i += 1    
    return posiveis_pos