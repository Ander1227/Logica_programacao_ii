M = []
lin = 5
col = 5
for i in range(lin):
    L = []
    for j in range(col):
        L.append(int(input(f"Digite um valor inteiro p M[{i}][{j}]: ")))
    M.append(L)

soma = 0
print("Somatório dos itens da linha 4: ")
for i in range(lin):
    for j in range(col):
        if i == 4:
            soma += M[i][j]
print(soma)
