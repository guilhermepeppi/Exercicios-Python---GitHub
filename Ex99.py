# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada
# informação no seu respectivo vetor. Imprima a idade e a altura na ordem
# inversa a ordem lida.

idades = []
alturas = []

for i in range(5):
    while True:
        try:
            idade = int(input(f'{i+1}º - Sua idade: '))
            altura = float(input(f'{i+1}º - Sua altura: '))
            idades.append(idade)
            alturas.append(altura)
            break
        except ValueError:
            print('\033[31mERRO! Digite um número inteiro.\033[m')

print("-" * 20)
print("Dados na ordem original:")

print(f'Idades original: {idades}')
print(f'Alturas original: {alturas}')

print("-" * 20)
print("Dados na ordem inversa:")

# Método reversed() para obter uma visualização reversa da lista sem modificar a lista original.
vetor_idades_reverso = list(reversed(idades))
vetor_alturas_reverso = list(reversed(alturas))

print(f'Idades reverso: {vetor_idades_reverso}')
print("Alturas reverso:", [format(altura, '.2f')
      for altura in vetor_alturas_reverso])
