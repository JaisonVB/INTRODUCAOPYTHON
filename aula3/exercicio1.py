# Crie um algoritmo que efetua a leitura de cinco números diferentes e
# identifica o maior e o menor valor

v1 = int(input('Digite o primeiro valor '))
v2 = int(input('Digite o segundo valor '))
v3 = int(input('Digite o terceiro valor '))
v4 = int(input('Digite o quarto valor '))
v5 = int(input('Digite o quinto valor '))

maior = -999999999
menor = 999999999

if(v1 != v2 and v1 != v3 and v1 != v4 and v1 != v5 and v2!= v3 and v2 != v4 and v2 != v5 and v3 != v4 and v3 != v5 and v4 != v5):
    if (v1 > maior):
        maior = v1
    if(v2 > maior):
        maior = v2
    if(v3 > maior):
        maior = v3
    if(v4 > maior):
        maior = v4
    if(v5 > maior):
        maior = v5

    if (v1 < menor):
        menor = v1
    if (v2 < menor):
        menor = v2
    if (v3 < menor):
        menor = v3
    if (v4 < menor):
        menor = v4
    if (v5 < menor):
        menor = v5

    print('O maior valor digitado foi', maior)
    print('O menor valor digitado foi', menor)
