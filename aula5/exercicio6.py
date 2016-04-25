


def calcula_imc(peso, altura):
    calc_imc = float(peso) / (float(altura) * float(altura))
    return calc_imc

peso = int(input('digite seu peso '))
altura = float(input('digite sua altura '))

imc = calcula_imc(peso, altura)

if(imc < 16.0):
    print(str(imc) + ' Magreza grave')
if(imc >= 16.0 and imc < 17.0):
    print('IMC = ' + str(imc) + ' Magreza moderada')
if(imc >= 17.0 and imc < 18.5):
    print('IMC = ' + str(imc) + ' Magreza leve')
if(imc >= 18.5 and imc < 25.0):
    print('IMC = ' + str(imc) + ' Saudavel')
if(imc >= 25.0 and imc < 30.0):
    print('IMC = ' + str(imc) + ' Sobrepeso')
if(imc >= 30.0 and imc < 35.0):
    print('IMC = ' + str(imc) + ' Obesidade grau 1')
if(imc >= 35.0 and imc < 40.0):
    print('IMC = ' + str(imc) + ' Obesidade grau 2')
if(imc >= 40.0):
    print('IMC = ' + str(imc) + ' Obesidade morbida')
