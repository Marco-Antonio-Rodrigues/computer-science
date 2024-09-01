listageral = []
listadepares = []
listadeimpares = []
while True:
    numero = int(input(f'Digite um número: '))
    listageral.append(numero)
    if numero % 2 == 0:
        listadepares.append(numero)
    else:
        listadeimpares.append(numero)
    resposta = str(input('Você quer continuar?[S/N]').upper())
    if resposta == 'N':
        break
print('=-'*30)
print(f'A lista completa é: {listageral}')
print(f'A lista de pares é: {listadepares}')
print(f'A lista de ímpares é: {listadeimpares}')
