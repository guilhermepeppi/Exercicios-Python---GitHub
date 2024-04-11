# Uma academia deseja fazer um senso entre seus clientes para descobrir o mais
# alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um
# programa que pergunte a cada um dos clientes da academia seu código, sua
# altura e seu peso.

# O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero)
# no campo código.

# Ao encerrar o programa também deve ser informados os códigos e valores do
# clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média
# das alturas e dos pesos dos clientes.

clientes = {'codigo': 0, 'altura': 0, 'peso': 0}

while True:
    try:
        clientes['codigo'] = int(input('Código: '))
        if clientes['codigo'] == 0:
            break
        else:
            clientes['altura'] = float(input('Altura: '))
            clientes['peso'] = float(input('Peso: '))
            continue
    except:
        print('\033[31mERRO! Digite um valor válido.\033[m')
