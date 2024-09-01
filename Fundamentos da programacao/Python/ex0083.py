lista = []
contador = 0
validador = (input('Digite uma expressão: '))
for c in range(len(validador)):
    lista.append(validador[c])
contador = vezesdedireita = vezesdeesquerda = 0
while contador != len(lista):
    if '(' in lista[contador]:
        vezesdedireita += 1
        contador += 1
    else:
        contador += 1
contador = 0
while contador != len(lista):
    if ')' in lista[contador]:
        vezesdeesquerda += 1
        contador += 1
    else:
        contador += 1
if vezesdeesquerda == vezesdedireita:
    print('Sua expressão é válida!')
else:
    print('Sua expressão não é válida!')