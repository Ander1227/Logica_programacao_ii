#multiplicação do primeiro elemento do vetor,
# por toda a primeira linha da matriz,
# do segundo item do vetor por toda a segunda linha da matriz
# e assim sucessivamente.

V = []
M = []
Resultado = []
for i in range(5): #preenche a lista
    V.append(int(input("Digite um valor inteiro: ")))

for i in range(5): #matriz
    L = []
    L2 = []
    for j in range(5):
        L.append(int(input(f"Digite um valor inteiro para Matriz M[{i}][{j}]: ")))
        L2.append(0)
    M.append(L)
    Resultado.append(L2)  # preeche a matriz resultado com zeros


for linha in range(len(M)):
    temporaria = V[linha] #salva o indice[i] da lista
    for coluna in range(len(M)):
        valor_matriz = M[linha][coluna] * temporaria #multiplica a linha toda pelo indice[i] da lista
        Resultado[linha][coluna] = valor_matriz #substitui na matriz resultado

print()

print(30 * "-")
for lista in Resultado:
    for elemento in lista:
        print(elemento, end=" ")
    print()
print(30 * "-")
