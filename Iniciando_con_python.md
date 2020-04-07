# Iniciando-Python
## Constantes
Aquellos valores numericos, strings que son fijos durante la ejecucion del programa
>Ejemplo:
> ```python
> print(123)
> print('Hello word')
> ```
## Palabras Reservadas
 Aquellas que son **Exclusivamente** utilizadas por Pyhon
>Algunas de ellass son:

|alse|class|return|is|finally |
|-----|-------|---|--|------- |
|none |if     |for|lambda| continue|
|true |def    |from|while| nonlocal|
|and |del    |global|not|with|
|as |elif     |try|or|yield|
|assert |else     |import|pass|break|
|except |in     |raise|| |

>*Scrips son varias lineas de codigoescritoe n python guardado en un  archivo con extencion .py*

## Variables
Es un espacio de memoria que se reserva en la computadora para guardar un dato, y cuyos valores pueden ser cambiados durante la ejecución del programa.Para identificar mas facilmente estos espacios de memoria se le asignan **Etiquetas**.

> ```pyhon
> x = 12.2
> y = 34
> x = 23 se sobreescribe
> ```
>##### **x** *es la etiqueta*
> 
> ##### **12.2** *es elvalor del dato*
> 
> #####  *todo junto se guarda en una posicion de memoria*

Reglas a tener en cuenta a la hora de nombrar Etiqetas a las variables:

  > Buenas:
  >* spam
  >* eggs
  >* spam23
  >* _speed
  >
  > Malas:
  >* 23spam
  >* #eggs
  >* spam.23
  >* _speed
  >
  > Son **Sensible a Mayusculas**. Las siguientes etiquetas son distintas:
  >* spam
  >* Spam
  >* SPAM

  Es muy importarnte que las etiquetas que se nombren tengan logica con el Dato o la funcion que va a desempeñar dentro del programa
  > Esto es un mal ejemplo
  >```python
  >asdfasdfashjkd = 123
  > erewwererw = asdfasdfashjkd + 45
  >print(erewwererw)
  >```
  > Esto es un Buen ejemplo
  >```python
  >Horas = 123
  > salario = Horas * 45
  >print(salario)
  >```

### Tipos de  variables:
En python no es necesario poner el tipo de variable a una etiqueta, pyhon desifra segun el dato, de que tipo es, aunque hay que tener ciertas precauciones.

>Python reconoce los tipos:
>```python
>x = 1 + 4
>print (x)
>salida = 5
>a = 'johan' + 'Arley'
>print (a)
>Salida = johan Arley
>```
>Operaciones prohibidas
>```python
>x = 'Johan' + 2
>!Error: y se detiene el programa
>```
>Puedo preguntarle a python cual es el tipo de varible con ` type ('hello')` esto regresará `< class 'srt'>`

No quiere decir que por que python entiende el tipo de variable de uaa etiqueta, estos tipos no existan, si existen y estos son uno de ellos

|Tipo|Ejemplo|
|----|-------|
|Entero| -14: 0: 12|
|Punto Flotante|-2.5: 0.0: 12.0|
   
## Declaracion de Asignación
La asignacion de hace por medio del operador `=`, todo aquello que este a su derecha, será asignado a la variable que este a su izquierda.

>Ejemplo
>```Python
> x = 3.9 * x * (1 - x)
>```
> Toda esta expresión *`3.9 * x * (1 - x)`* es asignada a la variable *`x`*

## Expresiones Numericas
### Operadores numericos
  
>|`Operador`|`Operación`|
>|:----------:|:-----------:|
>|+|Suma|
>-|Resta|
>|*|Multiplicación|
>|/|División|
>|**|Potencia|
>|%|Modulo|

 #### Orden de Evaluación de los Operadores Numericos (Precedencia de los Operadores):

