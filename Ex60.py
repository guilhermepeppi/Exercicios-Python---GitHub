# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça
# um programa capaz de gerar a série até o n−ésimo termo.

n = int(input('Digite o n-ésimo termo da série de Fibonacci: '))
ultimo = 1
penultimo = 1

if n == 1:
    print(1)
elif n == 2:
    print('1 1')
else:
    print('1 1', end=' ')
    for i in range(3, n + 1):
        termo = ultimo + penultimo
        print(termo, end=' ')
        penultimo = ultimo
        ultimo = termo
