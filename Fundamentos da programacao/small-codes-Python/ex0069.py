escolha = demaiores = homens = mulheres = 0
while True:
    idade = sexo = 0
    while idade == 0:
        idade = int(input('Digite a idade: '))
    if idade > 18:
        demaiores += 1
    while sexo != 'M' and sexo != 'F':
        sexo = input('Digite o sexo[M/F]: ').upper()
    if sexo == 'M':
        homens += 1
    else:
        if idade < 20:
            mulheres += 1
    escolha = input('Quer continuar? [S/N]:').upper()
    if escolha == 'N':
        break
print(f"""
{demaiores} pessoa(s) tem mais de 18 anos.

Foram cadastrado(s) {homens} homens.

Foram cadastrada(s) {mulheres} mulheres com idade abaixo de 20 anos.
""")
