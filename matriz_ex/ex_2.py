#lista preenchida pelas colunas
M = []
col = 5
linha = 5
L = []
for i in range(col * linha):
    L.append(int(input(f"Digite um valor inteiro p M: ")))

for j in range(linha):
    temporaria = []
    for k in range(col):
        #multiplica a linha pela coluna para pular p proxima coluna
        #soma o j p mover p baixo
        posicao_L = L[(k * linha) + j]
        temporaria.append(posicao_L)
    M.append(temporaria)


for lista in M:
    for elemento in lista:
        print(elemento, end=' ')
    print()
