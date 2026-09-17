import random
print("LOTOFÁCIL")
print("Digite um número inteiro pare seu palpite (1-100):")
print("-São 10 números-")
R = []
A = []
cont_pontos = 0
for i in range(5):
    R.append(random.randint(1,100))
for i in range(10):
    A.append(int(input(">> ")))
for numero in A:
    if numero in R:
        cont_pontos += 1
print(f"Sua cartela: {A}")
print(f"Você fez {cont_pontos} ponto(s), cartela: {R}")