tam_matriz = 4
M = []
SOMA = []
for i in range(tam_matriz):
    L = []
    for j in range(tam_matriz):
        L.append(int(input(f"Digite um valor para matriz M[{i}][{j}]: ")))
    M.append(L)
a = float(input("Digite um valor para multiplicar: "))
soma = 0
for i in range(len(M)):
    for j in range(len(M)):
        soma = M[i][j] * a
        SOMA.append(soma)
print(f"A multiplicação da matriz por {a} é: {SOMA}")