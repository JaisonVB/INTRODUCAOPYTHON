peso = float(input("Digite seu peso "))
altura = float(input("Digite sua altura "))

imc = float(peso) / (float(altura) * float(altura))    

if(imc < 16):
    print(imc, " magreza grave")
if(imc >= 16 and imc < 17):
    print(imc, " magreza moderada")
if(imc >= 17 and imc < 18):
    print(imc, " magreza leve")
if(imc >= 18 and imc < 25):
    print(imc, " saudável")
if(imc >= 25 and imc < 30):
    print(imc, " sobrepeso")      
if(imc >= 30 and imc < 35):
    print(imc, " obesidade grau 1")          
if(imc >= 35 and imc < 40):
    print(imc, " Obesidade grau 2")          
if(imc >= 40):
    print(imc, " Obesidade mórbida")

