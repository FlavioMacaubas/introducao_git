# Aplicativo - Calculadora de IMC

nome = input("Informe seu nome: \n")
peso = float( input("Informe seu peso: \n").replace(',','.') )
altura = float( input("Informe sua altura: \n").replace(',','.') )

# Calcular IMC
imc = peso / altura**2

if imc < 18.5:
    situacao = 'abaixo do peso'
elif imc < 25:
    situacao = 'peso normal'
elif imc < 30:
    situacao = 'sobrepeso'
elif imc < 35:
    situacao = 'obesidade grau 1'
elif imc < 40:
    situacao = 'obesidade grau 2'
else:
    situacao = 'obesidade grau 3 ou mórbida'

print(f"Sua altura é de {altura:.2f} e peso de {peso:.2f}, seu IMC é de {imc:.2f} classificada como {situacao}.")