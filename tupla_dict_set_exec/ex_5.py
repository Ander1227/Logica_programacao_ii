x = set()
y = set()
for i in range(3):
    x.add(int(input("Digite um número inteiro: ")))
    y.add(int(input("Digite outro número inteiro: ")))
diferenca = x - y
print(diferenca)