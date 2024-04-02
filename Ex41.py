# Faça um Programa que leia 2 números e em seguida
# pergunte ao usuário qual operação ele deseja realizar.

# O resultado da operação deve ser acompanhado de uma frase
# que diga se o número é: par ou ímpar; positivo ou negativo; inteiro ou decimal.

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação desejada (+, -, *, /): ")

if operacao == "+":
    resultado = numero1 + numero2
    print(f"O resultado da soma é {resultado}")
elif operacao == "-":
    resultado = numero1 - numero2
    print(f"O resultado da subtração é {resultado}")
elif operacao == "*":
    resultado = numero1 * numero2
    print(f"O resultado da multiplicação é {resultado}")
elif operacao == "/":
    resultado = numero1 / numero2
    print(f"O resultado da divisão é {resultado}")
else:
    print("Operação inválida")

if resultado % 2 == 0:
    print("O resultado é par.")
else:
    print("O resultado é ímpar.")

if resultado >= 0:
    print("O resultado é positivo.")
else:
    print("O resultado é negativo.")

if resultado == int(resultado):
    print("O resultado é inteiro.")
else:
    print("O resultado é decimal.")