>`x = 1 + (2 * 3) - (4 / (5 ** 6))`
>en este caso siempre se hace caso ar orden de agrupación de los parentesis, como se muestra a continuación.
>
> 1. ->  5 ** 6
> 2. ->  Item 1 / 4
> 3. ->  2 * 3
> 4. ->  Item 2 - Item 3  
> 5. -> 1 + item 4 
>
>Cuando **NO** se Utiliza los parentesis, el orden de precedencia de los operadores es el siguiete:
>
>* Potencia (**) ó Incremento (X+)
>* Multiplicación (*), Division (/), Modulo (%)
>* Suma (+) y Resta (-)
>* De Izquierda A Derecha
>
>Ejemplo:
>>
>>```python
>>x = 1 + 2 ** 3 / 4 * 5
>>print (x)
>> ```
>>1. ->  2 ** 3 = 8
>>2. ->  Item 1 / 4 = 2
>>3. ->  Item 2 * 5 = 10 
>>4. -> 1 + item 3 = 11 

Se pueden convertir tipos de variables o otros:
 >`print(float (99) + 100)`, convierte el resultado en flotante `199.0`
 >```python
 >i = 42
 >f = float (i)
 >Resultado: 42.0
 >```

 Conversión de cadenas de taxto: la mayoria de datos estaen en cadenas de texto, cuando los importamos desde otro fichero, al llamarlos desde una base de datos, entre otros, por esto es necesario convertirlos a otro tipos de datos segun la necesidad.

 >
 >```python
 >Svalor = '123'
 >Ivalor = 1
 >#para sumar estos 2 valores debo convertir el Svalor a Entero ojo sin espacios
 >Csvalor = int (Svalor)
 >print (Csvalor + 1)
 ># = 124
 >
 >```
 >


 NOTA: uno de los grandes cambios de python 2 a python 3 es la divicion de enteros:

 >python 2
 >```python
 >print (10 / 2)
 >=5
 >print (9 / 2)
 >= 4 #se come los decimales, por que al inicio no se pusieron los decimales
 >print (99 / 100)
 >= 0 # se come los decimales
 >print (10.0 / 2.0)
 >= 5.0
 >print (99.0 / 100.0)
 >= 0.99 # como se pusieron decimales en la >operacion, en el resultado se muesta con los >puntos decimas
 >```
 >*En python 3 **NO** es necesario poner las constantes o variasles como flotataes en una operacion de divición para que me arroje flotantes, solo basta con poner cualquier numero sea entero o flotante y python3 me dara el resultado sienpre con puntos decimales.*
 >```python
 >print (10 / 2)
 >=5.0
 >print (9 / 2)
 >= 4.5 # No se come los decimales, por que al inicio no se pusieron los decimales
 >print (99 / 100)
 >= 0.99 # No se come los decimales
 >print (10.0 / 2.0)
 >= 5.0
 >print (99.0 / 100.0)
 >= 0.99 # 
 >```

Para obtener datos del mundo exterior se utiliza la funcion Input, este siempre retorna un string
>```python
>nonbre = input ('Quien eres?')
>print('Bienvenido',nombre)
>#las sadida es:
>#Quien eres? johan
>#Bienvenido: johan
>```
---
## Operadores de comparación  

|`Python`|`Significado`|
|:----:|:-------:|
|<| Menor que|
|<= |Menor o igual que|
|==|Igual a|
|>=|myor o Igual a|
|>|Mayor que|
|!=|Diferente a|


## Condicionales 
## IF

>Ejemplo de uso de los operadores de compraracón con IF
>```python
> x = 5
> if x > 4 :
>   print ('mayor que 4')
> if x >= 5 :
>   print ('mayor o igual a 5')
> if x < 6 :
>   print ('menor que 6')
> if x <= 5 :
>   print ('Menor o igual a 5')
> if x != 6 :
>   print ('diferente a 6')
>```

## Indentación
la indentación es muy importante en python, es el equivalente a la llaves{} en java, o en c, agupa bloques de codigo, cambia el flujo de ejecución. 
    
