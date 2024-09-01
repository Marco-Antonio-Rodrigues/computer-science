n1 = n2 = n3 = 0
while n3!=5:
    if n3==4:
        print('Reiniciando...')
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite um número: '))
    print("""
    Menu:
    [1]somar
    [2]multiplicar
    [3]maior
    [4]novos números
    [5]sair do programa
    """)
    n3 = int(input('Qual opção?'))
    if n3 == 1:
        print(n1+n2)
    elif n3 == 2:
        print(n1*n2)
    elif n3 == 3:
        if n1>n2:
            print(n1)
        else:
            print(n2)
print('Fim!')

