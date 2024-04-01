# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = float(input('Digite o lado do quadrado: '))
area = lado ** 2
dobro_area = area * 2
print(f'A área do quadrado de lado {lado} é {area:.2f}.')
print(f'O dobro da área é {dobro_area:.2f}.')
