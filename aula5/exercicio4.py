# Crie uma função que imprime a tabuada do número recebido como parâmetro


def imprime_tabuada(valor):
    for i in range(1,11):
        print(int(valor) * i)

imprime_tabuada(5)