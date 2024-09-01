reta1 = float(input('Qual o comprimento da primeira reta?'))
reta2 = float(input('Qual o comprimento da segunda reta?'))
reta3 = float(input('Qual o comprimento e da terceira reta?'))
teste1 = bool(reta1+reta2>reta3)
teste2 = bool(reta2+reta3>reta1)
teste3 = bool(reta1+reta3>reta2)
resultado = teste1+teste3+teste2
if resultado==3:
    print('Pode formar um triângulo!')
    if reta1==reta2==reta3:
        print('é um triângulo equilátero!')
    elif reta1==reta2 or reta2==reta3 or reta1==reta3:
        print('é um triângulo isósceles!')
    else:
        print('é um triângulo escaleno!')

else:
    print('Não pode formar um triângulo!')

