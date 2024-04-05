# Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
# Depois modifique o programa para que ele mostre os números um ao lado do
# outro.

for numero in range(1, 20+1):
    print(numero)

for numero in range(1, 20+1):
    if numero < 20:
        print(numero, end=', ')
    else:
        print(numero, end='')
