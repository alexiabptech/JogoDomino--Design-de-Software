import domino 
print('Olá, bem-vindo ao Jogo Dominó!')
num_jog = int(input('Qual a quantidade de participantes?: '))
print(num_jog)


lista_pecas = domino.cria_pecas()
qtd = domino.inicia_jogo(num_jog, lista_pecas)
print(qtd)

