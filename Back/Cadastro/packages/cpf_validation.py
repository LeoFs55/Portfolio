def calculo_digit1(cpf):
    resultado = [int(cpf[indice]) * mult for indice, mult in enumerate(range(10,1,-1))]
    soma = 0
    for i in resultado:
        soma += i         
    digito = ((soma*10)%11)
    digito = 0 if digito > 9 else digito
    return str(digito)

def calculo_digit2(cpf):
    resultado = [int(cpf[indice]) * mult for indice, mult in enumerate(range(11,1,-1))]
    soma = 0
    for i in resultado:
        soma += i         
    digito = ((soma*10)%11)
    digito = 0 if digito > 9 else digito
    return str(digito)

def num_validation_on_cpf(cpf):
    numeric = cpf.isnumeric()
    if numeric:
        return True
    else:
        return False
def cpf(cpf):
    if num_validation_on_cpf(cpf):
        with_1_digit = calculo_digit1(cpf)
        with_2_digit = calculo_digit2(cpf)
        cpf_inter = cpf[:9]+with_1_digit+with_2_digit
        cpf_valid = cpf_inter if cpf == cpf_inter else 'cpf-invalido'
        return cpf_valid
    else:
        raise ValueError('input-invalid')

    