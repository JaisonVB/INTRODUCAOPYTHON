# Crie uma função que recebe como parâmetros dois valores e retorna o menor valor


def menor_valor(valor1, valor2):
    if (valor1 < valor2):
        return valor1
    else:
        return valor2


entrada_1 = int(input('digite um valor '))
entrada_2 = int(input('digite um valor '))

print('O menor valor digitado foi ', menor_valor(entrada_1, entrada_2))
