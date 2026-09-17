R = set()
S = set()
gabarito = set()
cont = 0
cont_palpite = 0
cont_pontos = 0
while cont != 5:
    sorteio = int(input("Digite um número do sorteio: "))
    if sorteio not in R:
        R.add(sorteio)
        cont += 1
    else:
        print("Não podem haver numeros repetidos!")

while cont_palpite != 10:
    palpite = int(input("Digite seu palpite: "))
    if palpite not in S:
        S.add(palpite)
        cont_palpite += 1
    else:
        print("Não podem haver numeros repetidos!")
for item in R:
    if item in S:
        cont_pontos += 1
        gabarito.add(item)

print(S)
print(R)
print(f"Quantidade de pontos: {cont_pontos}, {gabarito}")
