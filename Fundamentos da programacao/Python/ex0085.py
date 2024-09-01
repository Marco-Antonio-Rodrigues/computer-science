# recebe como entrada 7 valores numéricos
#coloque eles na lista principal
#separar dentro da lista os valores ímpares e pares dentro de mais duas listas
#mostrar os valores pares e ímpares em ordem crescente
pares = list()
impares = list()
numeros = [pares, impares]
entrada = 0
for entrada in range(1,8):
    entrada  = (int(input(f'Digite o {entrada}* número: ')))
    if entrada%2 == 0:
        pares.append(entrada)
    else:
        impares.append(entrada)
print('-='*30)
pares.sort()
impares.sort()
print(f'Os valores pares digitados foram: {pares}')
print(f'Os valores impares digitados foram: {impares}')
