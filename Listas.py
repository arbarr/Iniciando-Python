#función Range con listas
"""
x = range (4)
print (x)
print (list (x))
friends = ['castañeda', 'esinosa', 'loco']
print (len(friends))
print (list (range(len(friends))))
"""
#creando listas con rage
"""
friends = ['castañeda', 'esinosa', 'loco']

for amigos in friends:
    print ('hola jovenes: ',amigos)
    

for i in range (len(friends)) :
    amigos = friends [i]
    print ('hola jovenes: ',amigos)
    
"""
#concatenando listas
"""
a = [1,2,4]
b = [5,6,7]
c = a + b
print (a)
print (c)
"""
#Promedio de numeros sin listas
"""
total = 0
conteo = 0
while True : 
     num = input ('Ingresa un numero: ')
     if num == 'done' : break
     valor = float (num)
     total = total + valor
     conteo = conteo + 1
promedio = total / conteo
print ('el promedio es:', promedio)
"""
#Promedio de numeros con listas
"""
listnum = list()
while True : 
     num = input ('Ingresa un numero: ')
     if num == 'done' : break
     valor = float (num)
     listnum.append(valor)
promedio = sum(listnum) / len(listnum)
print ('el promedio es:', promedio)

"""
# Organizando listas (por defecto)
"""   
cars = ['Ford', 'BMW', 'Volvo']
lista = cars.sort()
print (cars)
"""
# Organizando listas (reverse de mayor a menor)
"""   
cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)
print (cars)
"""
# Organizando listas con nuestro criterio (longitud de sus elementos)
"""
def myFunc(e):
  return len(e)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc)
print (cars)
"""
# Organizando listas con nuestro criterio (longitud de sus elementos) de mayor a menor
"""
def myFunc(e):
  return len(e)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(reverse=True, key=myFunc)
print (cars)
"""
# trabajando con strins y listas split()
"""
txt = "welcome to the jungle"
x = txt.split()
print(x)
"""
#sacar el host de "johan.jimenez@gmail.com.co domingo 05 de abril a las 22:05 horas"
# esta es mi forma de hacerlo
"""
file = open ('texto.txt')
texto = file.read()
x = texto.split("\n")
primer = x[0].split()
correo = primer[1].split('@')
host = correo[1]
print (host)
"""
#Iniciando con diccionarios
"""
maleta = dict()
maleta ['dinero'] = 50000
maleta ['dulces'] = 10
maleta ['camisas'] = 4
print (maleta)
print (maleta['dulces'])
maleta ['dulces'] = maleta ['dulces'] + 2
print (maleta)

diccionario = {'nombre' : 'johan', 'edad': 29, 'estado civil': 'soltero'}
print (diccionario)
print (diccionario['nombre'])
"""
# con que frecuencia vemos algo
"""
counts = dict ()
names = ['johan', 'jessi','johan','yeison','jessi']
for name in names :
    if name not in counts :
        counts[name] = 1
    else :
        counts [name ] = counts[name] + 1
print (counts)
"""
#metodo get con dicionarios
"""
counts = dict ()
names = ['johan', 'jessi','johan','yeison','jessi']
for name in names :
    print (counts.get(name,0))
    counts[name] = counts.get(name,0) + 1
print (counts)
"""

#diccionarios y archivos1
"""
palabras = {'computador' : 3, 'mesa' : 1, 'fuente' : 4}
for key in palabras :
    print (key,palabras[key])
"""
#diccionarios y archivos2
"""
goles = {'johan' : 2 , 'yeison ' : 4, 'mateo': 3}
print (list (goles))   
print (goles.keys()) 
print (goles.values())
print (goles.items())
"""
#diccionarios y archivos3

#diccionarios y archivos4 variables de 2 iteraciones
"""
goles = {'johan' : 2 , 'yeison ' : 4, 'mateo': 3}
for key, value in goles.items() :
    print (key, value)
"""    

