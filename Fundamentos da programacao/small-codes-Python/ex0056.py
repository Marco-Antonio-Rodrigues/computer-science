i = 0
s = 0
idade2 = 0
idade3 = 0
for cadastro in range(0,4):
    nome = input('Digite seu nome? ')
    idade = int(input('Qual a sua idade?'))
    i = i + idade
    sexo = input('Qual o seu sexo?')
    if sexo=='masculino' and idade>idade2:
        idade2=idade
        idade3=idade2
        idade3=nome
    else:
        if idade<20:
            s= s+1

print (f'A média de idade do grupo é {int(i/4)} anos')
print(f'O homem mais velho é {idade3}')
print (f'E a quantidade de mulheres com menos de 20 anos é {s}')