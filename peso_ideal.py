nome = input('Oi, sou o robô da saude, qual é o seu nome ? ')
     
h = float(input('Digite sua altura: '))

peso = float(input('Digite seu peso: '))

sexo = int(input('Escolha: 1- Sexo Masculino / 2- Sexo Feminino: '))

peso_ideal = (72.7*h)-58 if sexo == 1 else (62.1*h)-44.7

if peso < peso_ideal:
    print('Poxa ' , nome , ' você está baixo do peso ideal !')
elif peso == peso_ideal:
    print('Prabanes', nome , ' você está dentro do peso ideal !')
else:
    print('Poxa', nome, ' você está acima do peso ideal !')


    

