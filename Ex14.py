# João Papo-de-Pescador, homem de bem,
# comprou um microcomputador para controlar o rendimento diário de seu trabalho.

# Toda vez que ele traz um peso de peixes maior que o estabelecido
# pelo regulamento de pesca do estado de São Paulo (50 quilos)
# deve pagar uma multa de R$ 4,00 por quilo excedente.

# João precisa que você faça um programa que
# leia a variável peso (peso de peixes) e calcule o excesso.

# Gravar na variável excesso a quantidade de quilos além do limite
# e na variável multa o valor da multa que João deverá pagar.
# Imprima os dados do programa com as mensagens adequadas.

peso_peixes = float(input('Digite o peso dos peixes: '))
excesso = peso_peixes - 50
multa = excesso * 4
print(f'O peso dos peixes excedeu o limite em {excesso:.2f}kg.')
print(f'O valor da multa a ser paga é de R${multa:.2f}.')
