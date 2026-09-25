#mostra os valores da diagonal principal
""" exemplo:
1
    0
        1
"""
M = []
lin = 5
col = 5
for i in range(lin):
    L = []
    for j in range(col):
        L.append(int(input(f"Digite um valor inteiro p M[{i}][{j}]: ")))
    M.append(L)

print("Valores da diagonal principal: ")
for i in range(lin):
    for j in range(col):
        if i == j:
            print(M[i][j], end=' ')

