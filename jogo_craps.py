from random import randint
print(' Bem vindo ao craps !!\n')
pergunta = input(' Você quer jogar craps sim / não ?\n ' )
if pergunta == 'sim':
        inst = input(' Você precisa de instrução sim / não ?\n ')
        if inst == 'sim':
            print(' Instruções!')
while pergunta == 'sim' or pergunta != 'sim':
        pause = input(' Pressione y para jogar o dado !\n')
        if pause == 'y' :
            d1= randint(2,12)
            print(d1)
        if d1 == 7 or d1 == 11:
            print(' Você venceu!')
            break
        elif d1 == 2 or d1 == 3 or d1 == 12:
            print(' Você perdeu!')
            break
        else:
            print(' Seu ponto!')
    
            
            
 
