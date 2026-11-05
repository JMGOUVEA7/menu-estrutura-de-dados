#Menu em Python

# Criação das funções
def menu_principal():
    while True:
        print("***********************************")
        print("| Estruturas de Dados e Ordenação |")
        print("-----------------------------------")
        print("| 1 - PILHA                       |")
        print("| 2 - FILA                        |")
        print("| 3 - FILA CIRCULAR               |")
        print("| 4 - ORDENAR                     |")
        print("| 5 - SAIR                        |")
        print("-----------------------------------")
        opt1 = int(input("Digite a opção desejada: "))
        return opt1

def pilha():
    #Criar estrutura, Armazenar Valor, Extrair Valor,
    #Imprimir Conteúdo, Voltar ao Menu Anterior.
    while True:
        print("\n\n\n\n")
        print("-----------------------------------")
        print("| Pilha |")
        print("-----------------------------------")
        print("| 1 - Criar estrutura             |")
        print("| 2 - Armazenar valor             |")
        print("| 3 - Extrair valor               |")
        print("| 4 - Imprimir conteúdo           |")
        print("| 5 - Voltar ao menu anterior     |")
        print("-----------------------------------")
        opt2 = int(input("Digite a opção desejada: "))

        if opt2 == 5:
            print("Voltando ao menu anterior")
            break
        elif opt2 == 1:
            print("executar funcao init da pilha, solicitando tamanho...")
        elif opt2 == 2:
            print("chamar funcao push da pilha...")
        elif opt2 == 3:
            print("chamar funcao pop da pilha...")
        elif opt2 == 4:
            print("chamar funcao show da pilha...")
        else:
            print("Opção inexistente")
     
        return

# Programa principal
while True:
    opt1 = menu_principal()

    if opt1 == 5:
        break
    elif opt1 == 1:
        pilha()
    elif opt1 == 2:
        print("chamar menu fila...")
    elif opt1 == 3:
        print("chamar menu fila circular...")
    elif opt1 == 4:
        print("chamar menu menu ordenar...")
    else:
        print("Opção inexistente")

print("Programa finalizado")
    