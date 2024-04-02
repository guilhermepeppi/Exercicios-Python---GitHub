# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

data = input("Digite uma data no formato dd/mm/aaaa: ")
dia, mes, ano = data.split("/")
dia = int(dia)
mes = int(mes)
ano = int(ano)
if mes == 2:
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        if dia > 0 and dia <= 29:
            print("Data válida")
        else:
            print("Data inválida")
    else:
        if dia > 0 and dia <= 28:
            print("Data válida")
        else:
            print("Data inválida")
elif mes in [1, 3, 5, 7, 8, 10, 12]:
    if dia > 0 and dia <= 31:
        print("Data válida")
    else:
        print("Data inválida")
elif mes in [4, 6, 9, 11]:
    if dia > 0 and dia <= 30:
        print("Data válida")
    else:
        print("Data inválida")
else:
    print("Data inválida")
