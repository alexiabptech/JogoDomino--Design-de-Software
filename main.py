import domino
import random

iniciando = input('Olá, bem vindo ao jogo Dominó. Você deseja jogar? (sim,não) ')

while iniciando == 'sim':
    criando_as_pecas = domino.cria_pecas() #crio as peças do jogo
    qtd_jogadores = int(input('Quantas pessoas vão jogar? ')) # Falo quantas pessoas vão jogar
    div_jogo = domino.inicia_jogo(qtd_jogadores,criando_as_pecas) #divido as peças para os jogadores, o monte e a mesa.
    jogadores = div_jogo['jogadores']
    monte = div_jogo['monte']
    mesa = div_jogo['mesa']
    qual_inicia = random.randint(0, qtd_jogadores - 1) # quem inicia o jogo aleatoriamente
    jogador_da_vez = qual_inicia
    
    jogando = True
    
    while jogando:
        
        if jogador_da_vez == 0: #Para voce jogar
            print('Sua vez de jogar')
            pecas_possiveis = domino.posicoes_possiveis(mesa, jogadores[jogador_da_vez]) # suas peças possiveis para jogar  
            print('As peças podem ser {}'.format(pecas_possiveis))     
            
            if pecas_possiveis != []: # se voce tiver peças para jogar
                print(pecas_possiveis)
                peca_jogada = int(input('Escolha a peça a ser jogada:(0/6) '))
                mesa = domino.adiciona_na_mesa(peca_jogada,mesa)
                del(jogadores[jogador_da_vez](peca_jogada))
                jogador_da_vez += 1   # para não jogar mais de uma vez

            else: # caso você não tenha peças para jogar
               
                if monte != []: # se tiver peça no monte eu eu pego uma
                    jogadores[jogador_da_vez].append(monte[0])
                    del(monte(0))
                else:
                    jogador_da_vez+=1
                    print('Voce pulou a vez')
       
        else:
            pecas_possiveis = domino.posicoes_possiveis(mesa,jogadores[jogador_da_vez])
            if pecas_possiveis != []:

                mesa = domino.adiciona_na_mesa(pecas_possiveis[0],mesa)
                del(jogadores[jogador_da_vez](pecas_possiveis[0]))
                jogador_da_vez += 1
            else:
                if monte != []:
                    jogadores[jogador_da_vez].append(monte[0])
                    del(monte[0])
                else:
                    jogador_da_vez += 1   
                    print('O jogador {} putlou a vez'.format(jogadores[jogador_da_vez]))
                                  