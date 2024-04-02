# Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
# Dica: utilize o operador módulo (resto da divisão).

numero = int(input("Digite um número inteiro: "))  # Solicita ao usuário um número inteiro e converte para um número inteiro.

if numero % 2 == 0:  # Verifica se o número é par.
    print(f"O número {numero} é par.")  # Se for par, exibe a mensagem informando que o número é par.
else:
    print(f"O número {numero} é ímpar.")
