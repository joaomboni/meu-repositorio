def converta(h, m):
    if 0 < h <= 12 and 0 < m < 60:
        print(f'{h}:{m} am')
    elif 12 < h < 24 and 0 < m < 60:
        print(f'{h - 12}:{m} pm')
    else:
        print('valor inválido')


while True:
    h = int(input(' Hora: '))
    if h == 999: break
    m = int(input(' Minuto: '))
    converta (h,m)
    print('='*12)
    
