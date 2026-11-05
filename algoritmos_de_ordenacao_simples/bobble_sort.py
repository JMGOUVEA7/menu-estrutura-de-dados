import random

def ordenacao_bolha(A):
    n = len(A)

    for i in range(n):
        for j in range (0,len(A)-1):  
            if (A[j]>A[j+1]):
                temp = A[j]  
                A[j] = A[j+1]  
                A[j+1] = temp

A = random.sample(range(-10, 10), 10)
print("Arranjo não ordenado: \t", A)

ordenacao_bolha(A)

print("Arranjo ordenado: \t", A)