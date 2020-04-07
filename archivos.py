#ver el contenido de un archivo
"""
file = open ('texto.txt')
contar = 0
print (file)
for mifile in file :
    contar = contar + 1
    print (mifile)
print ('total de lineas = ', contar)
"""

#leer todo el contenido de in archivo
"""
file = open ('texto.txt')
archivo = file.read()
print (archivo)
print('el toral de caracteres es de: ',len(archivo))
"""
# Buscar atravez de un archivo
"""
file = open ('texto.txt')
for line in file :
    line = line.rstrip()
    if line.startswith('de') :
         print (line)
"""
         
# Buscar atravez de un archivo, hace lo mismo que el anterior
"""
file = open ('texto.txt')
for line in file :
    line = line.rstrip()
    if not line.startswith('de') : #me confunde un poco
        continue
    print (line)
"""
# Solicitando el nombre del archivo
"""
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
"""
# Solicitando el nombre del archivo mas profesional
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
