# Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus
# vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por
# cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve
# vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou
# seja, um total de $470. Escreva um programa (usando um array de contadores)
# que determine quantos vendedores receberam salários nos seguintes intervalos
# de valores: $200 - $299 $300 - $399 $400 - $499 $500 - $599 $600 - $699 $700 -
# $799 $800 - $899 $900 - $999 $1000 em diante Desafio: Crie ma fórmula para
# chegar na posição da lista a partir do salário, sem fazer vários ifs
# aninhados.


# Definindo a lista de contadores para cada intervalo de salário
contadores = [0] * 10  # Inicializa todos os contadores com 0

# Lista de salários de exemplo
salarios_exemplo = [200, 250, 300, 400, 500, 600, 700, 800, 900, 1000, 1200]

# Percorrendo os salários e contando quantos vendedores estão em cada intervalo
for salario in salarios_exemplo:
    indice = min(salario // 100, 9)
    contadores[indice] += 1

# Imprimindo os resultados
for i, contador in enumerate(contadores):
    if i < 9:
        print(f"${i*100} - ${i*100 + 99}: {contador} vendedores")
    else:
        print(f"${i*100} em diante: {contador} vendedores")
