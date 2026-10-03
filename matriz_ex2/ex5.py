#determinate
tam_matriz = 2
M = []
multiplica_dp = 1
multiplica_ds = 1

#cria a matriz 2x2
for i in range(tam_matriz):
    L = []
    for j in range(tam_matriz):
        L.append(int(input(f"Insira uma valor para a matriz [{i}][{j}]: ")))
    M.append(L)

#determinante(2x2): Multiplica-se a diagonal principal e
# subtrai-se o produto da diagonal secundária (ad - bc).
for linha in range(len(M)):
    for col in range(len(M)):

        #multiplica os valores da diagonal principal(dp)
        if linha == col:
            multiplica_dp *= M[linha][col]

        #multiplica os valores da diagonal secundária(ds)
#formula ds = i + j = n + 1 , onde n = tamanho da matriz,
# como o indice começa em 0 em python vai n - 1
        if linha + col == len(M) - 1: #a ds é
            multiplica_ds *= M[linha][col]
print(multiplica_dp)
print(multiplica_ds)
determinante = multiplica_dp - multiplica_ds

#printa a matriz
for lista in M:
    for elemento in lista:
        print(elemento, end=' ')
    print()
print(f"O determinante da matriz 2x2 é {determinante}")