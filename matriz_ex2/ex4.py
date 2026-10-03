tam_matriz = 5
M = []
SL = []
SC = []
for i in range(tam_matriz):
    L = []
    for j in range(tam_matriz):
        L.append(int(input(f"Digite um valor para matriz M[{i}][{j}]: ")))
    M.append(L)

for i in range(len(M)):
    soma_lin = 0
    for j in range(len(M)):
        soma_lin += M[i][j]#soma pela linha
    SL.append(soma_lin)

#esse for anda pelas colunas
for j in range(len(M)):
    soma_col = 0
    for k in range(len(M)):
        soma_col += M[k][j]#soma pela coluna
    SC.append(soma_col)

for lista in M:
    for elemento in lista:
        print(elemento, end=' ')
    print()

print(SL)
print(SC)
