from asyncio.tools import build_async_tree

R = []
S = []
X = []
for i in range(5):
    R.append(int(input("Digite um numero inteiro para R: ")))
for i in range(10):
    S.append(int(input("Digite um numero inteiro S: ")))
for i in range(0, 5):
    for j in range(0, 10):
        if R[i] == S[j]: #compara se os valores são iguais
            X.append(R[i])
            break #quando encontrar ele para o loop de verificação
#OU
# for item in R:
#     if item in S:
#         if not item in X: #verifica se não tem o item em x
#             X.append(item)
print(f"O conjunto de números presentes em R e S são: {X}")

