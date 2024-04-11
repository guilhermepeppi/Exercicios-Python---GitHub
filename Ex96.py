# Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
# Imprima os três vetores.

from random import randint

vetor = [0] * 20
vetor_pares = []
vetor_impares = []

for i in range(len(vetor)):
    vetor[i] = randint(1, 100)
    if vetor[i] % 2 == 0:
        vetor_pares.append(vetor[i])
    else:
        vetor_impares.append(vetor[i])

print(f'Vetor: {vetor}')
print(f'Vetor pares: {vetor_pares}')
print(f'Vetor impares: {vetor_impares}')
