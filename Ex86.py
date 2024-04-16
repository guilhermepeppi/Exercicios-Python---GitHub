# Desenvolver um programa para verificar a nota do aluno em uma prova com 10
# questões, o programa deve perguntar ao aluno a resposta de cada questão e ao
# final comparar com o gabarito da prova e assim calcular o total de acertos e a
# nota (atribuir 1 ponto por resposta certa).

# Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno
# vai utilizar o sistema.

# Após todos os alunos terem respondido informar: Maior e Menor Acerto; Total de
# Alunos que utilizaram o sistema; A Média das Notas da Turma. Gabarito da
# Prova: 01 - A 02 - B 03 - C 04 - D 05 - E 06 - E 07 - D 08 - C 09 - B 10 - A

# Após concluir isto você poderia incrementar o programa permitindo que o
# professor digite o gabarito da prova antes dos alunos usarem o programa.

# Inicialização das variáveis
alunos = []
gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']

# Loop para processar respostas dos alunos
while True:
    respostas_aluno = []
    for i in range(1, 11):
        resposta = input(f"Resposta da questão {i}: ").upper()
        respostas_aluno.append(resposta)

    nota_aluno = 0
    for i in range(10):
        if respostas_aluno[i] == gabarito[i]:
            nota_aluno += 1

    alunos.append(nota_aluno)

    continuar = input("Outro aluno vai utilizar o sistema? (s/n): ").lower()
    if continuar != 's':
        break

# Imprimir estatísticas da turma
maior_acerto = max(alunos)
menor_acerto = min(alunos)
total_alunos = len(alunos)
media_notas = sum(alunos) / total_alunos

print(f"\nMaior acerto: {maior_acerto}")
print(f"Menor acerto: {menor_acerto}")
print(f"Total de alunos: {total_alunos}")
print(f"Média das notas: {media_notas:.2f}")
