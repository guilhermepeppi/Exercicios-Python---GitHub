# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num
# vetor a média de cada aluno, imprima o número de alunos com média maior ou
# igual a 7.0.

medias_alunos = []

# Loop para iterar sobre cada aluno
for i in range(10):
    # Solicitar as notas ao usuário
    print(f"Informe as notas do aluno {i + 1}:")
    notas = []
    for j in range(4):
        nota = float(input(f"Nota {j + 1}: "))
        notas.append(nota)

    # Calcular a média do aluno e adicioná-la à lista de médias dos alunos
    media = sum(notas) / len(notas)
    medias_alunos.append(media)

# Contar o número de alunos com média maior ou igual a 7.0
alunos_aprovados = sum(1 for media in medias_alunos if media >= 7.0)

# Imprimir o número de alunos aprovados
print(f"Número de alunos com média maior ou igual a 7.0: {alunos_aprovados}")
