import os
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
ejemplo_dir = 'C:/Users/Antonio/Desktop/Carlos' #Poner aqui directotio de los archivos de datos
contenido = os.listdir(ejemplo_dir)
print ("Ficheros de datos disponibles:")
for fiche in contenido:
    if os.path.isfile(os.path.join(ejemplo_dir, fiche)) and fiche.endswith('.txt'):
            print(fiche)
print ("Escoge fichero con datos a ajustar:")
c=input()
fich=c
c=ejemplo_dir+"/"+c
v=np.loadtxt(c)
sx=0
sy=0
sxy=0
sx2=0
sy2=0
n=np.size(v)/2
for x in v:
    sx=sx+x[0]
    sy=sy+x[1]
    sxy=sxy+x[0]*x[1]
    sx2=sx2+x[0]*x[0]
    sy2=sy2+x[1]*x[1]
a=(n*sxy-sx*sy)/(n*sx2-sx*sx)
b=(sy-a*sx)/n
r2=((n*sxy-sx*sy)*(n*sxy-sx*sy))/((n*sx2-sx*sx)*(n*sy2-sy*sy))
r2=sqrt(r2)
print("El ajuste lineal de los datos en el fichero ",end="")
print(fich,end="")
print (" es:")
print("y=",end="")
if a!=1:
    print(format(a,'0.2f'),end="")
print("x",end="")
if b!=0:
    if b>0:
        print("+",end="")
    print(format(b,'0.2f'))
print ("Coeficiente de correlación: R=",end="")
print (format(r2,'0.2f'))
plt.plot(v[:,0],v[:,1],marker='o',linestyle='None',color='r')
plt.plot(v[:,0],a*v[:,0]+b,marker='None',linestyle='-',color='k')
plt.title("Ajuste de los datos")
plt.xlabel("Valores X")
plt.ylabel("Valores Y")
