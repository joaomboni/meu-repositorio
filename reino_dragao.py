import random
import time

def introducao():
    print(' Você está em uma terra cheia de dragoes na sua frente, ')
    print(' Você vê duas cavernas. Em uma delas o dragão é amigavel, ')
    print(' E compartilhará seu tesouro com voçê. O outro dragão, ')
    print(' É ganancioso e faminto, e irá comê-lo à primeira vista. ')
    print()

def esc_caverna():
    caverna = ''
    while caverna != '1' and caverna != '2':
        print(' Em qual caverna você irá? (1 ou 2)')
        caverna = input()

    return caverna

def check_caverna(escolhendo_caverna):
    print(' Você se aproxima da caverna ... ')
    time.sleep(2)
    print(' É escuro e assustador ... ')
    time.sleep(2)
    print(' Um granda dragão na sua frente ! ele abre a mandíbula ... ')
    print()
    time.sleep(2)

    cave_certa = random.randint(1, 2)

    if escolhendo_caverna == str(cave_certa):
        print(' Você ganhouo o tesouro! ')
    else:
        print(' O dragão devorou você em uma mordida! ')

chance = 'sim' 
while chance == 'sim' or chance == 'SIM':
    introducao()
    num_caverna = esc_caverna()
    check_caverna(num_caverna)
    print(' Você quer jogar outra vez ? ( sim ou não)' )
    chance = input()

        

        

        


