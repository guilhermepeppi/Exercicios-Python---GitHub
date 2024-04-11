# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
# -----
# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro
# vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos
# intercalados dos dois outros vetores.


vetor1 = [0] * 5
vetor2 = [0] * 5
vetor3 = [0] * 5
vetor_final = []

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

print('-' * 20)
print('TERCEIRO VETOR')
for k in range(len(vetor3)):
    numero = int(input(f'Digite o {k + 1}º número: '))
    vetor3[k] = numero

for a in range(5):
    vetor_final.append(vetor1[a])
    vetor_final.append(vetor2[a])
    vetor_final.append(vetor3[a])


print('-' * 20)
print('TERCEIRO VETOR')
print(vetor_final)
