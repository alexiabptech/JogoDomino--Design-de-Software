import domino 
import random
jogar = input('Você quer iniciar o jogo?(sim/não) ')
while jogar == 'sim':
    print('Olá, bem-vindo ao Jogo Dominó!')
    #Define-se o numero
    num_jog = int(input('Qual a quantidade de participantes?: '))

    #Aqui, estamos pedindo pra que printe, de acordo com a nossa função  cria_pecas, pra que mostre a atd de peças disponiveis para a devida quantidade de jogadores
    #Aqui, cada jogador recebe 7 peças, aí as peças remanescentes vão para o monte
    lista_pecas = domino.cria_pecas()
    divisao_pecas = domino.inicia_jogo(num_jog, lista_pecas)
    print(divisao_pecas)
    mesa = []
    jogando = True
    while jogando:
        sorteia_jogador = random.randint(0,num_jog-1)
        #Inicia o jogo:
        #Para iniciar o jogo, temos que mostrar as peças que estão 
        # dispostas para o jogador
        suas_pecas = divisao_pecas['jogadores'][0] 

        print('O jogador {} inicia o jogo.'.format(sorteia_jogador))
        print('Suas peças são {}'.format(suas_pecas))
        if sorteia_jogador == 0:
            print(suas_pecas)
            posicao_peca = int(input('Escolha a posição da peça que deseja jogar: ')) #DE 0 a 6
            peca_jogada = suas_pecas[posicao_peca]
            mesa.append(peca_jogada)
        
        else:
            
            peca_jogada = divisao_pecas['jogadores'][sorteia_jogador] #Pega a chave do jogador que foi sorteado
            mesa.append(peca_jogada)    
        
        print(mesa)

            

