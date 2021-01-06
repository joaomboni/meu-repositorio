## jogo adivinhe o numero.
import random
guessesTaken = 0

print('Ola ! Qual é o seu nome ? ')
nome =  input()

num = random.randint(1, 10)
print('Bem, '+ nome +', Eu estou pensando um numero entre 1 é 10, tente advinhar.')
while guessesTaken < 6:
    print('Tente acertar.')
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < num:
        print('Sua tentativa é muito baixa.')

    if guess > num:
        print('Sua tentativa é muito alta.')

    if guess == num:
        break

if guess == num:
        guessesTaken = str(guessesTaken)
        print('Parabens ' + nome + ' você acertou o número !! '  + guessesTaken  +  ' tentativa!')
        
if guess != num:
        num = str(num)
        print(' Não, o número que eu estava pensando é ' + num)