***Importante, siempre usar los mismos espacios para la indentación, o de usa tab, o se usa espacios.python sabe cuando se utiliza tab y espacios. (esto lo suluciona los editores de texto como vs. atom etc. ellos lo hacen automatimamente cuando de pone la extención .py), pero si no los tienes es mejor utilizar espacios.***

### ELSE
hay 2 caminos para las desiciones, esto en python se logra con la combinación de if y else, que pasa si o de lo contrario haga otra cosa.

>Este es un ejemplo:
>```python
>x = 4
>if x > 2 :
>  print ('numero grande')
>else :
>  print ('numero pequeño')
>print ('aqui termina el if else')
>```

### Multipes caminos
solo recorre un solo camino, el que cumpla y listo. y el ultimo es el else que es por si ninguno cumple; pero como se dijo anteriormente solo ealua una de los muchos caminos y luego sale.

>```python
>x = 4
>if x < 2 :
>  print ('numero pequenño')
>elif x  < 10  :
>  print ('numero mediano')
> else :
>  print ('numero grande')
>print ('aqui termina el if else')
>```
>No es necesario poner el else, igual siempre el codigo seguira si no se pone.(trata que tu else no sea irrelevante, que sea logico ponerlo)

### Puedo tener varios elif
pero como siempre, encuentra la coincidencia y sale de los demas elif

>```python
>x = 4
>if x < 2 :
>  print ('numero pequenño')
>elif x  < 10  :
>  print ('numero mediano')
>elif x  < 20  :
>  print ('numero grande')
> else :
>  print ('numero grande')
>print ('aqui termina el if else')
>```
>solo se imprimirá numero mediano y saldrá

### Estructura "try" "except"
la idea de esto, es cuando tenenos un codigo y sabemos que por algura razon puede fallar; esto nos permite que el codigo no explote, se detenga y termine la ejecución, si no mas bien le damos algo que hacer cuando algo salga mal.

* Si el código en try funciona – except es omitido
* Si el código en try falla – pasa a la sección except 

>el siguiente es un codigo que va a fallar en la linea 2, como no tiene el try except el programa se detendra su ejecucion, sin que las otras linea de codigo se ejecuten
>```python
> $ cat notry.py
>astr = 'Hola Bob'
>istr = int(astr)
>print('Primero', istr)
>astr = '123'
>istr = int(astr)
>print('Segundo', istr)
>```

>Ejemplo en try except
>```python
>astr = 'Hola Bob'
>try:
>    istr = int(astr)
>except:
>    istr = -1
>print('Primero', istr)
>astr = '123'
>try:
>    istr = int(astr)
>except:
>    istr = -1
>print('Segundo', istr)


### Patrones de compartamiento
> Pasos secuenciales
> ```python
> x = 2
> print (x)
> x = x + 2
> print (x) 
> ```

>Pasos condicionales `if`
>```python
>x = 5
>if x < 10:
>   print ('Pequeño')
> if x > 20:
>   print('Grande')
> print ('Fin')

>Ciclos `while`
>```python
>print('Lo siguiente es un while')
>n = 5
>while n > 0 :
>    print (n)
>    n = n - 1
>print('salí del while\n')
---

## Comentarios
Es muy importarnte poner comentarios en nuestro codigo, esto nos ayuda a la documentación del mismo
y anuestro futuro yo.

`#un comentario en python inicia con #`

## Primer programa
todo programa en python contiene una  **Enetrada**, un **Procesamieto**, y genera una **Salida*.

```python
#Convertidor de pisos de un ascensor
inp = input ('Piso Eurpeo?')
usf = int(inp) + 1
print ('Piso equivalente USA', usf)
```
## Funciones
* las funciones de hacen con el fin de reutilizar el codigo lo mas que se pueda. si tenemos patrones repetitivos, hacemos funciones.
* En Python una función es un código reutilizable que toma argumentos(s) como input, realiza algunos cálculos y luego devuelve uno o más resultado(s).
* Para definir una función utilizamos la palabra reservada def.
* Llamamos/Invocamos a la función utilizando una expresión que contenga el nombre de la función, paréntesis y argumentos

