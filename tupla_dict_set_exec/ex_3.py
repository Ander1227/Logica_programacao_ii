#trocando ordem indices par/impar
K = []
for i in range(4):
    num = int(input("Digite um numero: "))
    K.append(num)
for i in range(0, len(K), 2): #va de 2 em 2 p pegar valores pares
    K[i], K[i+1] = K[i + 1], K[i] #inverte o indice atual
print(K)
