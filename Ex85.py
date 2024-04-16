# Em uma eleição presidencial existem quatro candidatos. Os votos são informados
# por meio de código. Os códigos utilizados são: 1, 2, 3, 4 - Votos para os
# respectivos candidatos (você deve montar a tabela ex: 1 - Jose/ 2- João/etc) 5
# - Voto Nulo 6 - Voto em Branco

# Faça um programa que calcule e mostre:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# A percentagem de votos nulos sobre o total de votos;
# A percentagem de votos em branco sobre o total devotos.

# Para finalizar o conjunto de votos tem-se o valor zero.

candidatos = {
    1: ('José', 0),
    2: ('João', 0),
    3: ('Maria', 0),
    4: ('Ana', 0),
    5: ('Nulo', 0),
    6: ('Branco', 0)
}

total_votos = 0
total_nulos = 0
total_brancos = 0

while True:
    try:
        candidato = int(input('Número do candidato (ou 0 para encerrar): '))
        if candidato == 0:
            break
        elif candidato in candidatos:
            candidatos[candidato] = (
                candidatos[candidato][0], candidatos[candidato][1] + 1)
            total_votos += 1
        elif candidato == 5:
            total_nulos += 1
            total_votos += 1
        elif candidato == 6:
            total_brancos += 1
            total_votos += 1
        else:
            print('\033[31mERRO! Candidato inválido.\033[m')
    except ValueError:
        print('\033[31mERRO! Digite um valor válido.\033[m')

percentual_nulos = (total_nulos / total_votos) * 100 if total_votos > 0 else 0
percentual_brancos = (total_brancos / total_votos) * \
    100 if total_votos > 0 else 0

print('Total de votos para cada candidato:')
for candidato in candidatos:
    print(f'{candidatos[candidato][0]}: {candidatos[candidato][1]} votos')
print(f'Total de votos nulos: {total_nulos}')
print(f'Total de votos em branco: {total_brancos}')
print(f'Percentual de votos nulos: {percentual_nulos:.2f}%')
print(f'Percentual de votos em branco: {percentual_brancos:.2f}%')
