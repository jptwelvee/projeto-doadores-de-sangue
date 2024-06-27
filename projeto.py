matriz = []
tipos_sanguineos = ["A", "A-", "B", "B-", "AB", "AB-", "O", "O-"]
hospitais = ["HOSPITAL 1", "HOSPITAL 2", "HOSPITAL 3"]
soma = 0
cont_linha = 0
cont_coluna = 0

menu = """
-----------------------------    menu   ---------------------------------------

    Olá usuário, nesse menu será possivel realizar essas SEIS opções de comando: 

    1 - PESQUISAR
    2 - EDITAR QUANTIDADE DE DOAÇÕES
    3 - TOTAL DE DOAÇÕES    
    4 - TAMANHO DA MATRIZ
    5 - MOSTRAR MATRIZ
    6 - ENCERRAR
--------------------------------------------------------------------------------
Desenvolvedores: Alexandre Placencia e Joao Pedro Rosa Da Silva
"""

def ler_int(msg, error_msg):
    not_inteiro = True
    while not_inteiro:
        valor = input(msg)
        not_inteiro = False 
        for digito in valor:
            if digito not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                not_inteiro = True
        if not_inteiro:
            print(error_msg)

    return int(valor)


for tipo in tipos_sanguineos:
    linha = []
    print(f"Tipo sanguíneo: {tipo}")
    for hospital in hospitais:
        doacoes = ler_int(f"Digite o número de doações para {hospital}: ", "digite um valor valido")
        linha.append(doacoes)
        soma += doacoes  
    matriz.append(linha)



print("-"*80)

def pesquisar_doacoes():
    tipo = input("Digite o tipo sanguíneo para pesquisar: ").upper()
    hospital = input("Digite o hospital para pesquisar: ").upper()
    
    if tipo in tipos_sanguineos and hospital in hospitais:
        tipoPesquisa = tipos_sanguineos.index(tipo)
        hospitalPesquisa = hospitais.index(hospital)
        doacoes = matriz[tipoPesquisa][hospitalPesquisa]
        print("-"*60)
        print(f"O número de doações para o tipo sanguíneo {tipo} no {hospital} é: {doacoes}")
        
    else:
        print("Tipo sanguíneo ou hospital inválido.") 

def editar_doacoes(soma):
    tipo = input("Digite o tipo sanguíneo para editar: ").upper()
    hospital = input("Digite o hospital para editar: ").upper()
    if tipo in tipos_sanguineos and hospital in hospitais:
        tipoEditar = tipos_sanguineos.index(tipo)
        hospitalEditar = hospitais.index(hospital)
        
        novo_valor = ler_int(f"Digite o novo número de doações para o tipo sanguíneo {tipo} no {hospital}: ", "Digite um valor válido.")
        soma_anterior = matriz[tipoEditar][hospitalEditar]
        matriz[tipoEditar][hospitalEditar] = novo_valor
    
        soma = soma - soma_anterior + novo_valor
        
        print(f"O número de doações para o tipo sanguíneo {tipo} no {hospital} foi atualizado para: {novo_valor}")
    else:

        print("Tipo sanguíneo ou hospital inválido.")
    
    return soma

def linha_coluna():
    cont_linha = len(matriz) 
    cont_coluna = len(matriz[0]) if matriz else 0  
    print(f'Total: {cont_linha} linhas x {cont_coluna} colunas')

def mostrar_matriz():
    print("Matriz de Doações:")
    print("            ", " | ".join(hospitais))
    for i, tipo in enumerate(tipos_sanguineos):
        linha = " | ".join(f"{x:3}" for x in matriz[i])
        print(f"{tipo:8}: {linha}")

print(menu)

while True:
    opcao = (input("O que você deseja realizar?: ")).strip().upper()
    print("-" * 80)

    if opcao == "1":
        pesquisar_doacoes()
    elif opcao == "2":
        soma = editar_doacoes(soma)
    elif opcao == "3":
        print(f"O total de doações que tivemos foi de: {soma} pessoas")
    elif opcao == "4":
        linha_coluna()
    elif opcao == "5":
        mostrar_matriz()
    elif opcao == "6":
        print("-" * 80)
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.")











