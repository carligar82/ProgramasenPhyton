import numpy as np
import matplotlib.pyplot as plt
ejemplo_dir = 'C:/Users/Antonio/Desktop/Carlos' #Poner aqui directorio con plot2.txt
c=ejemplo_dir+"/plot2.txt"
v=np.loadtxt(c)
plt.plot(v[:,0],v[:,1],'g')
plt.title("Tráfico en la web por semana")
plt.xlabel("Semana")
plt.ylabel("Usuarios")
plt.xlim(1,750)
plt.ylim(0,6020)