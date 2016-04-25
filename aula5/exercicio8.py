

def valida_cpf(str_cpf):
    digito_1 = int(str_cpf[9])  # primeiro digito verificador
    digito_2 = int(str_cpf[10]) # segundo digito verificador
    acumulador_d1 = 0
    acumulador_d2 = 0
    calculo_digito1 = 0
    calculo_digito2 = 0
    for i in range(0, 9):
        acumulador_d1 += (int(str_cpf[i]) * (10 -i))
    calculo_digito1 = 11 - (acumulador_d1 % 11)
    if (calculo_digito1 == digito_1) or (calculo_digito1 > 9 and digito_1 == 0):
        print('Primeiro digito ', digito_1)
        for i in range(0, 10):
            acumulador_d2 += (int(str_cpf[i]) * (11 -i))
        calculo_digito2 = 11 - (acumulador_d2 % 11)
        if(calculo_digito2 == digito_2):
            print('Segundo digito ', digito_2)
            print('CPF valido! ')
        else:
            print('CPF invalido ', calculo_digito2)
    else:
        print('CPF invalido ', calculo_digito1)

valida_cpf('12345678909')