#Ejercicio con archivos y diccionarios
"""
archivo = input ('Ingrese nombre del arcihvo: ')
file = open (archivo)
diccionario = dict()
for line in file :
    linea = line.split()
    for lineas in linea :
        diccionario [lineas] = diccionario.get(lineas,0) +1
print (diccionario)
conteomayor = None
palabramayor = None
for palabra, conteo in diccionario.items():
    if conteomayor is None or conteo > conteomayor :
        palabramayor = palabra
        conteomayor = conteo
print (palabramayor, conteomayor)
"""
#Tuplas
"""
goles = {'johan' : 2 , 'yeison ' : 4, 'mateo': 3}
tupla = goles.items()
print (tupla)

comp = (1,1,2) < (5,1,2) 
print (comp)
comp = (1,1,2) < (6,1,2) 
print (comp)
comp = ("joahn") < ("amor") 
print (comp)
comp = ("amor","yeizon") < ("amor","z")
print (comp)
"""
#organizarndo por llaves (key)
"""
goles = {'johan' : 2 , 'yeison ' : 4, 'mateo': 3}
item = goles.items()
print (item)
lorganizado = sorted(item)
print (lorganizado)
"""
#Organizar  los diccionaris por valores
"""
goles = {'johan' : 2 , 'yeison ' : 4, 'mateo': 3}
lista = list()
for nombre, gol in goles.items() :
    lista.append ((gol,nombre)) # esta es la clave se invierte goles y nombre
print (lista)
lista = sorted (lista,reverse=True)
print (lista)
"""
#Listas de compresión (listas simples)
"""
c = {'a' : 3, 'r' : 5, 'g' : 4}
print (sorted([(v,k) for k,v in c.items()]))
"""
#Listas de compresión (listas anidadas)
"""
empleados = [['juan' , 5000 , 'ventas'], ['elena' , 6000 , 'ventas'], ['marcos' , 3400 , 'operario']]
resultado1 = [ (nombre,sueldo) for nombre,sueldo,area in empleados if area is not 'ventas']
print (resultado1)
"""
#Bonus (jaor software)
"""
matriz = [[11,12,13],[21,22,23],[31,32,33]]
[[print(xdato) for xdato in fila ]for fila in matriz]
"""
#Ejercicio Final tal cua la guia 13 lineas
"""
file = open('texto.txt')
conteo = dict()

for line in file :
    matriz = line.split()
    for repeat in matriz :
        conteo [repeat] = conteo.get(repeat,0) +1

lista = list()

for llave,valor in conteo.items() :
    tupla = (valor,llave)
    lista.append(tupla)
    
lista = sorted(lista, reverse=True)

for valor, key in lista[:10] : 
    print (key,valor)
"""
#Ejercicio Final de la guia con una modificaciones propias 8 lineas
"""
file = open('texto.txt')
conteo = dict()

for line in file :
    matriz = line.split()
    for repeat in matriz :
        conteo [repeat] = conteo.get(repeat,0) +1

lista = sorted ([(valor, llave) for llave,valor in conteo.items()],reverse=True)
#print (lista)
[print(key,valor) for valor,key in lista[:10]]
"""

""" #Ejercicio Final Mi versión 6 lineas 
file = open('texto.txt')
#file = 'hola saludos hsludos'
listaAnidada = [line.split() for line in file ]
#print (matriz)
ListaSimple = [listSimple for sublista in listaAnidada for listSimple in sublista]
#print(uno)
frecPalabras=[ListaSimple.count(palabras) for palabras in ListaSimple]
#print(x)
#dict(list(zip(uno,x)))
result = sorted ([(valor, llave)for llave,valor in dict(list(zip(ListaSimple,frecPalabras))).items()],reverse =True)
#print (result)
[print(key,valor) for valor,key in result[:10]]
"""
#purebas compresion de listas
#print((i for i in range(3))) #no retrorna nada visible

#Retorna una Tubla = ((0, 0), (1, 1), (2, 4))
#tuple((v-tupla1=i,v-tupla2=i*i) for i in range(3))
print(tuple((i,i*i) for i in range(3)))   

#retorna una lista simple = [0, 1, 2]
# [elemetos de la lista = i for i in range(3)]
#cuando es una lista se ponen []
print([i for i in range(3)])

# otra fora de retornar una lista simple
#list(elemetos de la lista = i for i in range(3))
#en esta forma de declarar la lista se pone ()
print (list(i for i in range(3)))

#listas anidadas
#generando listas aninadas
#retorna =[[0, 1, 2], [0, 1, 2]]
#retorno2 = [0, 1, 2]
#observar muy bien como se escribio el codigo
hola = list()
hola= [[ h for h in range(3)],[ i for i in range(3)]]
print (hola)
print(hola[0])

#Aplanando listas anidadas de compresion
#esto se refiere a convertirla en una lista simple a una lista nidada
#Retorna = [11, 12, 13, 21, 22, 23, 31, 32, 33]
listaAnidada = [[11,12,13],[21,22,23],[31,32,33]]
ListaSimple = [listSimple for sublista in listaAnidada for listSimple in sublista]
print (ListaSimple)

#si quiero imprimir en una colomna todas los items de l alista puedo utilizar
#Retorna:
#11
#12
#13
#21
#22
#23
#31
#32
#33
[[print(xdato) for xdato in fila ]for fila in listaAnidada]

#Diccionarios
# Retorna un Diccionario ={0: 0, 1: 1, 2: 4}
#{(esta es la key) = i:(valores de cada key) = i**2 for i in range(3)}
#{2 -ESTE ES EL ELEMENTO DE CADA LLAVE : ESTE ES EL VALOR PARA CADA LLAVE 1-PARA cada ITERACION EN estos 3 numeros}
#para cada iteracion en estos 3 numeros
print({i:i**2 for i in range(3)})  










