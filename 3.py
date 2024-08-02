#Importamos el módulo sys para el uso de la salida y entrada estándar
import sys
for line in sys.stdin: #Entendemos cada línea como un cadena de texto terminada en \n
    line = line.strip() #Eliminamos los espacios en blanco 
    line = line.lower() #Ponemos todas las palabras en minúsculas
    words = line.split() #Divide la línea en palabras
    for word in words:
        i=0 #Variable contador
	#Escribimos el resultado en la salida estandar
	#El resultado obtenido en la salida será la entrada del código reduce
        for let in word:
		#Para cada vocal (que convertimos en la clave), se asigna el valor 1 y se imprime el par
		#clave-valor en una única línea separadas por un tabuldor.
           if ((word[i]=='a') or (word[i]=='e') or (word[i]=='i') or (word[i]=='o') or (word[i]=='u')):
               print ("%s\t%s" % (word[i], 1))
           i=i+1
#módulo con las operaciones definidas para objetos iterables 
#(nos permitirá por ejemplo contar el número de elementos)
from operator import itemgetter  

current_word = None
current_count = 0
word = None
print ("Vocales incluidas en el texto:")
#leemos de la entrada estandar
for line in sys.stdin:
    line = line.strip() #eliminamos los espacios
	#Dividimos la línea (que obtenemos de la salida de mapper.py)
	#en pares clave-valor (word, count), teniendo en cuenta que 
	#el delimitador es en este caso el tabulador
    word, count = line.split('\t', 1) 
	#este if funciona porque Hadoop ordena la salida del código mapper.py
	#por la clave (en este caso palabras) antes de pasarlo como entrada del
	#código reducer.py, de manera que todas las palabras iguales aparecerán seguidas
    if(current_word == word):
        current_count += int(count) #hacemos casting sobre count pues almacenaba un tipo caracter
    else:
        if current_word:  
            print ("%s\t%s" % (current_word, current_count),end="")
            if current_count=="1":
                print (" vez")
            else:
                print (" veces")
        current_count = int(count)
        current_word = word
		
#no debemos olvidar incluir la última palabra
if current_word == word:
	print ("%s\t%s" % (current_word, current_count),end="")
if current_count=="1":
    print (" vez")
else:
    print (" veces")	

