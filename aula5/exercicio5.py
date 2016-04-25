

def verifica_maiorValor(v1, v2, v3, v4, v5):
    maior = -999999999
    if(v1 > maior):
        maior = v1
    if(v2 > maior):
        maior = v2
    if(v3 > maior):
        maior = v3
    if(v4 > maior):
        maior = v4
    if(v5 > maior):
        maior = v5
    return maior

def verifica_menorValor(v1, v2, v3, v4, v5):
    menor = 999999999
    if(v1 < menor):
        menor = v1
    if(v2 < menor):
        menor = v2
    if(v3 < menor):
        menor = v3
    if(v4 < menor):
        menor = v4
    if(v5 < menor):
        menor = v5
    return menor

val_1 = int(input("Digite o primeiro numero "))
val_2 = int(input("Digite o segundo numero "))
val_3 = int(input("Digite o terceiro numero "))
val_4 = int(input("Digite o quarto numero "))
val_5 = int(input("Digite o quinto numero "))

if(val_1 != val_2 and val_1 != val_3 and val_1 != val_4 and val_1 != val_5 and val_2 != val_3 and val_2 != val_4 and val_2 != val_5 and val_3 != val_4 and val_3 != val_5 and val_4 != val_5):
    print('Maior valor ', verifica_maiorValor(val_1, val_2, val_3, val_4, val_5))
    print('Menor valor ', verifica_menorValor(val_1, val_2, val_3, val_4, val_5))
else:
    print("Valores repetidos, tente outra vez ")
