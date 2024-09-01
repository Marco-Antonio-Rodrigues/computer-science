lista = []
while True:
    numero = int(input('Digite um número: '))
    lista.append(numero)
    resposta = str(input('Quer continuar?[S/N]').upper())
    if resposta == 'N':
        break

print('=-'*30)
print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordens decrescentes são {lista}')
if 5 in lista:
    print('O valor 5 está contido na lista.')
else:
    print('5 não está contido na lista.')

