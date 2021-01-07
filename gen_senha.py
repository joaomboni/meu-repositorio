nomeid = str(input( ' Escolha um nome de usuário: '))
senha = str(input( ' Esolha uma senha: ' ))
while senha == nomeid:
        print('ERRO, usuário não pode ser igual senha, tente novamente! ')
        nomeid = str(input( ' Esolha o nome de usuário: '))
        senha = str(input( ' Escolha uma senha: '))

else:
    print('pronto !')

 


              
