# Crie uma função que recebe como entrada uma string e imprime a string invertida


def inverte_string(strParaInverter):
    tam = len(strParaInverter)
    for i in range(tam-1, -1, -1):
        print(strParaInverter[i])

inverte_string('OlaMundo')