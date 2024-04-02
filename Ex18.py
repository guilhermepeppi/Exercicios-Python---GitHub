# Faça um programa que peça o tamanho de um arquivo para download (em MB)
# e a velocidade de um link de Internet (em Mbps), calcule e
# informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho = float(input("Digite o tamanho do arquivo em MB: "))
velocidade = float(input("Digite a velocidade da internet em Mbps: "))

tempo = tamanho / (velocidade / 8) / 60  # 1 byte = 8 bits e 1 minuto = 60 segundos

print(f"O tempo aproximado de download é de {tempo:.2f} minutos.")
