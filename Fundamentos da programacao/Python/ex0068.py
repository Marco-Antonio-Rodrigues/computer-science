import random
cont = s = 0
while True:
    n = random.randint(1, 10)
    nj = int(input('Escolha um número: '))
    e = (input('Você quer ser PAR ou ÍMPAR?[p/i]'))
    r = n + nj
    if r%2 == 0:
        s='PAR'
    else:
        s='ÍMPAR'
    if r%2 == 0 and e =='p':
        print(f'Você jogou {nj} e o computador jogou {n}, total de {r} e deu {s}.')
        print('Você ganhou!')
        cont = cont + 1
    elif r%2 == 1 and e =='i':
        print(f'Você jogou {nj} e o computador jogou {n}, total de {r} e deu {s}.')
        print('Você ganhou!')
        cont = cont + 1
    else:
        print(f'Você jogou {nj} e o computador jogou {n}, total de {r} e deu {s}.')
        break
print('Você perdeu!')
print(f'Você ganhou {cont} vezes.')