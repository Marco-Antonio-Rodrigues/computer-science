import random
n=int(random.randint(0,5))
n1=int(input('adivinhe o número que pensei de 0 ao 5: '))
if n==n1:
    print('\033[42mParabéns você acertou!\033[m')
else:
    print('\033[41mVocê perdeu!\033[m')