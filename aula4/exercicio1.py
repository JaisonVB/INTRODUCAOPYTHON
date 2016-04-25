# Crie um algoritmo que realiza a leitura de 5
# valores e imprime o total e a media

valor = 0

for i in range(0,5):
    valor = valor + int(input('digite o valor '))

print('total: ', valor)
print('media:', float(valor/5.0))