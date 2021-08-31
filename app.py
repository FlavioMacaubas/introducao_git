# Aplicativo - Calculadora de IMC

nome = input("Informe seu nome: \n")
peso = float( input("Informe seu peso: \n").replace(',','.') )
altura = float( input("Informe sua altura: \n").replace(',','.') )

# Calcular IMC
imc = peso / altura**2

print(f"Olá {nome}, seu peso é de {peso}kg e altura de {altura}m, com IMC de {imc:.2f}.")