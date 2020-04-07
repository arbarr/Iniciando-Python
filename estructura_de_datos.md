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