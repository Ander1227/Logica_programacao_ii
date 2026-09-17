v = []
primos = []
for i in range(9):
    num = int(input("Digite um numero inteiro: "))
    v.append(num)
    if num == 2 or num == 3 or num == 5 or num == 7\
            or num == 13 or num == 17:
        primos.append(num)
        print(f"Primo: {num}, posição: {i}")

    elif num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0 and num % 13 != 0 and num % 17 != 0:
        primos.append(num)
        print(f"Primo: {num}, posição: {i}")
print(f"Lista: {v}")
print(f"Primos: {primos}")