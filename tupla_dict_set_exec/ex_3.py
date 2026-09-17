#trocando ordem indices par/impar
K = []
for i in range(3):
    num = int(input("Digite um numero: "))
    if i % 2 == 0:
        K.append(num)
        i += 1
    else:
        i -= 1
        K.append(num)
print(K)
