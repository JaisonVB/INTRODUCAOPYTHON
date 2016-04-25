# Ler uma temperatura em graus Fahrenheit  e apresenta-la convertida
# em graus Celsius. A fórmula de conversão é: C = (F-32)*(5/9)

temp_fahrenheith = float(input('Digite a temperatura em graus Fahrenheith '))
temp_celcius = (temp_fahrenheith - 32) * (5/9)

print( str(temp_fahrenheith) +  ' graus Fahrenheith corresponde a ' + str(temp_celcius) + ' graus Celsius')
