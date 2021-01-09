## Criando sistema de dados para uma empresa.

equipamentos = []
valores = []
seriais = []
departamentos = []
resposta ='s'
while resposta == 's':
    equipamentos.append(input('Equipamento: '))
    valores.append(float(input('Valores: ')))
    seriais.append(int(input('Número serial: ')))
    departamentos.append(input('Departamentos: '))
    resposta = input('Digite < s > para continuar.').upper()

for equipamento in equipamentos:
    print('Equipamento: ', equipamento)
for indice in range(0,len(equipamentos)):
    print('\nEquipamento:', (indice+1))
    print('nome...........:', equipamentos[indice])
    print('valor...........:', valores[indice])
    print('serial..........:', seriais[indice])
    print('Departamento.:', departamentos[indice])

##para buscar um dado expecifico.

busca = input('\nDigite o nome do equipamento que deseja buscar:')
for indice in range(0,len(equipamentos)):
    if busca == equipamentos[indice]:
        print('Valor..:', valores[indice])
        print('serial.:', seriais[indice])

##• Situação 1: todos os equipamentos “impressora” receberão uma
##depreciação (desvalorização após certo período) de 10%. Monte o código
##que seria responsável por alterar o valor de todos os equipamentos.

depreciacao = input('\nDigite o nome do equipamento que será depreciado: ')
for indice in range(0,len(equipamentos)):
    if depreciacao==equipamentos[indice]:
        print('valor antigo:', valores[indice])
        valores = valores[indice] == valores[indice] * 0.9
        print('Novo valor: ', valores[indice])

#Situação 2: um equipamento com um determinado número serial foi
#danificado e será descartado. Precisamos eliminar esse equipamento.

serial = int(input('\nDigite o serial do equipamento que deseja excluir: '))
for indice in range(0, len(departamentos)):
    if seriais[indice]==serial:
        del departamentos[indice]
        del equipamentos[indice]
        del seriais[indice]
        del valores[indice]
        break

for indice in range(0,len(equipamentos)):
    print('\nEquipamento..:', (indice+1))
    print('Nome............:', equipamentos[indice])
    print('Valores.........:', valores[indice])
    print('serial...........:', seriais[indice])
    print('Departamento......:', departamentos[indice])
