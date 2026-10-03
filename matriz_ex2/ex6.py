#multiplicação do primeiro elemento do vetor,
# por toda a primeira linha da matriz,
# do segundo item do vetor por toda a segunda linha da matriz
# e assim sucessivamente.

V = []
M = []
Resultado = []
for i in range(3): #preenche a lista
    V.append(int(input("Digite um valor inteiro: ")))

for i in range(3): #matriz
    L = []
    for j in range(3):
        L.append(int(input(f"Digite um valor inteiro para Matriz M[{i}][{j}]: ")))
        Resultado.append(0) #preecnhe a matriz resultado com zeros
    M.append(L)


for linha in range(len(M)):
    for coluna in range(len(M)):
        multiplica_liha = M[linha][coluna] * V[coluna]
        Resultado[linha][coluna].append(multiplica_liha)

print(Resultado)

