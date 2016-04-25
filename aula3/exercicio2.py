print("-------------------------------------------------")
print("Que operacao voce deseja realizar? ")
print("Digite 1 para soma ")
print("Digite 2 para subtracao ")
print("Digite 3 para multiplicacao ")
print("Digite 4 para divisao ")
print("-------------------------------------------------")

try:
    operacao = int(input('Digite qual a operacao desejada '))
    operando1 = 0
    operando2 = 0

    if(operacao != 1 and operacao != 2 and operacao != 3 and operacao != 4):
        print("Operacao invalida!")
    else:
        operando1 = float(input("Digite o valor do primeiro operando "))
        operando2 = float(input("Digite o valor do segundo operando "))
        if(operacao == 4 and operando2 == 0):
            print("Valor invalido - divisao por zero")
        elif(operacao == 1):
            print("Resultado da soma ", operando1 + operando2)
        elif(operacao == 2):
            print("Resultado da subtracao ", operando1 - operando2)
        elif(operacao == 3):
            print("Resultado da multiplicacao ", operando1 * operando2)
        elif(operacao == 4):
            print("Resultado da divisao ", operando1 / operando2)

except ValueError:
    print("Digite apenas valores numericos de 1 a 4")




