M = []
tam_matriz = 10
for i in range(tam_matriz):
    L = []
    for j in range(tam_matriz):
        L.append(int(input(f"Digite um numero inteiro [{i}][{j}]: ")))
    M.append(L)
for lista in M:
    for elemento in lista:
        print(elemento, end=' ')
    print()


for col in range(len(M)):
    aux = M[8][col]   #guarda o valor antigo da linha 8
    aux_2 = M[9][col] #guarda o valor antigo da linha 9
    # troca a linha 8 pela 2 e vice versa
    M[8][col] = M[2][col]
    M[2][col] = aux
    #troca a linha 5 pela 9 e vice versa
    M[9][col] = M[5][col]
    M[5][col] = aux_2
print()
print(f"Linhas 8 e 2 trocadas, e linha 9 e 5 trocadas: ")
for lista in M:
    for elemento in lista:
        print(elemento, end=' ')
    print()
