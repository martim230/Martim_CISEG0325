nome = input("Digite o nome do cliente: ")
valor_compra = float(input("Digite o valor da compra: "))
if valor_compra <= 200.00:
    percentual_desconto = 10
elif valor_compra <= 500.00:
    percentual_desconto = 15
else:
    percentual_desconto = 20
valor_desconto = (percentual_desconto / 100) * valor_compra
valor_total = valor_compra - valor_desconto
print(f"Nome do cliente: {nome}")
print(f"Valor da compra: {valor_compra:.2f}€")
print(f"Percentual de desconto: {percentual_desconto}%")
print(f"Valor do desconto: {valor_desconto:.2f}€")
print(f"Valor total a pagar: {valor_total:.2f}€")