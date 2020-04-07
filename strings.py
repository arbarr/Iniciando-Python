
# convirtiendo cadenas de texto
"""
nombre = input ('ingrese su nombre: ')
print (nombre)

manzanas = input ('Ingrese cantidad: ')
x = int (manzanas) + 1 # aqui se rompera el codigo si o ponemos el int
print (x) 
"""
# recorrer el string
"""
nombre = 'johan arley'
for nom in nombre :
    print (nom)
print ("la longitud de johan arley es: ",len (nombre))
"""

#recorrer string con while
"""
nombre = 'johan arley'
indice = 0
while indice < len (nombre) :
    letra = nombre [indice]
    print (letra)
    indice = indice + 1
print ("la longitud de johan arley es: ",len (nombre))
"""
"""
#Poniendo Limites
nombre = 'johan arley'
print (nombre[0:5])
print (nombre[6:11])
"""
"""
#Otra forma de Poner Limites
nombre = 'johan arley'
print (nombre[:5])# muestre los primeros 5
print (nombre[6:])#oculte los primeros 6, ó muestre del indice 6 en adelante
print (nombre [:],'\n')#muestre todo
"""

#conparando strings, cmpara la primera letra la que este primero en el abcedario
"""
word = 'banano'
if word == 'banano' :
    print ('All right, bananos .')
if word < 'banano' :
    print ('Your word, ' + word + ', comes before banano ')
elif word > 'banano' :
    print ('Your word,' + word + ', comes after banano')
else :
    print ('All right, bananos .')
"""
#biblioteca sting mayusculas y minusculas
"""
greet = 'SIGNIFICA SALUDO'
minuscula = greet.lower()
print (minuscula)
print (minuscula.upper())v
"""

#Buscando strings encuentra el indice de la primer cadena a buscar
"""
nombre = 'raboncita'
buscar = nombre.find('bon')
print (buscar) 
"""
#Buscando strings desde un indice especifico
"""
nombre = 'rabonc ita'
buscar = nombre.find(' ',2)
print (buscar) 
"""

#Buscar y reemplazar
"""
greet = 'Significa saludo'
remplazar = greet.replace('Significa','Traducción al español = ')
print (remplazar)  
"""
#Quitar los espacios en blanco
"""
greet = '    *greet significa saludo*     '
print (greet)
print (greet.lstrip())
print (greet.rstrip())
print (greet.strip())
"""

#prefijos
"""
parabra = 'es un bonito dia hoy domingo'
print (parabra.startswith('bonito',6,17))
"""
#Analisis y estracción
datos = 'Escrito por johan.jimenez@perex.sern.us en febrero 15 de 2020'
inicio = datos.find ('@')
print (inicio)
fin = datos.find (' ',inicio)
print (fin)
terminal = datos [inicio +1 : fin]
print (terminal)
