import random

def ordenacao_insercao(A):
    n = len(A)
    # Percorre o arranjo A.
    for j in range(1, n):
        chave = A[j]
        i = j - 1
        # Insere o elemento A[j] na posição correta.
        while i >= 0 and A[i] > chave:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = chave

#A = random.sample(range(1, 11), 10000)
#
A = [10,2,1,9,7,8,3,5,4,6]
#A= [2,10,1,9,7,8,3,5,4,6]
#A= [
print("Arranjo não ordenado: \t", A)

ordenacao_insercao(A)

print("Arranjo ordenado: \t", A)