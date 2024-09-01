nota1 = float(input('diga a sua primeira nota:'))
nota2 = float(input('diga a sua segunda nota:'))
media = (nota1+nota2)/2
if media>7:
    print('Aprovado')
elif 5<media<6.9:
    print('Recuperação')
else:
    print('reprovado')