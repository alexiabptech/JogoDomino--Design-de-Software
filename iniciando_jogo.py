def inicia_jogo (n_jogadores, lista_domino):

    div_jogo = {'jogadores': {}, 'monte': [], 'mesa': [] }

    
    if 2 <= n_jogadores <= 4:

        for i in range(0,n_jogadores):
            sete_pecas = []
            for n in range(0,7):
                sete_pecas.append(lista_domino[n])

            
            div_jogo['jogadores'][i] = sete_pecas
                
            
            del(lista_domino[0:7])
           

        div_jogo['monte'] = lista_domino     

    return div_jogo