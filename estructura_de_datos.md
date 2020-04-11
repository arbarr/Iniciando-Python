# Estructura de datos
## Strings
* los strins con una secuencia de caracteres.
* se usan `'string'` ó `"string"`
* cuando se usa el operador + con string significa concatenar, unir cadenas de texto
* cuando un string contiene numeros, hay que tener cuidado por que podemos causar un error en la ejecucion del programa
* si se va a trabajar con numeros lo mejor es convertirlos `string ` to `int` con `int('string')` y de esta forma ya podemos tratarlo como un dato numerico

```python
nombre = input ('ingrese su nombre: ')
print (nombre)

manzanas = input ('Ingrese cantidad: ')
x = int (manzanas) + 1 # aqui se rompera el codigo si o ponemos el int
print (x) 
```

### Mirando dentro de un string

* Podemos obtener cualquier caracter indivudual de una cadena de texto usando  su indice correspondiente dentro de  brackets []
* El valor del indice es un valor entero que inicia en 0














Aqui un ejemplo:
![string1](/imagenes/string1.png "tomado de:Charles Severance, Facultad de Información
de la Universidad de Michigan")













si no tenemos cuidado podemos cometer erronesm, como por ejeplo poner un indice que no corresponde.
```python

x = 'abc' # solo tiene 2 indices 0,1,2
print (c [5]) #este indice no existe arroja error
```





Para evitar estos errores, de salirnos la longitud de un indice, podemos preguntar primero cual es el la longitud de caracteres de un string, esto se hace con `len`
 
 >```python
 >fruta = 'banano'
 >print (len (fruta))
 >```
 >esto regresara 6 *oja no confundir con el indice*, `banana tiene 5 indices`, pero el largo de su cadena es de `longitud = 6`


|b|a|n|a|n|o||
|-|-|-|-|-|-|-|
|0|1|2|3|4|5|= 6|

lo mas recomendable a la hora de recorrer una cadena es utilizar el bucle `for`, aunque tambien se puede hacer con el bucle `while` pero este no es el recomendable

```python
#ejemplo con for
nombre = 'johan arley'
for nom in nombre :
    print (nom)
print ("la longitud de johan arley es: ",len (nombre))
```
```python
#ejemplo con while
nombre = 'johan arley'
indice = 0
while indice < len (nombre) :
    letra = nombre [indice]
    print (letra)
    indice = indice + 1
print ("la longitud de johan arley es: ",len (nombre))
#Arroja el mismo resultado que con el for
```
### Poniendo Limites a los strings
podemos  decirle a python que nos mueste solo una porcion del string por ejemplo del indice 0 al 4,
o del  4 al 8, esto dse hace con `[0:4]`

```python
#Poniendo Limites
nombre = 'johan arley'
print (nombre[0:5])
print (nombre[6:11])
```
```python
#Otra forma de Poner Limites
nombre = 'johan arley'
print (nombre[:5])# muestre los primeros 5
print (nombre[6:])#oculte los primeros 6, ó muestre del indice 6 en adelante
print (nombre [:])#muestre todo
```

## Manipulando Strings
### Concatenando
cuando se usa el signo + con strings, esto significa concatenar (unir)

```python
a = 'hola'
b = a + ' ' + 'johan'
# Resultado: hola johan
```



### `in` como operador logico


en python in actua como un operador logico, cuando se trabaja con strings, in verifica si una letra, una palabra esta dentro de otro, este `in` retorna `true` ó `false` segun lo que encuentre.

```python
fruta = 'banano'
'n' in fruta
#Resultado:true
'm' in fruta
#Resultado:false
'nano' in fruta
#Resultado:true
```
### Comparando `strings`
el siguiente ejemplo  compara la palabras verificando la primera letra teniendo en cuenta el orden que esta en el alfabeto.
```python
word = 'banano'
if word == 'banano' :
    print ('All right, bananos .')
if word < 'banano' :
    print ('Your word, ' + word + ', comes before banano ')
elif word > 'banano' :
    print ('Your word,' + word + ', comes after banano')
else :
    print ('All right, bananos .')
```

### Libreria `String` de Python
python tiene una libreria de string con muchas funciones, que pueden ser invocadas para trabajar con strings segun la necesidad del programador

```python
greet = 'SIGNIFICA SALUDO'
minuscula = greet.lower()
print (minuscula)
print (minuscula.upper())
#resultado: significa saludo
#SIGNIFICA SALUDO
```
`upper()` y  `lower` no son las unicas funciones de la libreria de `strings` de python, [aqui ](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "Documentación python") se puede consultar mas mas funciones.

### Buscando `strings` con `find()`
find lo que hace es, encontrar el indice del laprimera letra del string que se pretende buscar.
ejemplo:
```python
nombre = 'raboncita'
buscar = nombre.find('bon')
print (buscar)
#Resultado:2 = es el indice donde esta bon
```
tambien puedo decirle a `find ()` desde que numero de indice quiero que inici la busqueda.
`find ('busca esto', 2 aportir de este indice)`.

Ejemplo: buscar un espacio apartir de el indice 2 ('b')
```python
nombre = 'rabonc ita'
buscar = nombre.find(' ',2)
print (buscar)
#resultado = 6 indice
```

### Buscar y reemplazar `strings` con `replace()`


Ejemplo: `replace ('palabra a reemplazar', 'reemplazo')`



```python
greet = 'Significa saludo'
remplazar = greet.replace('Significa','Traducción al español = ')
print (remplazar)  
#resultado: tradución al español = saludo
```
### Qutar los espacios en blanco de un `string`

* `lstrip()`, ls hace referencia a left j(izquierda), por lo tanto quita los espacos en blanco del lado izquierdo del  `string`.
* `rstrip()`,ls hace referencia a right (derecha), por lo tanto quita los espacos en blanco del lado derecho del  `string`.
* `strip`, elimina los espacios en blanco tanto de la derecha como de la izquierda.

Ejemplo:

```python
greet = '    *greet significa saludo*     '
print (greet)
print (greet.lstrip())
print (greet.rstrip())
print (greet.strip())
#Resultados:
#*greet significa saludo*     
#*greet significa saludo*     
#    *greet significa saludo*
#*greet significa saludo*
```
 
### Prefijos `startwith()`
cuando necesitamos saber si una cadena inicia con una letra especifica, o una palabra especifica, ó deseamos especificar si en cierto rango  de indices existe una palabra que inicie con un string spefifco, utilizamos
`starwith ('string  a buscaer',indice star,indice stop)`, el indice de star y stop no son necesarios, se pueden dejar sin parametrd y la busqueda iniciara desde el indice 0.

Ejemplo: es importante que el indice de star coincida para que retorne un true, de lo contrario retornará un false.



```python
parabra = 'es un bonito dia hoy domingo'
print (parabra.startswith('bonito',6,17))
#resultado: true
parabra = 'es un bonito dia hoy domingo'
print (parabra.startswith('bonito',5,17))
#resultado: false
```


### Análisis y extracción  

Ejemplo:



```python
datos = 'Escrito por johan.jimenez@perex.sern.us en febrero 15 de 2020'
inicio = datos.find ('@')
print (inicio)
fin = datos.find (' ',inicio)
print (fin)
terminal = datos [inicio +1 : fin]
print (terminal)
#Resultado:
#25
#39
#perex.sern.us
```
## Archivos

### Abriendo un archivo


Para abrir un archivo utilizamos la función `open()` de python. esta función retorna in "file handle", es como un identificar, nos prepara el archivo correpondiente, para luego 
ser leido.




![archivo1](imagenes/archivo1.png "tomado de:Charles Severance, Facultad de Información
de la Universidad de Michigan")


un handle es un intermediario, que nos permite, abrir, leer, escribir y cerrar el archivo de texto que queremos manipular.

```python
archivo = open ('texto.txt')
print (archivo)
#Respuesta: <_io.TextIOWrapper name='texto.#txt' mode='r' encoding='UTF-8'>
```
cuando python no encuentra el archivo correctamente el programa se detiene, hay que tener cuidado con esto, para que no se detenga la ejecución del programa.

Es muy importarte recordar que un un documento en texto plano trae varias linenas, que invisible para nosotros se represetan con un `\n`,  estos 2 caracteres cuntan como caracteres en `len(\n) = 1`.

![archivo2](imagenes/archivo2.png "tomado de:Charles Severance, Facultad de Información
de la Universidad de Michigan")

### Mostrando el contenido de un archivo
como se habia dicho anteriormente, lo primero es pedir el handler
`archivo = open ('direcion/archivo.txt')`
seguidamente mostrar las lineas del archivo con un for: 


```python
contar = 0
for miarchivo in archivo :
    contar = contar + 1 #para contar las lineas
    print (miarchivo) # muestra el contenido de cada linea del archivo
print ('total de lineas = ', contar)
```
hay una función que me permite ver el contenido de un archivo sin necesidad de usar un for `read()` este no muestra los saltos de linea

ejemplo:

```python
file = open ('texto.txt')
archivo = file.read()
print (archivo)
print('el toral de caracteres es de: ',len(archivo))
#resultado:
#hola esta es la primera linea
#esta es la segunda linea
#esta es la tercera linea
#el toral de caracteres es de:  79
```
### Buscar atravez de un archivo

```python
file = open ('texto.txt')
for line in file :
    line = line.rstrip()
    if line.startswith('de') :
         print (line)
```

### Otra forma de busqueda en un archivo

```python
file = open ('texto.txt')
for line in file :
    line = line.rstrip()
    if not line.startswith('de') : #me confunde un poco pero arroja la misma consulta del anterior
        continue
    print (line)
```

### Solicitud de nombre de archivo
El siguiente ejemplo pide al usuario que ingrese el nombre del archivo, del cual se obtendrá si en ella hay una linas que inicien con la palabra ausunto, y ademos muestra la linea en la que esta esta palabra
```python
fname = input ('Ingrese nombre de archivo: ')
fhand = open(fname)
lines = 0
count = 0
for line in fhand :
    lines = lines + 1
    if line.startswith('asunto:') :   
        count = count + 1
        lineas = lines       
print ('There were', count, 'lineas de asunto en',fname,'y esta en la linea :',lineas)
#Resultado:There were 1 lineas de asunto en texto.txt en la lines numero: 5
```
### Solicitud de nombre de archivo de una forma mas profesional.


```python
fname = input ('Ingrese nombre de archivo: ')
try:
    fhand = open(fname)
except:
    print ('file cannot opened: ',fname)
    quit()
lines = 0
count = 0
for line in fhand :
    lines = lines + 1
    if line.startswith('asunto:') :   
        count = count + 1
        lineas = lines       
print ('There were', count, 'lineas de asunto en',fname,'y esta en la linea :',lineas)
```
## listas en python



las listas de datos, hacen parte de lo que se llama la `Estructura de datos`, que no es mas que un camino de organización de datos en una computadora. son formas conplejas de usar la memoria de un computador.

 * colecciones: donde tenemos mas de un valor en una variable
 * lo que no es una colección:
>```python
>x = 2
>x = 4
>print (x)
>```
>El codigo anterior no es una coleción,trata de confundirnos los diferentes valores que toma x pero es en un mismo instante.

### Listas
una lista es un tipo colección, es decir, en una sola variable  podemos tener mas de una cosa, son lo que normalmente en otros leguajes llamamos arrays.

```python
friends = ['el loco', 'espinosa', 'la maldita ranga']
otros = ['socks','calcetines','camisetas']
```


### Listasa de constantes

las constantes de una lista estan entre corchetes, y los elementos de las listas se ponen separados por comas
un elemento de una lista puede ser cualquier OBJETO de python, incluso un elemento puede ser una lista (una lista anidada dentro de un elemento)

Una lista tanbien puede estar vacia.

Unos ejemplos:
```python
print ([1, 23, 89 ])
#[1, 23, 89]
print (['red', 'rojo', 'yellow'])
#['red', 'rojo', 'yellow']
print (['red', 34, 98.4])
#['red',34,98.4]
print ([1, [5,6],7])
#[1,[5,6],7] - es una lista anidada en un elemento
print ([])
#[]
```
### Trabajando con listas


```python
friends = ['el loco', 'espinosa', 'la maldita ranga']
for amigos in friends :
    print ('Hola jovenes: ',amigos)
print ('terminado')

```
### Mirando dentro de una lista

esto ocurre cuando queremos ver un elemento especifico dentro de una lista, para esto utilizamos su Indice, estos iniciaan a contar desde 0, 1, 2 .....


```python
friends = ['castañeda', 'esinosa', 'loco']
print (friends [1])
#espinosa
```

### Las listas son mutables (se pueden cambiar sus elementos)


A comparación con las listas, los strings no son mutables, no se pueden cambiar su contenido

Ejemplo:

```python
fruit = 'Banana'
fruit [0] = 'b'
#esto arroja un errot
nun = [2,55,66,73]
print (num)
#[2,55,66,73]
num [2] = 90 # se cambia el valor del indice 2
print (num)
#[2,55,90,73]
```


### Como saber la longitud de  una lista?

```python
greet = 'Hola greet significa saludo'
print (len (greet))
#27 caracteres

x = [1, 2, 'johan', 88]
print (len (x))
#4
```
### Usando la Función `Range`
El tipo range() con un único argumento se escribe `range(n)` y crea una lista inmutable de n números enteros consecutivos que empieza en `0` y acaba en `n - 1.`

Para ver los valores del `range()`, es necesario convertirlo a lista mediante la función `list()`.
>https://www.mclibre.org/consultar/python/lecciones/python-range.html

Ejemplo:
```python
x = range (4)
print (x)
#ange(0, 4)
print (list (x))
#[0, 1, 2, 3]
friends = ['castañeda', 'esinosa', 'loco']
print (len(friends))
#3
print (list (range(len(friends))))
#[0, 1, 2]
```
### Concatenando listas con `+`
Podemos crear una nueva lista agregando  una lista ya creada ( sumando 2 listas)


```python
a = [1,2,4]
b = [5,6,7]
c = a + b
print (a)
#[1, 2, 4]
print (c)
#[1, 2, 4, 5, 6, 7]
```


Tambien podemos ver una lista por partes
No tiene en cuenta el segundo numero algo asi como `[x,n-1]`
```python
 t = [5,7,0,34,67,29]
 t[1:3]
 #[7,0]
 t[:4]
 #[5,7,0,34]
 t[3:]
 #[34,67,29]
t[:]
#[5,7,0,34,67,29]
```
### Metodo `list()`
el metodo `list()` crea una lista vacia,y se puede iniciar a llenerla  con  el metodo `append()`

```python
stuff = list () #se crea una lista vacia
stuff.append ('book')
stuff.append(99)
print (stuff)
#['book',99]
stuff.append('cookie')
print (stuff)
#['book',99,'cookie']
```

el metodo sppend(), agrega un elemto a la lista pero  al FINAL de la misma.

Ejercicio aplicando listas.
sacar el promedio de una lista de numeros ingresados. para salir del bucle el usuario debe introducir la palabra `done`

Ejemplo sin Utilizar listas:

```python
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
```

Ejemplo utilizando listas:

```python
listnum = list()
while True : 
     num = input ('Ingresa un numero: ')
     if num == 'done' : break
     valor = float (num)
     listnum.append(valor)
promedio = sum(listnum) / len(listnum)
print ('el promedio es:', promedio)
```
### Funciones que se usan con las listas
* `list.sort(reverse=True|False, key=myFunc)`: El sort()método ordena la lista de forma ascendente por defecto.
También puede realizar una función para decidir los criterios de clasificación.
```python  
#Organizando listas (por defecto)
  
cars = ['Ford', 'BMW', 'Volvo']
lista = cars.sort()
print (cars)
#['BMW', 'Ford', 'Volvo']
```
```python
# Organizando listas (reverse de mayor a menor)
   
cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)
print (cars)
#['Volvo', 'Ford', 'BMW']
```

```python
#Organizando listas con nuestro criterio (longitud de sus elementos)

def myFunc(e):
  return len(e)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc)
print (cars)
#['VW', 'BMW', 'Ford', 'Mitsubishi']
```


```python
# Organizando listas con nuestro criterio (longitud de sus elementos) de mayor a menor

def myFunc(e):
  return len(e)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(reverse=True, key=myFunc)
print (cars)
#['Mitsubishi', 'Ford', 'BMW', 'VW']
```
* la función `max()` regresa el valor mas grande
```python
num = [3,5,7,8,9,10]
print (max(num))
# 10
```

* la función `min()` regresa el valor mas pequeño

```python
num = [3,5,7,8,9,10]
print (min(num))
# 10
``` 

* la función `sum()` suma los elementos en una lista y regresa el resultado

```python
num = [3,5,7,8,9,10]
print (sum(num))
# 42
```

## Trabajando con  strings y List `string.split(separator, maxsplit)`
una de las primeras funciones útiles para trabajar con `strings` y `list()` es la función `split()`, que nos permite dividir una cadena de texto en una lista(cada palabra es un elemento de la lista).
* se sede definir el separador, pero por defecto  es cualquier espacio en blanco.
```python
txt = "welcome to the jungle"
x = txt.split()
print(x)
#['welcome', 'to', 'the', 'jungle']
```
* se define el separador ","
```python
txt = "hello, my name is Peter, I am 26 years old"
x = txt.split(", ")
print (x)
#['hello', 'my name is pedro', 'I am 43years old']
```

* tambien se puede especificar en  cuentos elementos se quiere dividir la lista `maxsplit(n+1)`
  
```python
txt = "apple#banana#cherry#orange
x = txt.split("#", 1)
print(x)
#['apple', 'banana#cherry#orange']
```
Ejercicio:
```python
#sacar el host de "johan.jimenez@gmail.com.co domingo 05 de abril a las 22:05 horas"
# esta es mi forma de hacerlo

file = open ('texto.txt')
texto = file.read()
x = texto.split("\n")
primer = x[0].split()
correo = primer[1].split('@')
host = correo[1]
print (host)
#gmail.com.co
```
## Diccinarios
los diccionarios son otro tipo de colleciones (como las listas). los diccionaros son las colecciones mas importantes de python.

en los diccionarios se manejan etiquetas, (un nombre identificativo para un elemento).
*par de  valores clave para cada elemento*

Entonces, todos lo elementos dentro de un diccionario tiene una clave  un valor.

son como una base de datos bebes (valor clave). os diccionarios en python son como los arrys asociativos en php

```python
maleta = dict()
maleta ['dinero'] = 50000
maleta ['dulces'] = 10
maleta ['camisas'] = 4
print (maleta)
#{'dinero': 50000, 'dulces': 10, 'camisas': 4}
print (maleta['dulces'])
#10
maleta ['dulces'] = maleta ['dulces'] + 2
print (maleta)
#{'dinero': 50000, 'dulces': 12, 'camisas': 4}
```


haciendo una comparación con las listas, podemos observar la siguiente imagen.










![Diccionario1](imagenes/diccionario1.png "tomado de:Charles Severance, Facultad de Información
de la Universidad de Michigan")

tambien se pueden crear diccionarios sin la funcion `dict()`.
ejemplo:
```python
diccionario = {'nombre' : 'johan', 'edad': 29, 'estado civil': 'soltero'}
print (diccionario)
#{'nombre': 'johan', 'edad': 29, 'estado civil': 'soltero'}
print (diccionario['nombre'])
#johan
diccionario_vacio = {}
```
Un uso común de los diccionarios es contar con qué frecuencia "vemos" algo

```python
count = dict ()
names = ['johan', 'jessi','johan','yeison','jessi']
for name in names :
    if name not in count : #  si no esta en entra
        count[name] = 1
    else :
        count [name ] = count[name] + 1
print (count)
#{'johan': 2, 'jessi': 2, 'yeison': 1}
``` 
### Metodo get en Diccionarios
El `get()` método devuelve el valor del elemento con la clave especificada.

`dictionary.get(keyname, value)`
keyname:Necesario. El nombre clave del elemento del que desea devolver el valor.

value:Opcional. Un valor a devolver si la clave especificada no existe.
Valor predeterminado Ninguno

```python
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")
print(x)
#Mustang
```

ejemplo: contar con qué frecuencia "vemos" algo con `get()`
```python
counts = dict ()
names = ['johan', 'jessi','johan','yeison','jessi']
for name in names :
    print (counts.get(name,0))
    counts[name] = counts.get(name,0) + 1
print (counts)
#{'johan': 2, 'jessi': 2, 'yeison': 1}
```

## Diccionarios y archivos
Ejemplo 1:


```python
palabras = {'computador' : 3, 'mesa' : 1, 'fuente' : 4}
for key in palabras :
    print (key,palabras[key])
#computador 3
#mesa 1
#fuente 4
```
Ejemplo 2:Recuperanso la lista de claves y valores
de un diccionario se pueden recuperar los elementos de varias formas:

* una lista de claves
* una lista de valores
* una lista de items (llave , valor en tuplas)

```python
goles = {'johan' : 2 , 'yeison ' : 4, 'mateo': 3}
print (list (goles)) 
#['johan', 'yeison ', 'mateo'] 
#  
print (goles.keys()) 
#dict_keys(['johan', 'yeison ', 'mateo'])

print (goles.values())
#dict_values([2, 4, 3])

print (goles.items())
#dict_items([('johan', 2), ('yeison ', 4), ('mateo', 3)])
```
### Variables de 2 iteraciones

```python
goles = {'johan' : 2 , 'yeison ' : 4, 'mateo': 3}
for key, value in goles.items() :
    print (key, value)
#johan 2
#yeison  4
#mateo 3
```
Ejemplo practico de archivos y diccionarios, 
retorna la palabra que mas se prepite en un archivo.
```python
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
```
## Tuplas
 Una tupla es una colección ordenada e inmutable (es como una lista de constantes, por que sus valores no se pueden cambiar) .En Python, las tuplas se escriben entre corchetes.  

```python
tupla = ("apple", "banana", "cherry")
print(thistuple[-1]) #imprime el último elemento de al tupla
#cherry  
```
con las tuplas, al ser inmutables, no trabaja con las funciones `sort()`, `append()`, `reverse()`

Nota Importante: Como Python no tiene que construir estructuras de tuplas para poder modificarse, son más simples y eficientes en términos de uso de memoria y rendimiento que la lista.

así que en nuestro programa cuando hacemos "variables temporales" preferimos las tuplas sobre la lista

### Formas de asignar tuplas
```python
(x,y) = (4,'johan')
print (x)
#4
print(y)
#johan
```
### Tuplas y diccionarios
el metodo `intems()` en diccionarios retorna una tupla de (llave, valor)

```python
ggoles = {'johan' : 2 , 'yeison ' : 4, 'mateo': 3}
tupla = goles.items()
print (tupla) 
#ict_items([('johan', 2), ('yeison ', 4), ('mateo', 3)])
```

### se pueden usar los operadores de comparación con tuplas
Los operadores de comparación trabajan con tuplas y otras secuencias. si el  primer elemento es igual, python pasa al siguiente elemento, y así sucesivamente, hasta que encuentra elementos que difieren.

```python
comp = (1,1,2) < (5,1,2) 
print (comp)
#True
comp = (1,1,2) < (6,1,2) 
print (comp)
#True
comp = ("joahn") < ("amor") 
print (comp)
#False
comp = ("amor","yeizon") < ("amor","z")
print (comp)
#True
```
### Organizando lista de tuplas
para organizar un diccionario, primero lo convertimos en tuplas con el metodo `items()` y luego organizamos estas listas de items con la función `sort()`.


```python
goles = {'johan' : 2 , 'yeison ' : 4, 'mateo': 3}
item = goles.items()
print (item)
#dict_items([('johan', 2), ('yeison ', 4), ('mateo', 3)])
lorganizado = sorted(item)
print (lorganizado)
#[('johan', 2), ('mateo', 3), ('yeison ', 4)]
```

Otra forma de hacer lo anterior:

```python 
goles = {'johan' : 2 , 'yeison ' : 4, 'mateo': 3}
orga = sorted (goles.item())
for name, goles in sorted(goles.items()) :
    print (name, goles)
    #[('johan', 2), ('mateo', 3), ('yeison ', 4)]
```

### Organizar por valores en lugar de clave
Normalmente cuando se usa sorted(), este lo organiza por las llaves (por orden alfabetico, numeros d emenor a mayor, etc), pero siempre utilizando la llave (key) , para organizarlo por los valores, la clave es cambiar de lugar la llave y el valor, y a funcion sorted () hará lo suyo.



```python
goles = {'johan' : 2 , 'yeison ' : 4, 'mateo': 3}
lista = list()
for nombre, gol in goles.items() :
    lista.append ((gol,nombre)) # esta es la clave se invierte goles y nombre
print (lista)
#(2, 'johan'), (4, 'yeison '), (3, 'mateo')]
lista = sorted (lista,reverse=True)
print (lista)
#[(4, 'yeison '), (3, 'mateo'), (2, 'johan')]
```

### Listas de comprención (listas simples)
`[(vretorno1,vretorno2) for i, x in dictonari.item() if i > algo]`

La listas de comprención las entiendo como una forma corta de representar (listas con for y condicionales).
un termino mas teorico es:

Las comprensiones de listas ofrecen una manera concisa de crear listas. Sus usos comunes son para hacer nuevas listas donde cada elemento es el resultado de algunas operaciones aplicadas a cada miembro de otra secuencia o iterable, o para crear una subsecuencia de esos elementos para satisfacer una condición determinada.

```python
c = {'a' : 3, 'r' : 5, 'g' : 4}
print (sorted([(v,k) for k,v in c.items()]))
#[(3, 'a'), (4, 'g'), (5, 'r')]
```

### Listas de comprención (listas anidadas)

```python
empleados = [['juan' , 5000 , 'ventas'], ['elena' , 6000 , 'ventas'], ['marcos' , 3400 , 'operario']]
resultado1 = [ (nombre,sueldo) for nombre,sueldo,area in empleados if area is not 'ventas']
print (resultado1)
#[('marcos', 3400)]
```

### Bonus

especie de matriz

```python
matriz = [[11,12,13],[21,22,23],[31,32,33]]
[[print(xdato) for xdato in fila ]for fila in matriz]
#lo primero que se ejecuta es el ultio forel de mas adentro
#for fila no regresa nada
#for x dato regresa xdato
#1
#12
#13
#21
#22
#23
#31
#32
#33
```

Ejercicio final:

imprmir desde un archivo las 10 letras mas reperidas de este mismo

```python
file = open('texto.txt')
conteo = dict()
#matriz = [line.split() for line in file ]
for line in file :
    matriz = line.split()
    for repeat in matriz :
        conteo [repeat] = conteo.get(repeat,0) +1
#print (conteo)

lista = list()
"""
for llave,valor in conteo.items() :
    tupla = (valor,llave)
    lista.append(tupla)
lista = sorted(lista, reverse=True)
for valor, key in lista[:10] : 
    print (key,valor)
"""
lista = sorted ([(valor, llave) for llave,valor in conteo.items()],reverse=True)
print (lista)
[print(key,valor) for valor,key in lista[:10]]
```






