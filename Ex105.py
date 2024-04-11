# Faça um programa que leia um número indeterminado de valores, correspondentes
# a notas, encerrando a entrada de dados quando for informado um valor igual a
# -1 (que não deve ser armazenado).

# Após esta entrada de dados, faça:
# 1) Mostre a quantidade de valores que foram lidos;
# 2) Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# 3) Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# 4) Calcule e mostre a soma dos valores;
# 5) Calcule e mostre a média dos valores;
# 6) Calcule e mostre a quantidade de valores acima da média calculada;
# 7) Calcule e mostre a quantidade de valores abaixo de sete;
# 8) Encerre o programa com uma mensagem;

valores = []
qtde_valores_lidos = 0

while True:
    try:
        valor = int(input('Informe um valor (ou -1 para encerrar: '))
        if valor != -1:
            valores.append(valor)
            qtde_valores_lidos += 1
        else:
            print('\n8) ENCERRANDO ENTRADA DE DADOS\n')
            break
    except ValueError:
        print('\033[31mERRO! Digite um valor válido.\033[m')

print('\n1) QUANTIDADE DE VALORES QUE FORAM LIDOS')
print(f'{qtde_valores_lidos}')

print('\n2) EXIBA TODOS OS VALORES NA ORDEM EM QUE FORAM INFORMADOS, UM AO LADO DO OUTRO')
for i in range(len(valores)):
    print(f'{valores[i]}', end=' ')
print()

print('\n3) LISTA REVERSA')
vetor_reverso = list(reversed(valores))
print(f'{vetor_reverso}')

print('\n4) SOMA DOS VALORES')
soma = sum(valores)
print(f'{soma}')

print('\n5) MÉDIA DOS VALORES')
media = soma / len(valores)
print(f'{media}')

print('\n6) VALORES ACIMA DA MÉDIA')
for j in range(len(valores)):
    if valores[j] > media:
        print(f'{valores[j]}')

print('\n7) VALORES ABAIXO DE SETE')
for k in range(len(valores)):
    if valores[k] < 7:
        print(f'{valores[k]}')

print('\nPROGRAMA ENCERRADO\n')
exit()
