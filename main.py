#Primeiro iniciamos o Jogo criando as peças:

import random
def cria_pecas(): 
#para i variando de 0 a 6, então devolva uma lista com todas as combinaçoes de 0 a 6 e um j fixo:
   lista_domino = []

   for i in range(0,7):
      for j in range(0,7):
         lista_peca = [i,j] #Varia primeiro o j até o 6 e depois volta pro primeiro for, variando o i
         lista_peca.sort()
         if lista_peca not in lista_domino: #Aqui eu estou dizendo que se a peca não está dentro da lista domino então adiciona 
            lista_domino.append(lista_peca)
   
   random.shuffle(lista_domino)
   return lista_domino 

#Depois, Verificamos o numero de jogadores, para podermos distribuirmos as peças, assim o que sobra vai pro monte.
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

#Essa função analisa as peças remanescentes do jogadores e devolve o vencedor, ou seja, aquele que não possuir mais peças.
def verifica_ganhador(num_jog):
#num_jogadores = {numero: lista_peças}
#return posicao do jogador sem peças
    for jogador, pecas in num_jog.items():
        if pecas == []:
            return jogador
    
    return -1