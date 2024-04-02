# Uma fruteira está vendendo frutas com a seguinte tabela de preços:

# Até 5 Kg:
# Morango R$2,50/kg - Maçã R$ 1,80/kg
# Acima de 5 Kg
# Morango R$2,20/kg - R$1,50/kg

# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
# receberá ainda um desconto de 10% sobre este total.

# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas
# e escreva o valor a ser pago pelo cliente.

moran = float(input("Digite a quantidade de morangos em Kg: "))
maca = float(input("Digite a quantidade de maças em Kg: "))
total = moran + maca

if moran <= 5:
    valor_moran = moran * 2.50
else:
    valor_moran = moran * 2.20

if maca <= 5:
    valor_maca = maca * 1.80
else:
    valor_maca = maca * 1.50

valor_total = valor_moran + valor_maca

if total > 8 or valor_total > 25:
    valor_total = valor_total - (valor_total * 0.10)

print(f"O valor total a ser pago é de R${valor_total:.2f}")
