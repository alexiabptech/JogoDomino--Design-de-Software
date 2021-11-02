def adiciona_na_mesa (peca, mesa):
    print(mesa, peca)
    if mesa == []:
        mesa.append(peca)

    elif peca[1] ==mesa[0][0]:
        mesa.insert(0,peca)
    
    elif peca[0] == mesa[0][0]:
        peca.reverse()
        mesa.insert(0,peca) 

    elif peca[1] == mesa[-1][1]:
        peca.reverse()
        mesa.append(peca) 

    elif peca[0] == mesa[-1][1]:
        mesa.append(peca)

    return mesa  