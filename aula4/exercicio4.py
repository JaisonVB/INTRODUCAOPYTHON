# Crie um algoritmo que deixe o usuário digitar
# 10 numeros positivos e imprima a raiz
# quadrada de cada numero. Para cada
# entrada de dados devera haver um trecho de
# protecao para evitar que numeros negativos
# sejam aceitos.

import math

numero = 0
for i in range(0,10):
    numero = int(input('digite um numero '))
    while(numero < 0):
        numero = int(input('digite um numero'))
    print('raiz quadrada de ' + str(numero) + ' he ',math.sqrt(numero))
