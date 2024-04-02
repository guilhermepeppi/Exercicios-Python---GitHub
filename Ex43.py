# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool: até 20 litros, desconto de 3% por litro acima de 20 litros, desconto de 5% por litro
# Gasolina: até 20 litros, desconto de 4% por litro acima de 20 litros, desconto de 6% por litro

# Escreva um algoritmo que leia o número de litros vendidos,
# o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
# calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50
# o preço do litro do álcool é R$ 1,90.

litros = float(input("Digite o número de litros vendidos: "))
combustivel = input("Digite o tipo de combustível (A-álcool, G-gasolina): ").upper()

if combustivel == "A":
    preco = 1.9
    if litros <= 20:
        desconto = 0.03
    else:
        desconto = 0.05
else:
    preco = 2.5
    if litros <= 20:
        desconto = 0.04
    else:
        desconto = 0.06

valor = litros * preco * (1 - desconto)
print(f"O valor a ser pago pelo cliente é R$ {valor:.2f}.")
