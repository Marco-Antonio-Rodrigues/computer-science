# Por: Marco Antonio Rodrigues Gomes de Souza

# Tem como função ser um pequeno gerenciador de séries sem banco de dados, 
# então nada é salvo definitivamente.

escolha = contador = pesquisa = 0
lista_de_series = []
dados_do_filme = []
soma = 0.0

while escolha != 9:
    escolha = 0
    sub_escolha = 0
    print ("=-=-=-=-=-=-=-=| MENU INICIAL|=-=-=-=-=-=-=-=")
    print("1- Cadastrar série de TV")
    print("2- Consulta série de TV adicionada")
    print("3- gerar listagens das séries de TV")
    print("9- sair")
    escolha = int(input(":"))
    
    while escolha == 1 and sub_escolha != 2:
        sub_escolha = 0
        dados_do_filme.append(str(input("Nome da série: ")))
        dados_do_filme.append(int(input("Quantidade de episódios: ")))
        dados_do_filme.append(int(input("número do último episódio assistido: ")))
        lista_de_series.append(dados_do_filme[:])
        dados_do_filme.clear()
        print("Continuar?")
        print("1- sim")
        print("2- não")
        sub_escolha = int(input(":"))
        
    while escolha == 2 and sub_escolha != 2:
        contador = resultados = sub_escolha = 0
        pesquisa = str(input("Qual o nome da série?"))
        while contador < len(lista_de_series):
            if len(lista_de_series) != 0:
                if lista_de_series[contador][0] == pesquisa:
                    print(f"{lista_de_series[contador][0]}")
                    print(f"Número de episódios: {lista_de_series[contador][1]}")
                    print(f"último episódio assistido: {lista_de_series[contador][2]}")
                    print(f"Você assistiu {(lista_de_series[contador][2]/lista_de_series[contador][1])*100:,.2f}%")
                    resultados = resultados + 1
            contador = contador + 1
        if resultados == 0:
            print("Série não encontrada")
        print("Continuar?")
        print("1- sim")
        print("2- não")
        sub_escolha = int(input(":"))
        
    while escolha == 3 and sub_escolha != 2:
        contador = sub_escolha = subcontador = soma = 0
        if len(lista_de_series) == 0:
            print("Não a séries cadastradas")
        while contador < len(lista_de_series):
            print(f"A série {lista_de_series[contador][0]} tem {lista_de_series[contador][1]} episódios e você assistiu até o {lista_de_series[contador][2]},{(lista_de_series[contador][2]/lista_de_series[contador][1])*100}% assistido")
            contador = contador + 1
        while subcontador < len(lista_de_series):
            soma = soma + (lista_de_series[subcontador][2]/lista_de_series[subcontador][1])
            subcontador = subcontador + 1
        soma = (soma/subcontador)*100
        print(f"Você assistiu {soma:,.2f}% de todas as séries")
        print("Continuar?")
        print("1- sim")
        print("2- não")
        sub_escolha = int(input(":"))