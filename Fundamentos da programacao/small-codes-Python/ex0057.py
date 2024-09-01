sexo = 0
while sexo!='M' and sexo!='F':
    sexo = str(input('Informe o seu sexo[M/F]: ')).upper()
    if sexo!='M' and sexo!='F':
        print('Dados inválidos. Por favor, informe seu sexo!')
    else:
        print(f'Sexo {sexo} registrado com sucesso.')