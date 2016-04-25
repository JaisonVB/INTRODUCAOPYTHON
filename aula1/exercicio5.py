# Elaborar um programa que efetue a leitura de três valores inteiros (variáveis A, B, C)
# e apresente como resultado final o valor do quadrado da soma

var_A = int(input('Digite o primeiro valor '))
var_B = int(input('Digite o primeiro valor '))
var_C = int(input('Digite o primeiro valor '))

soma = var_A + var_B + var_C
soma_quadrado =  soma * soma

print('O quadrado da soma dos valores digitados he  ' + str(soma_quadrado))