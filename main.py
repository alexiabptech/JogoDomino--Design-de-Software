import domino
import random
from cores import *

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
        
        print('MESA: ', mesa)
        print('\n')
        if jogador_da_vez == 0: #Para voce jogar
            print('Sua vez de jogar')
            pecas_possiveis = domino.posicoes_possiveis(mesa, jogadores[jogador_da_vez]) # suas peças possiveis para jogar  
            print('As peças que voce tem {}'.format(div_jogo['jogadores'][0]))  
            pecas_disponiveis = [div_jogo['jogadores'][0][i] for i in pecas_possiveis]
            print(colorindo('As peças que voce pode jogar {}'.format(pecas_disponiveis),'ciano'))  
            print(colorindo('As posicoes das peças que voce pode jogar {}'.format(pecas_possiveis), 'amarelo'))     
            
            if pecas_possiveis != []: # se voce tiver peças para jogar
                #print(pecas_possiveis)
                peca_jogada = int(input('Escolha a peça a ser jogada:(0/6) '))
                mesa = domino.adiciona_na_mesa(jogadores[jogador_da_vez][peca_jogada], mesa)
                jogadores[jogador_da_vez].pop(peca_jogada)
                print('Voce colocou a peça: ', peca_jogada)
                #del(jogadores[jogador_da_vez][peca_jogada])
                jogador_da_vez += 1   # para não jogar mais de uma vez

                if peca_jogada not in pecas_possiveis:
                    print('Você não possui essa peça.')
                    peca_jogada = int(input('Escolha outra peça válida: '))
                    mesa = domino.adiciona_na_mesa(jogadores[jogador_da_vez][peca_jogada], mesa)
                    jogadores[jogador_da_vez].pop(peca_jogada)
                    print('Voce colocou a peça: ', peca_jogada)
                    #del(jogadores[jogador_da_vez][peca_jogada])
                    jogador_da_vez += 1   # para não jogar mais de uma vez

                else:

                    mesa = domino.adiciona_na_mesa(jogadores[jogador_da_vez][peca_jogada], mesa)
                    jogadores[jogador_da_vez].pop(peca_jogada)
                    print('Voce colocou a peça: ', peca_jogada)
                    #del(jogadores[jogador_da_vez][peca_jogada])
                    jogador_da_vez += 1   # para não jogar mais de uma vez

            else: # caso você não tenha peças para jogar
               
                if monte != []: # se tiver peça no monte eu eu pego uma
                    while domino.posicoes_possiveis(mesa, jogadores[jogador_da_vez]) == [] and monte != []:
                        jogadores[jogador_da_vez].append(monte[0])
                        monte.pop(0)
                    if domino.posicoes_possiveis(mesa, jogadores[jogador_da_vez]) != []:
                        mesa = domino.adiciona_na_mesa(jogadores[jogador_da_vez][-1], mesa)
                        print('Voce colocou a peça: ', peca_jogada)
                        jogador_da_vez += 1
                    elif monte == []:
                        jogador_da_vez += 1
                        print('Voce pulou a vez')

                else:
                    jogador_da_vez += 1
                    print('Voce pulou a vez')
       
        else:
            pecas_possiveis = domino.posicoes_possiveis(mesa, jogadores[jogador_da_vez])
            if pecas_possiveis != []:
                mesa = domino.adiciona_na_mesa(jogadores[jogador_da_vez][pecas_possiveis[0]],mesa)
                print(f'O jogador {jogador_da_vez} colocou a peça: {jogadores[jogador_da_vez][pecas_possiveis[0]]}')
                jogadores[jogador_da_vez].pop(pecas_possiveis[0])
                # del(jogadores[jogador_da_vez][pecas_possiveis[0]])
                jogador_da_vez += 1
            else:
                if monte != []:
                    # jogadores[jogador_da_vez].append(monte[0])
                    # del(monte[0])
                    while domino.posicoes_possiveis(mesa, jogadores[jogador_da_vez]) == [] and monte != []:
                        jogadores[jogador_da_vez].append(monte[0])
                        monte.pop(0)
                    if domino.posicoes_possiveis(mesa, jogadores[jogador_da_vez]) != []:
                        mesa = domino.adiciona_na_mesa(jogadores[jogador_da_vez][-1], mesa)
                        print(f'O jogador {jogador_da_vez} colocou a peça ', jogadores[jogador_da_vez][-1])
                        jogador_da_vez += 1
                    elif monte == []:
                        jogador_da_vez += 1
                        print('O jogador {} pulou a vez'.format(jogador_da_vez)) 
                else:
                    jogador_da_vez += 1   
                    print('O jogador {} pulou a vez'.format(jogador_da_vez)) 
        
        if domino.verifica_ganhador(jogadores) != -1:
            if jogador_da_vez == 0:
                print('Parabéns, você venceu!!!')
            else:    
                print(f'O jogador {jogador_da_vez} venceu')
                jogando = False

        if jogador_da_vez >= qtd_jogadores:
            jogador_da_vez = 0
        # else:
        #     jogador_da_vez += 1
    resposta = input("Quer continuar jogando? ")
    if resposta != 'sim':
        print('Adeus :)')

