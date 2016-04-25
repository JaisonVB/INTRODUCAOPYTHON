# Crie um algoritmo que realiza a leitura de três valores, 
# armazena esses valores em variáveis e informa qual foi o maior valor digitado
# 
# este algoritmo não funciona corretamente porque não são testadas todas as
# possibilidades 

valor1 = int(input("Digite o primeiro valor "))
valor2 = int(input("Digite o segundo valor "))
valor3 = int(input("Digite o terceiro valor "))

maior = 0

if(valor1 > maior):
    maior = valor1
elif(valor2 > maior):
    maior = valor2
elif(valor3 > maior):
    maior = valor3

print("O maior valor digitado foi", maior)
