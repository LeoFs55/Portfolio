import datetime

def date_validation(date):
    dia,mes,ano = date.split('/')
    dia_int, mes_int, ano_int = int(dia), int(mes), int(ano)
    try:
        valition = datetime.date(ano_int, mes_int, dia_int)
        return valition
    except:
        return 'data-invalida'

