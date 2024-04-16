# Uma grande emissora de televisão quer fazer uma enquete entre os seus
# telespectadores para saber qual o melhor jogador após cada jogo. Para isto,
# faz-se necessário o desenvolvimento de um programa, que será utilizado pelas
# telefonistas, para a computação dos votos. Sua equipe foi contratada para
# desenvolver este programa. Para computar cada voto, a telefonista digitará um
# número, entre 1 e 23, correspondente ao número da camisa do jogador. Um número
# de jogador igual zero, indica que a votação foi encerrada. Se um número
# inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem
# de aviso, e voltando a pedir outro número. Após o final da votação, o programa
# deverá exibir: O total de votos computados; Os númeos e respectivos votos de
# todos os jogadores que receberam votos; O percentual de votos de cada um
# destes jogadores; O número do jogador escolhido como o melhor jogador da
# partida, juntamente com o número de votos e o percentual de votos dados a ele.
# Observe que os votos inválidos e o zero final não devem ser computados como
# votos. O resultado aparece ordenado pelo número do jogador. O programa deve
# fazer uso de arrays. O programa deverá executar o cálculo do percentual de
# cada jogador através de uma função. Esta função receberá dois parâmetros: o
# número de votos de um jogador e o total de votos. A função calculará o
# percentual e retornará o valor calculado.

# Exemplo: Enquete: Quem foi o melhor jogador?

# Número do jogador (0=fim): 9 Número do jogador (0=fim): 10 Número do jogador (0=fim): 9 Número do jogador (0=fim): 10 Número do jogador (0=fim): 11 Número do jogador (0=fim): 10 Número do jogador (0=fim): 50 Informe um valor entre 1 e 23 ou 0 para sair! Número do jogador (0=fim): 9 Número do jogador (0=fim): 9 Número do jogador (0=fim): 0

# Resultado da votação:

# Foram computados 8 votos.

# Jogador Votos % 9 4 50,0% 10 3 37,5% 11 1 12,5% O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.

jogadores = [0] * 23
total_votos = 0

while True:
    try:
        numero_jogador = int(input('Número do jogador (0=fim): '))

        if numero_jogador == 0:
            break

        if 1 <= numero_jogador <= 23:
            jogadores[numero_jogador - 1] += 1
            total_votos += 1
        else:
            print('Informe um valor entre 1 e 23 ou 0 para sair!')
    except ValueError:
        print('Informe um valor válido!')

melhor_jogador = 0
votos_melhor_jogador = 0

print('\nResultado da votação:\n')
print(f'Foram computados {total_votos} votos.\n')
print('Jogador  Votos  %')
for i, votos in enumerate(jogadores):
    if votos > 0:
        percentual = (votos / total_votos) * 100
        print(f'{i+1: <9} {votos: <7} {percentual: .1f}%')
        if votos > votos_melhor_jogador:
            melhor_jogador = i + 1
            votos_melhor_jogador = votos

print(f'\nO melhor jogador foi o número {melhor_jogador}, com {votos_melhor_jogador} votos, correspondendo a \
      {(votos_melhor_jogador / total_votos) * 100:.1f}% do total de votos.')
