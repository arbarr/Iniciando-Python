# Secuencial
print('Secuencial')
x = 2
print (x)
x = x + 2
print (x ,'\n')

#Presedencia de Operadores
print ('lo Siguiente es para demostrar la precedencia de operadores\n')
print ('b = 1 + 2 ** 3 / 4 * 5\n')
print( '1:  2 ** 3 =', 2 ** 3,'\n')
print ('2: 1 /4 =',2 ** 3 /4,'\n')
print ('3: 2 * 5 =',2 ** 3 /4 * 5,'\n' )
print ('4: 1 + 3 =',1 + 2 ** 3 /4 * 5,'\n' )


# if
print('El siguiente es un if')
a = 5
if a < 10:
    print('Numero menor a 10')
if a > 20:
    print('Nnumero mayor a 20')
print('Fin del if\n ')

#while
print('Lo siguiente es un while')
n = 5
while n > 0 :
    print (n)
    n = n - 1
print('salí del while\n')

#convirtiendo valores
print ('El siguiente es la canversion de un String to Integer')
print ('c = string 123', type('123'))
print ('c en entero es:',int('123'),type (int('123')))
print ('ahora puedo sumar 123 + 1 = ',int ('123')+1,type (int ('123')+1),'\n')

#Obteniendo datos del exterior (teclado)
print('Obtener datos del exterior, teclado')
nombre = input ('Quien eres? ')
print('Bienvenido:',nombre)

#convertidos de pisos
print('este es el convertidor de pisos del ascensor')
inp = input ('Piso Eurpeo?')
usf = int(inp) + 1
print ('Piso equivalente USA', usf,'\n')

# try except
print('el siguiente es un ejemplo del try except\n')
astr = 'Cadena de texto'
print('soy un ', astr ,' un',type (astr))
try:
    print ('qui estoy en el primer try ejecutaré int(Cadena de texto) y fallaré')
    istr = int(astr)
except:
    print('estoy en el primer excetp')
    istr = -1
print('Como el codigo el try falló, ejecuto except y en este caso  No detengo la ejecución y muestro', istr,'\n')
astr = '123'
print('soy una cadena de texto pero en numeros co el valor ', astr ,' un',type (astr))
try:
    print ('qui estoy en el segundo try ejecutaré int(123) y esto no fallará')
    istr = int(astr)
except:
    print ('aqui estoy en el segundo except y este codigo no se ejecuta por que int(123) del segunto try es correcto ')
    istr = -1
print('Ejecuto lo del segundo try y sigue l aejecución', istr)
