M = []
for i in range(5):
    L = [] #precisa zerar a lista se n vai ficar add
    for j in range(5):
        L.append(int(input(f"Digite um valor inteiro p M[{i}][{j}]: ")))
    M.append(L)
for lista in M:
    for elemento in lista:
        print(elemento, end=' ')
    print()
