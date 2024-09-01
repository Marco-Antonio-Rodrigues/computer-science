n = 22
while True:
    contagem = 'zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatoze','quinze','dizesseis','dizesete','dezoito','dezenove','vinte'
    n = int(input('Digite um número entre 0 e 20: '))
    if n >= 0 and n <= 20:
        print(f'O número por extenso é {contagem[n]}')
        escolha = input('Quer continuar?[s/n]')
        if escolha == 'n':
            break
    else:
        print('Tente novamente! Digite um número de 0 a 20')



