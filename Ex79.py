# Um funcionário de uma empresa recebe aumento salarial anualmente.

# Sabe-se que: Esse funcionário foi contratado em 1995, com salário inicial de
# R$ 1.000,00; Em 1996 recebeu aumento de 1,5% sobre seu salário inicial; A
# partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro
# do percentual do ano anterior.

# Faça um programa que determine o salário atual desse funcionário. Após
# concluir isto, altere o programa permitindo que o usuário digite o salário
# inicial do funcionário.

import datetime

while True:
    try:
        salario_inicial = float(input('Seu salário inicial: '))
        break
    except:
        print('\033[31mERRO! Digite um valor válido.\033[m')

data_inicial = datetime.date(1995, 1, 1)
data_final = datetime.date.today()

# Usando datetime.date.year para extrair somente os anos
ano_inicial = data_inicial.year
ano_final = data_final.year
diferenca_em_anos = ano_final - ano_inicial

salario_final = salario_inicial
porcentagem_aumento = 0.015

for i in range(diferenca_em_anos):  # Começar a partir do segundo ano (1996)
    salario_final += salario_final * porcentagem_aumento
    porcentagem_aumento *= 2  # Dobrar a porcentagem de aumento a cada ano

print(f'Salário final: {salario_final:.2f}')
