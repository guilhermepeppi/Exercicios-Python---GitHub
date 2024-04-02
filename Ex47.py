# Faça um programa que leia um nome de usuário e a sua senha
# e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

usuario = str(input("Digite o nome de usuário: "))
senha = str(input("Digite a senha: "))
while usuario == senha:
    print("Erro: a senha não pode ser igual ao nome de usuário.")
    usuario = str(input("Digite o nome de usuário: "))
    senha = str(input("Digite a senha: "))
print("Usuário e senha cadastrados com sucesso.")
