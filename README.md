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



