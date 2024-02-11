def alessandro():
    p1 = str(input('Bem vindo de volta Alessandro...'))

def criarconta():
    nome1 = str(input("Digite o seu primeiro nome: "))
    nome2 = str(input("Digite o seu ultimo nome: "))
    email = str(input("Digite o seu melhor Email: "))
    password1 = str(input("Digite uma palavra passe no minímo com 6 digitos: "))



def entrar():
    email = str(input("Digite o seu email: "))
    password = str(input("Digite sua palavra passe: "))

    if email == 'alessandropaulino@gmail.com' and password == 'Catambi8899' or 'Alessandropaulino@gmail.com' and password == 'Catambi8899':
        alessandro()


    else:
        print('Parece que vc ainda não têm uma conta ou está a digitar incorretamente os seus dados!')
    c = str(input('Se deseja tentar novamente digite 1, se pretende criar conta digite 0: '))
    if c == 1:
        entrar()
    elif c == 0:
        criarconta()    



