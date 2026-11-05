import random

def ordenacao_selecao(A):
    n = len(A)
    # Percorre o arranjo A.
    for i in range(n):
        # Encontra o elemento mínimo em A.
        minimo = i
        for j in range(i + 1, n):
            if A[minimo] > A[j]:
                minimo = j
        # Coloca o elemento mínimo na posição correta.
        A[i], A[minimo] = A[minimo], A[i]

#A = random.sample(range(-10, 10), 10)
A = [10,2,1,9,7,8,3,5,4,6]
print("Arranjo não ordenado: \t", A)
ordenacao_selecao(A)
print("Arranjo ordenado: \t", A)