import random
X = []
Y = []
DIFERENCA = []
for i in range(3):
    X.append(float(input("Digite um numero real para X: ")))
    Y.append(float(input("Digite um numero real para Y: ")))
print(f"Vetor X: {X}\nVetor Y: {Y}")
for numero in X:
    if numero not in Y:
        if numero not in DIFERENCA:
            DIFERENCA.append(numero)
print(f"A difereça entre o vetor X e Y é: {DIFERENCA}")