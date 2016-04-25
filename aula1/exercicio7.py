# Uma fábrica de camisetas produz os tamanhos pequeno, médio e grande,
# cada uma sendo vendida respectivamente por 10,12 e 15 reais.
# Construa um algoritmo em que o usuario forneca a quantidade de camisetas
# pequenas, médias e grandes referentes a uma venda, e o
# programa informe quanto será o valor arrecadado

valor_ref_P = 10
valor_ref_M = 12
valor_ref_G = 15

quant_P = int(input('Quantidade de vendas tamanho P '))
quant_M = int(input('Quantidade de vendas tamanho M '))
quant_G = int(input('Quantidade de vendas tamanho G '))

total_vendas = quant_P * valor_ref_P + quant_M * valor_ref_M + quant_G * valor_ref_G

print('Total vendido R$ ' + str(total_vendas))