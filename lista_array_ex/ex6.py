modelo_carros = []
consumo_carros = []
consumo_1000 = []
mais_economico = ''
carro_economico = ''
for i in range(5):
    modelo_carros.append(input("Qual o modelo do carro? "))
    consumo_carros.append(float(input("Qual o consumo do carro(KM p/ Litro)? ")))
    consumo_1000.append(1000 / consumo_carros[i])
for i in range(len(consumo_carros)):
    if i == 0:
        mais_economico = consumo_carros[i]
        carro_economico = modelo_carros[i]
    if consumo_carros[i] > mais_economico:
        mais_economico = consumo_carros[i]
        carro_economico = modelo_carros[i]
print(f"O carro mais econõmico é o {carro_economico}. Ele faz {mais_economico} KM por Litros ")
for i in range(len(consumo_1000)):
    print(f"O consumo do carro {modelo_carros[i]} para 1000 km é de: {consumo_1000[i]:.2f} Litros.")

