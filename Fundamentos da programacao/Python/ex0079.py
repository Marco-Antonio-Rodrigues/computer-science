lista = []
resposta = elementosdalista = 0
while True:
    numero = 0
    numero = (int(input('Digite um valor: ')))
    if len(lista) == 0:
        lista.append(numero)
    else:
        lista.append(numero)
        lista.sort()
        if len(lista) > 1:
            contador = 0
            while len(lista) != contador:
                if lista[contador] + lista[contador+1] == lista[contador]*2:
                    print('número repetido, não irei adicionar na lista!')
                    del lista[contador]
                if len(lista)-contador == 2:
                    break
                else:
                    contador += 1
    resposta = input('Quer continuar?[S/N]').upper()
    if resposta == 'N':
        break
print('=-'*30)
lista.sort()
print(f'Você digitou os valores {lista}')

