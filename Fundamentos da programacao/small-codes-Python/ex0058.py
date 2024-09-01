import random
n=int(random.randint(0,10))
n1 = 0
p = 1
while n!=n1:
    n1 = int(input('adivinhe o número que pensei de 0 ao 10: '))
    if n!=n1:
        print('\033[41mVocê errou! Tente novamente.\033[m')
        p += 1
    else:
        print('\033[42mParabéns você acertou!\033[m')
        print(f'Você precisou de {p} palpites para acertar')
