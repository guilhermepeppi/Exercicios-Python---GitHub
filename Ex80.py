# Faça um programa que leia dez conjuntos de dois valores, o primeiro
# representando o número do aluno e o segundo representando a sua altura em
# centímetros.

# Encontre o aluno mais alto e o mais baixo.

# Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com
# suas alturas.

# Inicialize as variáveis para armazenar o número e a altura do aluno mais alto e mais baixo
aluno_mais_alto = 0
altura_aluno_mais_alto = 0
aluno_mais_baixo = 0
altura_aluno_mais_baixo = 0

# Faça um loop para ler os dez conjuntos de valores
for i in range(1, 11):
    numero_aluno = int(input("Digite o número do aluno: "))
    altura_aluno = float(input("Digite a altura do aluno em centímetros: "))

    # Verifique se o aluno atual é o mais alto ou o mais baixo
    if altura_aluno > altura_aluno_mais_alto:
        aluno_mais_alto = numero_aluno
        altura_aluno_mais_alto = altura_aluno
    if altura_aluno < altura_aluno_mais_baixo or altura_aluno_mais_baixo == 0:
        aluno_mais_baixo = numero_aluno
        altura_aluno_mais_baixo = altura_aluno

# Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas
print("Aluno mais alto:")
print("Número:", aluno_mais_alto)
print("Altura:", altura_aluno_mais_alto)

print("Aluno mais baixo:")
print("Número:", aluno_mais_baixo)
print("Altura:", altura_aluno_mais_baixo)
