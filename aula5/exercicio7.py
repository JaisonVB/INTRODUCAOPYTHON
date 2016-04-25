

def signos(dia, mes):
    JANEIRO = 1
    FEVEREIRO = 2
    MARCO = 3
    ABRIL = 4
    MAIO = 5
    JUNHO = 6
    JULHO = 7
    AGOSTO = 8
    SETEMBRO = 9
    OUTUBRO = 10
    NOVEMBRO = 11
    DEZEMBRO = 12
    if(dia >= 21 and mes == MARCO) or (dia <= 20 and mes == ABRIL):
        return 'Aries'
    elif(dia >= 21 and mes == ABRIL) or (dia <= 20 and mes == MAIO):
        return'Touro'
    elif(dia >= 21 and mes == MAIO) or (dia <= 21 and mes == JUNHO):
        return 'Gemeos'
    elif(dia >= 21 and mes == JUNHO) or (dia <= 21 and mes == JULHO):
        return'Cancer'
    elif(dia >= 22 and mes == JULHO) or (dia <= 22 and mes == AGOSTO):
        return'Leao'
    elif(dia >= 23 and mes == AGOSTO) or (dia <= 22 and mes == SETEMBRO):
        return 'Virgem'
    elif(dia >= 23 and mes == SETEMBRO) or (dia <= 22 and mes == OUTUBRO):
        return 'Libra'
    elif(dia >= 23 and mes == OUTUBRO) or (dia <= 21 and mes == NOVEMBRO):
        return 'Escorpiao'
    elif(dia >= 22 and mes == NOVEMBRO) or (dia <= 21 and mes == DEZEMBRO):
        return 'Sagitario'
    elif(dia >= 22 and mes == DEZEMBRO) or (dia <= 20 and mes == JANEIRO):
        return 'Capricornio'
    elif(dia >= 21 and mes == JANEIRO) or (dia <= 19 and mes == FEVEREIRO):
        return'Aquario'
    elif(dia >= 20 and mes == FEVEREIRO) or (dia <= 20 and mes == MARCO):
        return 'Peixes'

dia_nascimento = int(input('Digite o dia de seu nascimento '))
mes_nascimento = int(input('Digite o mês de seu nascimento '))

print('Seu signo é ', signos(dia_nascimento, mes_nascimento))