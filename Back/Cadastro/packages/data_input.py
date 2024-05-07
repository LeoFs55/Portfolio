import packages.password_validation as password_validation
import packages.name_validation as name_validation
import packages.age_validation as age_validation
import packages.cpf_validation as cpf_validation

def data_input(name,surname,age,cpf,password):
    with open('Back\Cadastro\data\dados.txt','r+',encoding='utf-8') as pagina:
        if cpf not in pagina.read():    
            pagina.write(f"""
    'nome':{name_validation.name(name)},
    'sobrenome':{name_validation.surname(surname)},
    'data-nascimento':{age_validation.date_validation(age)},
    'cpf':{cpf_validation.cpf(cpf)},
    'senha':{password_validation.password(password)}
""")
            return 'Usuário cadastrado'
        else: 
            return 'Usuário já cadastrado.'