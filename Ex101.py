# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro
# vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos
# intercalados dos dois outros vetores.

vetor1 = [0] * 10
vetor2 = [0] * 10
vetor3 = []

print('-' * 20)
print('PRIMEIRO VETOR')
for i in range(len(vetor1)):
    numero = int(input(f'Digite o {i + 1}º número: '))
    vetor1[i] = numero

print('-' * 20)
print('SEGUNDO VETOR')
for j in range(len(vetor2)):
    numero = int(input(f'Digite o {j + 1}º número: '))
    vetor2[j] = numero

for k in range(10):
    vetor3.append(vetor1[k])
    vetor3.append(vetor2[k])

print('-' * 20)
print('TERCEIRO VETOR')
print(vetor3)
