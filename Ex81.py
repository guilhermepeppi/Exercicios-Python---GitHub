# Foi feita uma estatística em cinco cidades brasileiras para coletar dados
# sobre acidentes de trânsito.

# Foram obtidos os seguintes dados: Código da cidade; Número de veículos de
# passeio (em 1999); Número de acidentes de trânsito com vítimas (em 1999).

# Deseja-se saber: Qual o maior e menor índice de acidentes de transito e a que
# cidade pertence; Qual a média de veículos nas cinco cidades juntas; Qual a
# média de acidentes de trânsito nas cidades com menos de 2.000 veículos de
# passeio.

# Dados das cidades
dados_cidades = [
    {"cidade": "Cidade A", "veiculos": 1000, "acidentes": 20},
    {"cidade": "Cidade B", "veiculos": 1500, "acidentes": 15},
    {"cidade": "Cidade C", "veiculos": 1800, "acidentes": 25},
    {"cidade": "Cidade D", "veiculos": 2000, "acidentes": 10},
    {"cidade": "Cidade E", "veiculos": 2500, "acidentes": 30}
]

# Passo 1: Calcular o índice de acidentes de trânsito para cada cidade
for cidade in dados_cidades:
    cidade["indice_acidentes"] = cidade["acidentes"] / cidade["veiculos"]

# Passo 2: Identificar a cidade com o maior e menor índice de acidentes
cidade_maior_indice = max(dados_cidades, key=lambda x: x["indice_acidentes"])
cidade_menor_indice = min(dados_cidades, key=lambda x: x["indice_acidentes"])

# Passo 3: Calcular a média de veículos de passeio nas cinco cidades
media_veiculos = sum(cidade["veiculos"]
                     for cidade in dados_cidades) / len(dados_cidades)

# Passo 4: Calcular a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio
cidades_menos_2000_veiculos = [
    cidade for cidade in dados_cidades if cidade["veiculos"] < 2000]
media_acidentes_menos_2000 = sum(
    cidade["acidentes"] for cidade in cidades_menos_2000_veiculos) / len(cidades_menos_2000_veiculos)

# Exibindo os resultados
print("Maior índice de acidentes:",
      cidade_maior_indice["indice_acidentes"], "em", cidade_maior_indice["cidade"])
print("Menor índice de acidentes:",
      cidade_menor_indice["indice_acidentes"], "em", cidade_menor_indice["cidade"])
print("Média de veículos nas cinco cidades:", media_veiculos)
print("Média de acidentes nas cidades com menos de 2.000 veículos de passeio:",
      media_acidentes_menos_2000)
