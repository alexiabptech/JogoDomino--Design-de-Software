import domino 
from random import randint

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
pecas = qtd['jogadores'][sorteia_jogador]
    # mesa = 
    # posicoes = 

print('Suas peças são: ', pecas)
print('Posições possíveis',)

