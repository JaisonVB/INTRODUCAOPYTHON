# Crie uma função que calcula a média de três valores passados por parâmetro


def media_valores(valor1, valor2, valor3):
    media = valor1 + valor2 + valor3
    return media/3

v1 = int(input('digite o primeiro valor '))
v2 = int(input('digite o segundo valor '))
v3 = int(input('digite o terceiro valor '))

print('a média é ', media_valores(v1,v2,v3))