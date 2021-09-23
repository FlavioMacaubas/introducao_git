# Programa para caixa de supermercado

# Lista de despesas
items = []

while True:
    price = input("Informe o preço do produto ou digite q para encerrar: ")

    if price.lower().strip() == 'q':
        print('Obrigado')
        break

    qtd = input("informe a quantidade para sair ou digite q para encerrar: ")

    if qtd.lower().strip() == 'q':
        print('Obrigado')
        break

    value = float(price)*float(qtd)
    items.append(value)


if len(items) > 0: 
    print(f'Valor da compra (R$): {sum(items):.2f}')  
    cash = float(input("Informe o valor pago: "))
    print(f"O troco é de: {(cash - sum(items) ):.2f}")
else:
    print('Obrigado')


