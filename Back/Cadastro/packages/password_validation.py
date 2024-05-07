erro = ''
def first_letter(password):
    first = password[0].isupper()
    if first:
        return True
    global erro
    erro = 'A primeira letra precisa ser maiuscula.'
    return False

def quantidade(password):
    quant = len(password)
    if quant>7:
        return True
    global erro
    erro = 'A senha precisa ser ter 8 caracteres'
    return False

def special_caracter(password):
    special = ['!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/','_','+']
    for i in special:
        if i in password:
            return True
    global erro
    erro = "Sua senha deve ter '!','"',"#","$","%","&","'",'(',')','*','+',',','-','.','/','_','+'"
    return False

def password(password):
    if special_caracter(password) and quantidade(password) and first_letter(password):
        return password
    return erro

