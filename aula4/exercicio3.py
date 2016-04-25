# Crie um algoritmo que pergunta ao usuario
# quantos numeros ele deseja digitar e apos
# isso realiza as leituras e imprime a soma dos
# valores

valores = int(input('Quantos numeros deseja digitar? '))
soma = 0
for i in range(0,valores):
    soma = soma + int(input('digite um valor '))
print('a soma dos valores ', soma)