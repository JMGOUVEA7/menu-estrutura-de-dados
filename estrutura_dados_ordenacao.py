import time

# Algoritmos de ordenacao
def bubble_sort(A):
    n = len(A)
    for i in range(n):
        for j in range(n - 1 - i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
    return A

def selection_sort(A):
    for i in range(len(A)):
        minimo = i
        for j in range(i + 1, len(A)):
            if A[j] < A[minimo]:
                minimo = j
        A[i], A[minimo] = A[minimo], A[i]
    return A

def insertion_sort(A):
    for j in range(1, len(A)):
        chave = A[j]
        i = j - 1
        while i >= 0 and A[i] > chave:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = chave
    return A


# Um unico vetor compartilhado pelas tres estruturas.
dados = []
estrutura = None
capacidade = 0

# Controle da fila linear.
rpos = 0
spos = 0

# Controle da fila circular.
inicio_circular = 0
fim_circular = 0
quantidade_circular = 0


def criar_estrutura(tipo):
    global estrutura, capacidade, rpos, spos
    global inicio_circular, fim_circular, quantidade_circular

    while True:
        try:
            tamanho = int(input("Digite o tamanho da estrutura: "))
            if tamanho > 0:
                break
            print("O tamanho deve ser maior que zero.")
        except ValueError:
            print("Digite um numero inteiro valido.")

    estrutura = tipo
    capacidade = tamanho
    rpos = spos = 0
    inicio_circular = fim_circular = quantidade_circular = 0

    if tipo == "circular":
        dados[:] = [None] * capacidade
    else:
        dados[:] = []

    print(f"Estrutura {tipo} criada com capacidade {capacidade}.")


def armazenar_valor():
    global spos, fim_circular, quantidade_circular

    try:
        valor = int(input("Digite o valor: "))
    except ValueError:
        print("Digite um numero inteiro valido.")
        return

    if estrutura == "pilha":
        if len(dados) >= capacidade:
            print("Pilha cheia!")
            return
        dados.append(valor)

    elif estrutura == "fila":
        if spos >= capacidade:
            print("Fila cheia!")
            return
        dados.append(valor)
        spos += 1

    elif estrutura == "circular":
        if quantidade_circular >= capacidade:
            print("Fila circular cheia!")
            return
        dados[fim_circular] = valor
        fim_circular = (fim_circular + 1) % capacidade
        quantidade_circular += 1

    print("Valor armazenado com sucesso.")


def extrair_valor():
    global rpos, inicio_circular, quantidade_circular

    if estrutura == "pilha":
        if not dados:
            print("Pilha vazia!")
            return
        print("Valor extraido:", dados.pop())

    elif estrutura == "fila":
        if rpos >= spos:
            print("Fila vazia!")
            return
        print("Valor extraido:", dados[rpos])
        rpos += 1

    elif estrutura == "circular":
        if quantidade_circular == 0:
            print("Fila circular vazia!")
            return
        valor = dados[inicio_circular]
        dados[inicio_circular] = None
        inicio_circular = (inicio_circular + 1) % capacidade
        quantidade_circular -= 1
        print("Valor extraido:", valor)


def obter_elementos_ativos():
    if estrutura == "pilha":
        return dados.copy()
    if estrutura == "fila":
        return dados[rpos:spos]
    if estrutura == "circular":
        return [dados[(inicio_circular + i) % capacidade]
                for i in range(quantidade_circular)]
    return []


def imprimir_conteudo():
    if estrutura == "pilha":
        print("Pilha (base para topo):", dados)
    elif estrutura == "fila":
        print("Fila (inicio para fim):", dados[rpos:spos])
    elif estrutura == "circular":
        print("Vetor dados:", dados)
        print("Fila circular (inicio para fim):", obter_elementos_ativos())


def atualizar_estrutura(valores):
    global fim_circular

    if estrutura == "pilha":
        dados[:] = valores
    elif estrutura == "fila":
        dados[rpos:spos] = valores
    elif estrutura == "circular":
        dados[:] = [None] * capacidade
        for i, valor in enumerate(valores):
            dados[(inicio_circular + i) % capacidade] = valor
        fim_circular = (inicio_circular + quantidade_circular) % capacidade


def executar_ordenacao(nome, algoritmo):
    if estrutura is None:
        print("\\nNenhuma estrutura foi criada.")
        print("Escolha primeiro PILHA, FILA ou FILA CIRCULAR e crie a estrutura.")
        return

    valores = obter_elementos_ativos()
    if not valores:
        print("\\nA estrutura esta vazia. Armazene valores antes de ordenar.")
        return

    print("\\nAntes da ordenacao:", valores)
    inicio = time.perf_counter()
    algoritmo(valores)
    fim = time.perf_counter()

    atualizar_estrutura(valores)
    print("Depois da ordenacao:", valores)
    print("Algoritmo:", nome)
    print(f"Tempo de execucao: {fim - inicio:.10f} segundos")


def menu_estrutura(tipo):
    while True:
        print(f"\\n===== {tipo.upper()} =====")
        print("1. Criar estrutura")
        print("2. Armazenar valor")
        print("3. Extrair valor")
        print("4. Imprimir conteudo")
        print("5. Voltar ao menu anterior")
        opcao = input("Digite a opcao desejada: ")

        if opcao == "1":
            criar_estrutura(tipo)
        elif opcao in ("2", "3", "4"):
            if estrutura != tipo:
                print("Crie primeiro esta estrutura.")
            elif opcao == "2":
                armazenar_valor()
            elif opcao == "3":
                extrair_valor()
            else:
                imprimir_conteudo()
        elif opcao == "5":
            break
        else:
            print("Opcao invalida.")


def menu_ordenar():
    while True:
        print("\\n===== ORDENAR =====")
        print("1. Bubble Sort")
        print("2. Selection Sort")
        print("3. Insertion Sort")
        print("4. Voltar ao menu anterior")
        opcao = input("Digite a opcao desejada: ")

        if opcao == "1":
            executar_ordenacao("Bubble Sort", bubble_sort)
        elif opcao == "2":
            executar_ordenacao("Selection Sort", selection_sort)
        elif opcao == "3":
            executar_ordenacao("Insertion Sort", insertion_sort)
        elif opcao == "4":
            break
        else:
            print("Opcao invalida.")


def menu_principal():
    while True:
        print("\\n***********************************")
        print("| Estruturas de Dados e Ordenacao |")
        print("-----------------------------------")
        print("| 1 - PILHA                       |")
        print("| 2 - FILA                        |")
        print("| 3 - FILA CIRCULAR               |")
        print("| 4 - ORDENAR                     |")
        print("| 5 - SAIR                        |")
        print("***********************************")
        opcao = input("Digite a opcao desejada: ")

        if opcao == "1":
            menu_estrutura("pilha")
        elif opcao == "2":
            menu_estrutura("fila")
        elif opcao == "3":
            menu_estrutura("circular")
        elif opcao == "4":
            menu_ordenar()
        elif opcao == "5":
            print("Programa finalizado.")
            break
        else:
            print("Opcao invalida.")


if __name__ == "__main__":
    menu_principal()
