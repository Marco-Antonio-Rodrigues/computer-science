ano = int(input('Qual o seu ano de nascimento?'))
tempo = 2021-ano
if tempo>18:
    print(f'Já passou seu tempo de alistamento em {tempo-18}.')
elif tempo == 18:
    print('Está na hora de você se alistar!')
else:
    print(f'Ainda não precisa se alistar, ainda falta {18-tempo}anos')
