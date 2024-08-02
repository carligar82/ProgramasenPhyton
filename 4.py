import pandas as pd #Importamos las biblitecas
import matplotlib.pyplot as plt
# Creamos 2 dataframes a partir de la tabla excel, una con los partidos políticos y otra sin ellos.
tabla='C:/Users/Antonio/.spyder-py3/02_201606_1.xlsx'
xls_congreso = pd.read_excel(tabla,header=None,skiprows=4)
xls_congreso2 = pd.read_excel(tabla,skiprows=5)
arr = xls_congreso.iloc[0] #Creamos un vector con los partidos
x=arr.values
#Averiguamos a partir de que indice en el vector de partidos hay valores no nulos
ind=0
ind2=0
for i in x:
    if pd.isnull(i)==False: 
        if ind2 == 0:
            ind2=1
            nn=ind   
    ind=ind+1
arr = xls_congreso.iloc[1]
x=arr.values
a=0
for i in x:
    if a>=nn:
        #Creamos un dataframe de los valores a representar y los agrupamos por comunidades
        print ()
        print (i,":")
        ComunidadP=xls_congreso2
        ComunidadP[i]=xls_congreso2.iloc[:,a]
        PorComunidad=ComunidadP.groupby(['Nombre de Comunidad'])[['Total votantes',i]].sum()
        PorComunidad ["% Voto"]=PorComunidad[i]/PorComunidad["Total votantes"]*100
        #Ordenamos por porcentaje de votos de mayor a menor para presentarlos
        PorOrdenComunidad=PorComunidad.sort_values(by=["% Voto"],ascending=[False])
        print (PorOrdenComunidad)
        t="Votos "+i+" por Comunidad Autónoma"
        Barras=PorOrdenComunidad["% Voto"].plot (kind='bar',title=t)
        Barras.set (xlabel='Comunidad Autónoma',ylabel='% Votos')
        plt.show()
        print ("Pulsa INTRO para seguir ",end="")
        input()
    a=a+1
#Creamos Dataframe ordenado de mayor a menor con la prticipación en cada provincia
Participacion=xls_congreso2.groupby(['Nombre de Provincia'])[['Total censo electoral','Total votantes']].sum()
Participacion ["% Voto"]=Participacion['Total votantes']/Participacion["Total censo electoral"]*100
ParticipacionOrden=Participacion.sort_values(by=["% Voto"],ascending=[False])
#Lo mostramos,además de indicar la de participación mayor
arr=ParticipacionOrden.iloc[0]
x=arr.values
print (ParticipacionOrden)
print()
print ("La provincia con mayor participación (",end="")
print (format(x[2],'0.2f'),"%) ha sido ",end="")
print (arr.name)
# Creamos 2 dataframes a partir de la tabla excel, una con los partidos políticos y otra sin ellos.
tabla='C:/Users/Antonio/.spyder-py3/PROV_02_201606_1.xlsx'
xls_congreso = pd.read_excel(tabla,header=None,skiprows=4)
xls_congreso2 = pd.read_excel(tabla,skiprows=5)
arr = xls_congreso.iloc[0] #Creamos un vector con los partidos
x=arr.values
#Averiguamos a partir de que indice en el vector de partidos hay valores no nulos
ind=0
ind2=0
for i in x:
    if pd.isnull(i)==False: 
        if ind2 == 0:
            ind2=1
            nn=ind   
    ind=ind+1
for i in x:
    if pd.isnull(i)==False:
        #Creamos un dataframe de los valores a estudiar, hacemos los cálculos y
        #los escribimos para cada partido
        print ()
        print (i,":")
        ComunidadP=xls_congreso2
        ComunidadP[i]=xls_congreso2.iloc[:,nn]
        ComunidadP['Diputados']=xls_congreso2.iloc[:,nn+1]
        vot=sum(ComunidadP['Total votantes'])
        votP=sum(ComunidadP[i])
        DR=sum(ComunidadP['Diputados'])
        D=votP*350/vot
        print ('Votos: ',votP," ",format(votP/vot*100,'0.2f'),"% del total")
        print ('  Diputados:')
        print ('  Reales:',DR,' Estimados:',format(D,'0.0f'),' Diferencia:',format(D-DR,'0.0f'))
        nn=nn+2
  # Creamos dataframes para las cámaras
tabla='C:/Users/Antonio/.spyder-py3/02_201606_1.xlsx'
tabla2='C:/Users/Antonio/.spyder-py3/03_201606_1.xlsx'
#Creamos vector con los partidos en el congreso
xls_congreso = pd.read_excel(tabla,header=None,skiprows=4)
arr = xls_congreso.iloc[0] 
x=arr.values
ind=0
ind2=0
pc=[]
for i in x:
    if pd.isnull(i)==False:  
        if ind==0:
            ind=1
            c=ind2
    ind2=ind2+1
arr = xls_congreso.iloc[1] 
x=arr.values
ind=0
for i in x:
    if ind>=c:
        pc.append(i)
    ind=ind+1
xls_congreso = pd.read_excel(tabla,skiprows=5)
xls_senado = pd.read_excel(tabla2,header=None,skiprows=5)
#Creamos vector con los partidos comunes a las 2 cámaras
arr = xls_senado.iloc[1] 
x=arr.values
xls_senado = pd.read_excel(tabla2,skiprows=6)
pcs=[]
ind=0
for i in pc:
    for a in x:
        if i==a:
            ind=1
    if ind==1:
        ind=0
        pcs.append(i)
#Creamos en el dataframe del senado columnas sumando los votos de los partidos
for i in pcs:
    u='Votos '+i
    xls_senado[u]=0
xls_senado['Senado']=0
for i in pcs:
    ind=0
    u='Votos '+i
    for a in x:
        if a==i:
            xls_senado[u]=xls_senado[u]+xls_senado.iloc[:,ind]
        ind=ind+1    
    xls_senado['Senado']=xls_senado['Senado']+xls_senado[u]
#Creamos Dataframe de comparación de porcentaje de voto por comunidad autónoma para luego representarlo en un diagrama para cada
#partido con representación en las 2 cámaras
for i in pcs:
    print ()
    print (i,":")
    Congreso=xls_congreso.groupby(['Nombre de Comunidad'])[['Total votantes',i]].sum()
    Compara=Congreso.sort_values(by=["Nombre de Comunidad"],ascending=[True])
    Congresosort=Compara
    u='Votos '+i
    Senado=xls_senado.groupby(['Nombre de Comunidad'])[[u,'Senado']].sum()
    Senadosort=Senado.sort_values(by=["Nombre de Comunidad"],ascending=[True])
    Compara=Compara.drop(['Total votantes',i], axis=1)
    Compara ["% Congreso"]=Congresosort[i]/Congresosort['Total votantes']*100
    Compara ["% Senado"]=Senadosort[u]/Senadosort['Senado']*100
    print (Compara)
    u='Porcentaje votos '+i+' por comunidad'
    Barras=Compara.plot(kind='barh',title=u)
    Barras.set (xlabel='% Votos',ylabel='Comunidad Autónoma')
    plt.legend()
    plt.show()
    print ("Pulsa INTRO para siguiente partido",end='')
    input()