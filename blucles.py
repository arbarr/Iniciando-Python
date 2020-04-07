
""" while True:
    linea = input ('>')
    if linea == 'terminado' :
        break
    print (linea)
print ('terminado  por break')

while True:
    linea = input ('>')
    if linea == 'terminado' :
        break
    print (linea)
print ('terminado  por break')
"""
 
"""
n = 0
b = 0
while True:
    n = n + 1 
    print (n ,' bucle' )    
    linea = input ('>')
    if linea [0] == '#' :
        b = b + 1 
        print (b,'continue' )
        continue
    if linea == 'terminado' : 
        break     
    print (linea)
    
print ('terminado  por break')   
"""

amigos = ['castañeda','loco', 'espinosa']
for ami in amigos :
    print ('Feliz cuarentena ',ami)
print ('fin del for')

# encontrar el numero mayor
_masgrande = -1
for numeros in [1,34,6,78,4,64,8,56] :
    if numeros > _masgrande :
        _masgrande = numeros
    print (_masgrande ,numeros)
print ('el numero mas grande es: ', _masgrande)
         