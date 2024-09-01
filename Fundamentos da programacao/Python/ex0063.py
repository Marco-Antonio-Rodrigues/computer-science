n = int(input('Digite um número: '))
n1 = n3 = 0
n2 = 1
cont = 1
if n == 1:
    print(f'{n1}')
else:
    while cont <= n:
        if cont == n:
            print(f'{n3}', end='')
        else:
            print(f'{n3}',end=',')
        n1 = n2
        n2 = n3
        n3 = n1 + n2
        cont += 1
