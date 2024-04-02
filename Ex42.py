# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"

# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.

# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
# Caso contrário, ele será classificado como "Inocente".

telefonou = input("Telefonou para a vítima? (s/n) ")
esteve = input("Esteve no local do crime? (s/n) ")
mora = input("Mora perto da vítima? (s/n) ")
devia = input("Devia para a vítima? (s/n) ")
trabalhou = input("Já trabalhou com a vítima? (s/n) ")

respostas = [telefonou, esteve, mora, devia, trabalhou]
positivos = respostas.count("s")

if positivos == 2:
    print("Suspeita")
elif 3 <= positivos <= 4:
    print("Cúmplice")
elif positivos == 5:
    print("Assassino")
else:
    print("Inocente")
