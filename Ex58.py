# Faça um programa que peça dois números, base e expoente, calcule e mostre o
# primeiro número elevado ao segundo número. Não utilize a função de potência da
# linguagem.

base = int(input('Digite a base: '))
expoente = int(input('Digite o expoente: '))
resultado = base ** expoente
print(f'{base} elevado a {expoente} é igual a {resultado}')
