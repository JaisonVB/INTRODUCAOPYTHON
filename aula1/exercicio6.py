# Elaborar um programa que efetue a leitura de quatro valores inteiros (variáveis A, B, C e D).
# Ao final o programa deve apresentar o resultado do produto (variável P) do primeiro com o terceiro valor,
# e o resultado da soma (variável S) do segundo com o quarto

var_A = int(input('Digite o primeiro valor '))
var_B = int(input('Digite o segundo valor '))
var_C = int(input('Digite o terceiro valor '))
var_D = int(input('Digite o quarto valor '))

var_P = var_A * var_C
var_S = var_B + var_D

print('Produto do primeiro com o terceiro ' + str(var_P))
print('Soma do segundo com o quarto ' + str(var_S))

