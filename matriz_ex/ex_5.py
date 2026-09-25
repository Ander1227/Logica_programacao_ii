M = []
lin = 10
col = 10
for i in range(lin):
    L = []
    for j in range(col):
        L.append(int(input(f"Digite um valor inteiro p M[{i}][{j}]: ")))
    M.append(L)

soma = 0
soma_dp = 0
for i in range(lin):
    for j in range(col):
        if i == 2:
            soma += M[i][j]
        if i == j:
            soma_dp += M[i][j]
print(f"Somatório dos itens da linha 2: {soma}")
print(f"Somatório dos valores da diagonal principal: {soma_dp} ")


