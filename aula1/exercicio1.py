# Ler uma temperatura em graus Celsius e apresenta-la convertida
# em graus Fahrenheit. A fórmula de conversão é: F = (9*C+160)/5

temp_celcius = int(input('Digite a temperatura em graus Celsius '))
temp_fahrenheith = (9 * temp_celcius + 160)/5

print( str(temp_celcius) +  ' graus Celsius corresponde a ' + str(temp_fahrenheith) + ' graus fahrenheith')
