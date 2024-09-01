lista = []
for cont in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {cont}: ')))
print(f'você digitou os valores: {lista}')
lista1 = lista[:]
lista1.sort()
elementos = len(lista)
print(f'O maior valor digitado foi {lista1[-1]} nas posições',end='')
for cont in range(0,elementos):
    if lista1[-1] == lista[cont]:
        print(f' {cont}...', end='')
print( )
print(f'O menor valor digitado foi {lista1[0]} nas posições',end='')
for cont in range(0,elementos):
    if lista1[0]== lista[cont]:
            print(f' {cont}...',end='')