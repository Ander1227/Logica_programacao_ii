N = int(input("Digite o tamnho da matriz quadrada: "))
M = []
for i in range(N):
    L = []
    for j in range(N):
        L.append(int(input(f"Digite um valor para Matriz M:[{i}][{j}]: ")))
    M.append(L)

O = []
for i in range(N):
    L = []
    for j in range(N):
        L.append(int(input(f"Digite um valor para Matriz O:[{i}][{j}]: ")))
    O.append(L)

soma = 0
for i in range(len(M)):
    for j in range(len(M)):
        soma += M[i][j] + O[i][j]
print(M)
print(O)
print(f"A soma das matrizes é: {soma:.2f}")
