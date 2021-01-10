
dia = ['zero','um','dois','tres','quatro', 'cinco', 'seis','sete',
       'nove','dez','onze','doze','treze','quatorze',
       'quinze','dezesseis','dezessete','dezoito','dezenove',
       'vinte','vinte e um','vinte e dois','vinte e tres','vinte e quatro',
       'vinte e cinco','vinte e seis','vinte e sete','vinte e oito','vinte e nove',
       'trinta','trinte e um']

meses = ["zero",
         "janeiro",
         "fevereiro",
         "março",
         "abril",
         "maio",
         "junho",
         "julho",
         "agosto",
         "setembro",
         "outubro",
         "novembro",
         "dezembro"]
while True:
    data_dia = int(input("informe o dia que deseja transformar: "))
    data_meses = int(input('informe o mês que deseja transformar: '))
    data_ano = int(input('Digite o ano que você esta:'))
    if data_dia == dia or data_meses == meses:
        break
    print(f'Dia, {dia[data_dia]} de, {meses[data_meses]}', data_ano)
