# Numa eleição existem três candidatos. Faça um programa que peça o número total
# de eleitores. Peça para cada eleitor votar e ao final mostrar o número de
# votos de cada candidato.

votos_candidatos = {1: 0, 2: 0, 3: 0}

while True:
    try:
        total_eleitores = int(input("Número total de eleitores: "))
        break
    except ValueError:
        print("\033[31mErro! Digite um número.\033[m")

for eleitor in range(1, total_eleitores+1):
    print(f'Voto {eleitor}º eleitor: ')
    voto = int(input("Digite o número do candidato (1, 2 ou 3): "))

    # Verifica se o voto é válido e atualiza o contador de votos
    if voto in votos_candidatos:
        votos_candidatos[voto] += 1
    else:
        print("Opção inválida. Voto descartado.")

# Exibe o resultado final
print("\nResultado da eleição:")
for candidato, votos in votos_candidatos.items():
    print(f"Candidato {candidato}: {votos} votos")
