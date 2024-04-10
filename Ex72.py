# Faça um programa que calcule o valor total investido por um colecionador em
# sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá
# informar a quantidade de CDs e o valor para em cada um.

qtde_cds = 0
valor_total = 0
media = 0

while True:
    try:
        qtde_cds = int(input("Número de CDs: "))
        break
    except ValueError:
        print("\033[31mErro! Digite um número.\033[m")

for i in range(1, qtde_cds+1):
    while True:
        try:
            valor_cd = int(input(f"Valor do {i}º CD: "))
            valor_total += valor_cd
            break
        except ValueError:
            print("\033[31mErro! Digite um número.\033[m")

valor_medio = valor_total / qtde_cds

print(f'Total gasto: {valor_total:.2f}')
print(f'Valor médio gasto: {valor_medio:.2f}')
