
def objeto():
    print('Hola')
print('Diversión')

objeto()
print('Zip')
objeto()

#pueba calcular salario
def calculesalario (hora,tarifa):
    resulta = int (hora) * int (tarifa)
    return resulta

hora = input ('Ingrese horas trabajadas: ')
tarifa = input ('Ingrese tarifa: ')
resultado = calculesalario (hora,tarifa)
print ('Tu salario es de:', resultado)