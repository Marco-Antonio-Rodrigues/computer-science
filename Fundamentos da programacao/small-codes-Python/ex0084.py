listageral = []
listabreve = []
listapesados = []
resposta = nome = peso = pesoanterior = 0
pesoleve = 1000000000000000000000000000000000000000000000000000000000000000000
listaleves = []
while resposta != 'N':
    contador = 0
    nome = input('nome: ')
    peso = float(input('peso: '))
    listabreve.append(nome)
    listabreve.append(peso)
    listageral.append(listabreve[:])
    listabreve.clear()
    resposta = input('Quer continuar?[S/N]').upper()
while contador != len(listageral):
    if listageral[contador][1] > pesoanterior:
        pesoanterior = listageral[contador][1]
        listapesados.clear()
        listapesados.append(listageral[contador][0])
        contador += 1
    elif  listageral[contador][1] == pesoanterior:
        listapesados.append(listageral[contador][0])
        contador += 1
    else:
        contador +=1
contador = 0
while contador != len(listageral):
    if listageral[contador][1] < pesoleve:
        pesoleve = listageral[contador][1]
        listaleves.clear()
        listaleves.append(listageral[contador][0])
        contador += 1
    elif  listageral[contador][1] == pesoleve:
        listaleves.append(listageral[contador][0])
        contador += 1
    else:
        contador +=1
print(f'Ao todo, você cadastrou {len(listageral)} pessoas')
print(f'O maior peso foi de {pesoanterior}kg. peso de {listapesados}')
print(f'O menor peso foi de {pesoleve}kg. peso de {listaleves}')