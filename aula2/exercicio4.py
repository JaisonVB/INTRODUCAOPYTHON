dia = int(input("Digite o dia do seu aniversario "))
mes = int(input("Digite o mes do seu aniversario "))

JANEIRO   = 1
FEVEREIRO = 2
MARCO     = 3
ABRIL     = 4
MAIO      = 5
JUNHO     = 6
JULHO     = 7
AGOSTO    = 8
SETEMBRO  = 9
OUTUBRO   = 10
NOVEMBRO  = 11
DEZEMBRO  = 12

if(dia >= 21 and mes == MARCO) or (dia <= 20 and mes == ABRIL):
    print('Áries') 
elif(dia >= 21 and mes == ABRIL) or (dia <= 20 and mes == MAIO):
    print('Touro') 
elif(dia >= 21 and mes == MAIO) or (dia <= 21 and mes == JUNHO):
    print('Gêmeos')
elif(dia >= 21 and mes == JUNHO) or (dia <= 21 and mes == JULHO):
    print('Câncer')
elif(dia >= 22 and mes == JULHO) or (dia <= 22 and mes == AGOSTO):
    print('Leão') 
elif(dia >= 23 and mes == AGOSTO) or (dia <= 22 and mes == SETEMBRO):
    print('Virgem')
elif(dia >= 23 and mes == SETEMBRO) or (dia <= 22 and mes == OUTUBRO):
    print('Libra') 
elif(dia >= 23 and mes == OUTUBRO) or (dia <= 21 and mes == NOVEMBRO):
    print('Escorpião') 
elif(dia >= 22 and mes == NOVEMBRO) or (dia <= 21 and mes == DEZEMBRO):
    print('Sagitário')
elif(dia >= 22 and mes == DEZEMBRO) or (dia <= 20 and mes == JANEIRO):
    print('Capricórnio')
elif(dia >= 21 and mes == JANEIRO) or (dia <= 19 and mes == FEVEREIRO):
   print('Aquário')
elif(dia >= 20 and mes == FEVEREIRO) or (dia <= 20 and mes == MARCO):
   print('Peixes')



