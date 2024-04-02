# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = str(input("Digite o nome: "))

while len(nome) <= 3:
    print("Erro: o nome deve ter mais de 3 caracteres.")
    nome = str(input("Digite o nome: "))
idade = int(input("Digite a idade: "))

while idade < 0 or idade > 150:
    print("Erro: a idade deve estar entre 0 e 150.")
    idade = int(input("Digite a idade: "))
salario = float(input("Digite o salário: "))

while salario <= 0:
    print("Erro: o salário deve ser maior que zero.")
    salario = float(input("Digite o salário: "))
sexo = str(input("Digite o sexo (f ou m): "))

while sexo != 'f' and sexo != 'm':
    print("Erro: o sexo deve ser 'f' ou 'm'.")
    sexo = str(input("Digite o sexo (f ou m): "))
estado_civil = str(input("Digite o estado civil (s, c, v ou d): "))

while estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
    print("Erro: o estado civil deve ser 's', 'c', 'v' ou 'd'.")
    estado_civil = str(input("Digite o estado civil (s, c, v ou d): "))

print("Informações cadastradas com sucesso.")

print("Nome:", nome)
print("Idade:", idade)
print("Salário: R$", salario)
print("Sexo:", sexo)
print("Estado civil:", estado_civil)
