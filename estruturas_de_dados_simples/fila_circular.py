global fila, spos, rpos, MAX

def init(maximo):
    global fila, spos, rpos, MAX

    MAX = maximo
    fila = []
    for i in range(0,MAX):
        fila.append(None)

    spos = 0
    rpos = 0

def push(valor):
    global fila, spos

    if (rpos == spos and fila[rpos] != None) or (spos == MAX and rpos == 0):
        print("\nFila Vazia!!")
        return
    if spos == MAX and rpos != 0:
        spos = 0

    fila[spos] = valor
    spos = spos + 1
    return

def pop():
    global fila, rpos

    if rpos == spos and fila[rpos] == None:
        print("Fila Vazia!!")
        return
    if rpos == MAX:
        rpos = 0
    valor = fila[rpos]
    fila[rpos] = None
    rpos = rpos + 1
    return valor

def show():
    for i in range(0, MAX):
        print(fila[i])
    return None

def showp():
    print(' rpos = ', rpos, ' spos = ', spos, ' MAX = ', MAX)
    return

# Testando a Fila Circular
init(5)
push(10)
push(20)
push(30)
push(40)
push(50)
show()
pop()
show()
showp()
input()
push(60)
show()
showp()