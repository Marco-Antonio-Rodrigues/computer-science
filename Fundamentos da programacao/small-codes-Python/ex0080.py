lista = []
for c in range(0,3):
    numero = 0
    numero = int(input('Digite um número: '))
    if len(lista) == 0:
        lista.append(numero)
    else:
        if len(lista) == 1:
            if lista[0]> numero:
                lista.insert(0,numero)
            else:
                lista.append(numero)
        else:
            if len(lista) == 2:
                if lista[0] > numero < lista[1]:
                    print(lista)
                    if numero > lista[1]:
                        lista.insert(1,numero)
                    else:
                        lista.insert(2,numero)
                else:
                    if lista[0]>numero:
                        lista.insert(0,numero)
                    else:
                        lista.append(numero)
    print(f'fim{lista}')




