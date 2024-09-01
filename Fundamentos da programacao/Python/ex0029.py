v=int(input('Em quantos km/h você estava? '))
if v>=80:
    print('você foi multado!')
    print(f'Sua multa foi de: {((v%80+1)*7):.2f} R$')
