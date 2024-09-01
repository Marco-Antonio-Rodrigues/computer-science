casa = int(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
anos = int(input('Em quantos anos você quer pagar? '))
valor_prestação = casa/(anos*12)
porcetagem = float(salario*0.3)
print(f'O valor da prestação é de R${valor_prestação} mensais')
if valor_prestação<porcetagem:
    print('\033[;42mAprovado! hehe\033[m')
else:
    print('\033[;41mnegado seu pobre!\033[m')