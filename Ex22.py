# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input('Digite uma letra: ')).strip().lower()[0]

if letra in 'aeiou':
    print(f'{letra} é uma vogal')
else:
    print(f'{letra} é uma consoante')
