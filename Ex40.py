# Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
# Dica: utilize uma função de arredondamento.

numero = float(input("Digite um número: "))  # Solicita ao usuário um número e converte para um número real.

if numero == round(numero):  # Verifica se o número é igual ao seu arredondamento.
    print(f"O número {numero} é inteiro.")  # Se for igual, exibe a mensagem informando que o número é inteiro.
else:
    print(f"O número {numero} é decimal.")
