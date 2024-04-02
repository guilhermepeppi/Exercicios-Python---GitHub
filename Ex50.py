# Altere o programa anterior permitindo ao usuário informar
# as populações e as taxas de crescimento iniciais.
# Valide a entrada e permita repetir a operação.

from math import ceil

while True:
    try:
        populacao_a = int(input("Informe a população do país A: "))
        populacao_b = int(input("Informe a população do país B: "))
        taxa_a = float(input("Informe a taxa de crescimento do país A: "))
        taxa_b = float(input("Informe a taxa de crescimento do país B: "))
        anos = 0
        if populacao_a < 0 or populacao_b < 0 or taxa_a < 0 or taxa_b < 0:
            raise ValueError
        break
    except ValueError:
        print("Informe valores válidos.")

while populacao_a < populacao_b:
    populacao_a += populacao_a * taxa_a / 100
    populacao_b += populacao_b * taxa_b / 100
    anos += 1

print("Serão necessários", anos, "anos para que a população de A ultrapasse a população de B.")
print(f"População de A: {ceil(populacao_a):.0f}")
print(f"População de B: {ceil(populacao_b):.0f}")
print(f"Diferença populacional: {ceil(populacao_a - populacao_b):.0f}")
