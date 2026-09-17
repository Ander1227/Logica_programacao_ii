R = set()
S = set()
X = set()
for i in range(3):
    R.add(float(input("Digite um numero real para X: ")))
for i in range(6):
    S.add(float(input("Digite um numero real para S: ")))

X = R & S
print(f"Os termos comuns  entre o conjunto R e S é: {X}")