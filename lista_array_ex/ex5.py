import random
X = []
Y = []
intercalacao = []
for i in range(10):
    X.append(random.randint(1,100))
    Y.append(random.randint(1,100))
for i in range(len(X)):
    intercalacao.append(X[i])
    intercalacao.append(Y[i])
print(f"Vetor X: {X}")
print(f"Vetor Y: {Y}")
print(f"Intercalao X, Y: {intercalacao}")
