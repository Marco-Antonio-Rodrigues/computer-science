n = int(input('Digite um número e veja seu fatorial: '))
f = n
m=1
while f > 0:
    m *= f
    if f == n:
        print(f'{n}!=', end='')
    if f != 1:
     print(f'{f}',end='x')
    else:
        print(f'{f} = {m}')
    f -= 1

