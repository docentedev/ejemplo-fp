usuario = {
    'id': 12,
    'name': 'Carlos',
}
print(f'El nombre es: {usuario['name']}')

numeros = []
opt = ''
while opt != 'x':
    opt = input('Ingrese una opción (sumar, res, x para salir): ')
    if opt == 'sumar':
        print('Sumando...')
        nuevo_num = 0.0
        while True:
            try:
                nuevo_num = float(input('ingrese num: '))
                break
            except ValueError:
                print('Valor incorrecto...')
        numeros.append(nuevo_num)
        print(numeros)
    if opt == 'res':
        print('Resultado')
        resultado = sum(numeros)
        promedio = resultado / len(numeros)
        print(f'El resultado es: {resultado}')
        print(f'El promedio: {promedio}')

