import domino 
import random  
jogando = True
while jogando :
    print('Olá, bem-vindo ao Jogo Dominó!')
    #Define-se o numero
    num_jog = int(input('Qual a quantidade de participantes?: '))
    print(num_jog)

    #Aqui, estamos pedindo pra que printe, de acordo com a nossa função  cria_pecas, pra que mostre a atd de peças disponiveis para a devida quantidade de jogadores
    #Aqui, cada jogador recebe 7 peças, aí as peças remanescentes vão para o monte
    lista_pecas = domino.cria_pecas()
    qtd = domino.inicia_jogo(num_jog, lista_pecas)
    #print(qtd)


    sorteia_jogador = random.randint(0,num_jog-1)
        #Inicia o jogo:
        #Para iniciar o jogo, temos que mostrar as peças que estão 
        # dispostas para o jogador
    pecas = qtd['jogadores'][0]
        # mesa = 
        # posicoes = 

    print('O jogador {} inicia o jogo.'.format(sorteia_jogador))
    print('Suas peças são {}'.format(pecas))
    #print('Posições possíveis',)

    
