# Faça um programa que receba a temperatura média de cada mês do ano e
# armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e
# mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram
# (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

temperaturas = []

meses = [
    "Janeiro", "Fevereiro", "Março", "Abril",
    "Maio", "Junho", "Julho", "Agosto",
    "Setembro", "Outubro", "Novembro", "Dezembro"
]

for i in range(12):
    while True:
        try:
            temperatura = float(input(f'Temperatura média de {meses[i]}: '))
            temperaturas.append(temperatura)
            break
        except ZeroDivisionError:
            print("Erro: Nenhuma temperatura foi informada.")
            exit()
        except ValueError:
            print('\033[31mERRO! Digite um valor válido.\033[m')


media = 0

print('-' * 30)
print('MÉDIA ANUAL')
media = sum(temperaturas) / len(temperaturas)
print(f'Média anual de temperatura: {media:.2f}')

print('-' * 30)
print('MESES COM A TEMPERATURA ACIMA DA MÉDIA ANUAL')

for j in range(12):
    if temperaturas[j] > media:
        print(f'{meses[j]} - {temperaturas[j]}')
