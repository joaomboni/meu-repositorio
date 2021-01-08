inventario = []
res = 's'
while res == 's':
    inventario.append(input('equipamento:'))
    inventario.append(float(input('valor:')))
    inventario.append(int(input('número social:')))
    inventario.append(input('departamento:'))
    res = input('digite /"s/" para continuar:').upper()

for elemento in inventario:
    print(elemento)
