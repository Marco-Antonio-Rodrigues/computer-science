import emoji
import random
jogador = input('qual você escolheu?')
maquina = random.randint(1,3)

if maquina==1:
    maquina='pedra'
elif maquina==2:
    maquina='papel'
elif maquina==3:
    maquina='tesoura'

print(f'Eu escolhi {maquina} e você {jogador}')



if maquina=='tesoura' and jogador=='papel':
    print('Eu ganhei!')
elif maquina=='pedra' and jogador=='tesoura':
    print('Eu ganhei!')
elif maquina=='papel' and jogador=='pedra':
    print('Eu ganhei!')

if jogador=='tesoura' and maquina=='papel':
    print('voc6e ganhou!')
elif jogador=='pedra' and maquina=='tesoura':
    print('Você ganhou!')
elif jogador=='papel' and maquina=='pedra':
    print('Você ganhou!')

if jogador=='tesoura' and maquina=='tesoura':
    print('empatamos!')
elif jogador=='pedra' and maquina=='pedra':
    print('empatamos!')
elif jogador=='papel' and maquina=='papel':
    print('empatamos!')



