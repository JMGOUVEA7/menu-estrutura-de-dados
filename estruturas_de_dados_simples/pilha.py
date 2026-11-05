global pilha, ponteiro, MAX

def inicializa():
    global pilha, ponteiro
    MAX = 5
    pilha = []
    ponteiro = -1
    return

def push(valor):
    global pilha, ponteiro, MAX
    
    if ponteiro == MAX-1:
        print("\nPilha Cheia!!!")
        return
    
    pilha.append(valor)
    ponteiro = ponteiro + 1
    return

def pop():
    global pilha, ponteiro
    
    if ponteiro < 0:
        print("\nPilha Vazia!!!")
        return
    else:
        valor = pilha[ponteiro]
        del(pilha[ponteiro])
        ponteiro = ponteiro - 1
        return(valor)

def show():
    global pilha
    print(pilha)

'''
# Testando o funcionamento da pilha    
inicializa()
push(10)
push(20)
push(30)
push(40)
show()
a = pop()
show()
print(pop())
show()
print(pop())
print(pop())
show()
pop()
'''