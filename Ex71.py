# Faça um programa que calcule o número médio de alunos por turma. Para isto,
# peça a quantidade de turmas e a quantidade de alunos para cada turma. As
# turmas não podem ter mais de 40 alunos.

total_alunos = 0
media = 0

while True:
    try:
        total_turmas = int(input("Número total de turmas: "))
        break
    except ValueError:
        print("\033[31mErro! Digite um número.\033[m")

for i in range(1, total_turmas+1):
    while True:
        try:
            qtde_alunos = int(input(f"Número total de alunos da {i}ª: "))
            if qtde_alunos > 40:
                print('Número não pode exceder 40 alunos')
            else:
                total_alunos += qtde_alunos
                break
        except ValueError:
            print("\033[31mErro! Digite um número.\033[m")

media = total_alunos / total_turmas

print(f'Média de alunos: {media:.2f}')
