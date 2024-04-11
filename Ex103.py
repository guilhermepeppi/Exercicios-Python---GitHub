# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que
# determine quantos alunos com mais de 13 anos possuem altura inferior à média
# de altura desses alunos.

idades = []
alturas = []
media = 0
total_alunos_maior_idade = 0

for i in range(5):
    while True:
        try:
            idade = int(input(f'{i+1}º Aluno - idade: '))
            altura = float(input(f'{i+1}º Aluno - altura: '))
            idades.append(idade)
            alturas.append(altura)
            break
        except ValueError:
            print('\033[31mERRO! Digite um valor válido.\033[m')


media = sum(alturas) / len(alturas)
print(f'Média de altura {media:.2f}')

for i in range(len(idades)):
    if idades[i] > 13 and alturas[i] < media:
        total_alunos_maior_idade += 1

print(f'Quantidade de alunos com mais de 13 anos possuem altura inferior à média: {
      total_alunos_maior_idade}')
