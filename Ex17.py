"""
Este programa calcula a quantidade de tinta e os preços necessários para pintar uma área específica.
Ele considera que a cobertura da tinta é de 1 litro para cada 6 metros quadrados.
A tinta é vendida em latas de 18 litros por R$ 80,00 ou em galões de 3,6 litros por R$ 25,00.
O programa informa ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
1. Comprar apenas latas de 18 litros;
2. Comprar apenas galões de 3,6 litros;
3. Misturar latas e galões, de forma que o preço seja o menor.
O programa também acrescenta 10% de folga e sempre arredonda os valores para cima, considerando latas cheias.
"""

import math

# Solicitar a entrada da área em metros quadrados ao usuário
area = float(input("Digite a área a ser pintada em metros quadrados: "))

rendimento_tinta = 6  # Definindo o rendimento da tinta em metros quadrados por litro

quantidade_tinta = area / rendimento_tinta  # Calculando a quantidade de tinta necessária

quantidade_tinta *= 1.1  # Adicionando 10% de folga

latas_18_litros = math.ceil(quantidade_tinta / 18)  # Calculando o número de latas de 18 litros necessárias

preco_latas_18_litros = latas_18_litros * 80  # Calculando o preço das latas de 18 litros

galoes_3_6_litros = math.ceil(quantidade_tinta / 3.6)  # Calculando o número de galões de 3,6 litros necessários

preco_galoes_3_6_litros = galoes_3_6_litros * 25  # Calculando o preço dos galões de 3,6 litros


# Calculando a mistura de latas e galões
latas_para_mistura = int(quantidade_tinta // 18)
resto = quantidade_tinta % 18
galoes_para_mistura = math.ceil(resto / 3.6)

# Calculando o preço da mistura de latas e galões
preco_mistura = (latas_para_mistura * 80) + (galoes_para_mistura * 25)

# Imprimindo os resultados
print("1. Comprar apenas latas de 18 litros:")
print("Quantidade de latas:", latas_18_litros)
print("Preço:", preco_latas_18_litros)

print("\n2. Comprar apenas galões de 3,6 litros:")
print("Quantidade de galões:", galoes_3_6_litros)
print("Preço:", preco_galoes_3_6_litros)

print("\n3. Misturar latas e galões:")
print("Latas:", latas_para_mistura)
print("Galões:", galoes_para_mistura)
print("Preço:", preco_mistura)
