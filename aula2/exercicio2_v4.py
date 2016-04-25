# Crie um algoritmo que realiza a leitura de três valores, 
# armazena esses valores em variáveis e informa qual foi o maior valor digitado

valor1 = int(input("Digite o primeiro valor "))
valor2 = int(input("Digite o segundo valor "))
valor3 = int(input("Digite o terceiro valor "))

maior = 0

if((valor1 > valor2) and (valor1 > valor3)):
    print("O maior valor digitado foi", valor1)
elif((valor2 > valor1) and (valor2 > valor3)):
    print("O maior valor digitado foi", valor2)
elif((valor3 > valor1) and (valor3 > valor2)):
    print("O maior valor digitado foi", valor3)