>El siguiente es un ejempolo de declaracion y llamado de una función
>```python
>def objeto(): #con def de declara una función
>    print('Hola')
>>print('Diversión')
>objeto() #con el nombre de la funcion se llama la misma
>print('Zip')
>objeto()
>```

Las funciones en python las haY de 2 tipos

1. Funciones incorporadas, que son parte de python, y se identifican con palabras reservadas del lenguaje `print(), type(),float(),init().`
2. Funciones que nosotros definimos, y despues que las definimos, se convierten como un nuvo tipo de palabra reservada. ***es decirlas tratamos como palabras reservadas, no les damos estos nombres a variables dentro el programa***

el siguiente ejemplo de la función max, que recibe como argumento una caden ade texto, y regresa la letra mas alta del alfabeto. en la siguiete imagen podemos ver su comportamiento.



![Funcion1](/imagenes/funcion1.png "tomado de:Charles Severance, Facultad de Información
de la Universidad de Michigan")





![Funcion1](/imagenes/funcion2.png "tomado de:Charles Severance, Facultad de Información
de la Universidad de Michigan")








![Funcion1](/imagenes/funcion3.png "tomado de:Charles Severance, Facultad de Información
de la Universidad de Michigan")

Una vez que hemos definido una función, podemos llamarla (o
invocarla) todas las veces que queramos
Este es el patrón almacenar y reutilizar

### Argumentos de una función
* Un argumento es un valor que informamos a la función como su entrada (input) cuando llamamos a la función
* Utilizamos argumentos para poder instruir a la función que realice diferentes tareas cuando la llamamos en diferentes oportunidades
* Colocamos los argumentos entre paréntesis luego del nombre de la función (no es una variable es un dato concreto)

>`grande = max('Hola mundo')`
### Parametros
Un parámetro es una variable que utilizamos en la función definition (definición). Es una “handle” (palanca) que permite al código de la función
acceder a los argumentos para invocar una función en particular.(si es una variable)

>```python
> def saludo(lang):
>   if lang == 'es':
>       print('Hola')
>   elif lang == 'fr':
>       print('Bonjour')
>   else:
>       print('Hello')
>
>   >>> saludo ('en')
>   Hello
>   >>> saludo ('es')
>   Hola
>   >>> saludo ('fr')
>   Bonjour
>```

### Valores de Retorno
A menudo, una función tomará sus argumentos, hará algunos cálculos, y retornará un valor que se usará como el valor de la llamada de la función en la expresión de llamada. La palabra clave return (retorno) se utiliza para esto.

>```python
>def saludo ():
>   return "Hola"
> 
>print(saludo (), "Glenn")# Hola Glenn
>print(saludo (), "Sally")#Hola Sally
>```

El enunciado return termina la ejecución de la función y “devuelve” el resultado de la
función
>```python
> def saludo (lang):
>   if lang == 'es':
>       return 'Hola'
>   elif lang == 'fr':
>       return 'Bonjour'
>   else:
>       return 'Hello'
>
>>>> print(saludo ('en'),'Glenn')
>Hello Glenn
>>>> print(saludo ('es'),'Sally')
>Hola Sally
>>>>print(saludo ('fr'),'Michael')
>Bonjour Michael
>``` 

### Multiples parametros y argumentos
* Podemos definir más de un parámetro en la definición de la función
* Simplemente agregamos más argumentos cuando llamamos a la función
* ***Hacemos coincidir el número y orden de los argumentos y parámetros***
>```python
>def addtwo(a, b):
>   agregado = a + b
>   return agregado
>x = addtwo(3, 5)
>print(x)
>8
>```


# Bucles
Los bucles (pasos repetidos) tienen variables de iteración que cambian cada vez a través del bucle. 
## Bucles Indefinidos `while`
Los bucles while se llaman “bucles indefinidos” porque continúan hasta que una condición lógica se vuelve False (Falsa)

A menudo, estas variables de iteración atraviesan una secuencia de números. su "Bandera (ó condición logica) de terninación es n-1"

>```python
>n = 5
>while n > 0 :
>   print (n)
>   n = n – 1
>print( 'fin del while')
>print (n)
>```
### Bucles infinitos
son blucles que nunca van a terninar, ya que su "Bandera de terninación" no esta definida.

>```python
>n = 5
>while n > 0 :
>   print ('Enjabonar')
>   print ('Enjuagar')
>print('Secar')
>```
>el codigo anterior siempre imprimirá enjabonar,enjuagar.

### Bucle que nunca se ejecutará
>```python
>n = 0
>while n > 0 :
>   print ('Enjabonar')
>   print ('Enjuagar')
>print('Secar')
>```


### Romper un bucle `Break`
El enunciado break (romper) termina el bucle actual y salta al enunciado que le sigue  inmediatamente al bucle.

Es como una prueba de bucle que puede suceder en cualquier lado en el cuerpo del bucle


>```python
>while True:
>    linea = input ('>')
>    if linea == 'terminado' :
>        break
>   print (linea)
>print ('terminado  por break')
>```
> Al escribir en el terminal  `terminado` inmediatamente se ejecuta el `break` y sale del while.

### Finalizar una Iteración `Continue`

El enunciado continue (continuar) termina la iteración actual y salta a la parte superior del bucle y comienza la siguiente iteración.


>```python
>n = 0
>b = 0
>while True:
>    n = n + 1 
>    print (n ,' bucle' )    
>    linea = input ('>')
>    if linea [0] == '#' :
>        b = b + 1 
>        print (b,'continue' )
>        continue
>    if linea == 'terminado' : 
>        break     
>    print (linea)
>   
>print ('terminado  por break')   
>```

## Bucles definidos
### Bucle `For`
* Estos bucles se denominan “bucles definidos” porque se ejecutan una cantidad exacta de veces.

* Con bastante frecuencia tenemos una lista de los ítems de las líneas en un archivo, es decir un conjunto finito de cosas.
  

* Podemos escribir un bucle para ejecutar el bucle una vez para cada uno de los ítems de un conjunto utilizando la secuencia for de Python 
  

* Decimos que los “bucles definidos iteran a través de los miembros de un conjunto”


### Bucle definido Simple

>```python
>for i in [5, 4, 3, 2, 1] :
>   print(i)
>print('Fin del for')
>```
>Resultado
>* 5
>* 4
>* 3
>* 2
>* 1
>* Fin del for
>
>* i es una varible de iteración, que cambian cada vez a través del bucle. Estas variables de iteración se mueven a través del conjunto o secuencia
>* El bloque (cuerpo) del código se ejecuta una vez
para cada valor in de la secuencia

>* La variable de iteración se mueve a través de todos los valores in de la secuencia








![bucle1](/imagenes/bucles1.png "tomado de:Charles Severance, Facultad de Información
de la Universidad de Michigan")








### Bucle definido con cadenas

>```python
>amigos = ['castañeda', 'loco', 'espinosa']
>for ami in amigos :
>   print('Feliz cuarentena',ami)
>print('Fin del for')
>```
>Resultado
>* Feliz cuarentena  castañeda
>* Feliz cuarentena  loco
>* Feliz cuarentena  espinosa
>* fin del for
>* Fin del for





Utilizar los bucles para algo inteeligente
>```python
>_masgrande = -1
>for numeros in [1,34,6,78,4,64,8,56] :
>    if numeros > _masgrande :
>        _masgrande = numeros
>    print (_masgrande ,numeros)
>print ('el numero mas grande es: ', _masgrande)
 >        
>```
operador `i`s es como el == pero mas estricto en el tipo de datoa comparar
>```python
> >>>1 is 1.
>False
> >>>a, b = 1, 1
> >>>a is b
>True
>```

el operador `is not ` es un operador logico y mas  estricto que `!=`.