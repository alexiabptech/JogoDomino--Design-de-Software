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
      

    


    