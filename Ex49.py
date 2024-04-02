# Supondo que a população de um país A seja da ordem de 80000 habitantes
# com uma taxa anual de crescimento de 3% e que
# a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.

# Faça um programa que calcule e escreva o número de anos necessários
# para que a população do país A ultrapasse ou iguale
# a população do país B, mantidas as taxas de crescimento.

from math import ceil

populacao_a = 80000
populacao_b = 200000
anos = 0

while populacao_a < populacao_b:
    populacao_a += populacao_a * 0.03
    populacao_b += populacao_b * 0.015
    anos += 1

print("Serão necessários", anos, "anos para que a população de A ultrapasse a população de B.")
print(f"População de A: {ceil(populacao_a):.0f}")
print(f"População de B: {ceil(populacao_b):.0f}")
print(f"Diferença populacional: {ceil(populacao_a - populacao_b):.0f}")
