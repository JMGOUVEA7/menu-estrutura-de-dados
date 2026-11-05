global fila, spos, rpos, MAX
MAX = 5
fila = []
spos = 0
rpos = 0

def push(valor): #adiciona
    global spos, rpos, fila     
    if spos == MAX:
        print("\nFila cheia")
        return
    
    fila.append(valor)
    spos = spos+1
    return

def pop(): #remove valor
    global spos, rpos, fila     
    if rpos == spos:
        print("\nFila Vazia!!!")
        return None
    
    rpos = rpos + 1
    return fila[rpos-1]

def show(): 
    global spos, rpos, fila    
    if rpos == spos:
        print("\nFila Vazia")
        return 
    
    for i in range(rpos,spos):
        print(fila[i])

    return

def showp():
    global spos, rpos, fila 
    print("rpos = ",rpos,"    spos = ", spos)
    return
