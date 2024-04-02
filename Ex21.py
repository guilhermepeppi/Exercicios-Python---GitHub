# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.


letra = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]

if letra == 'M':
    print('M - Masculino')
elif letra == 'F':
    print('F - Feminino')
else:
    print('Sexo Inválido')
