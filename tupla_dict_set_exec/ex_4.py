'''
#jeito gambiarra
X = []
primos = []
for i in range(9):
    n = int(input("Digite um numero: "))
    X.append(n)
    if n > 1:
        if (n % 2 != 0 and n % 3 != 0 and n % 5 != 0 and n % 7 != 0
                and n % 13 != 0 and n % 17 != 0 and n % 11 != 0 or (n == 2) or (n == 3) or
                (n == 5) or (n == 7) or (n == 13) or (n ==11) or (n == 17)):
            primos.append(n)
            print(f"Primo na posição: {i}")
print(X)
print(f"Números primos: {primos}")
'''
#ou
L = []
primos = []
for i in range(9):
    t = int(input("Digite um numero: "))
    L.append(t)
    primo = True
    if t > 1:
        for j in range(2,  t):#vai testar até o tamanho do número
            if t % j == 0: #se for divisivel não é primo
                primo = False
                break
        if primo:
            primos.append(t)
            print(f"Primo {t} na posição: {i}")
print(L)
print(primos)



