import random

# Forçar zeros à esquerda e remover parte decimal:
number = 3.141
print(f'{number:06.0f}')
# Forçar espaços em branco:
print(f'{int(number):6d}')
# Forçar total de dígitos (contando o ponto como dígito) e zeros:
print(f'{number:06.3f}')
# Forçar total de dígitos (contando o ponto como dígito) e zeros:
print(f'{number:06.3}')
# Imprimir com vírgula como separador de milhares e um número determinado de decimais (vírgulas e pontos contam como caracteres):
print(f'{number*10000:010,.2f}')
# Imprimir com vírgula como separador de milhares em um inteiro, forçando zeros à esquerda:
print(f'{int(number*100654):010,d}')
# Separar milhares com vírgulas e definir número de decimais é útil, por exemplo, para valores monetários:
print(f'R${10000.0:,.2f} ou US${1864.1590:,.2f} ou €{1530.50828:,.2f}')
# Forçar zeros pode ser útil para formatar datas:
print(f'{random.randint(1,28):02d}/{random.randint(1,12):02d}/{random.randint(1,2050):04d}')
