#!/usr/bin/python
# -*- coding: utf8 -*-

"""
Código hecho en clases prácticas de Introducción a la Física
E. de Física - UIS - Santander - 2014
H. Asorey y C. Sarmiento

Análisis de datos del proyecto LAGO (Latin American Giant Observatory)
para el programa LAGO-SpaceWeather y LAGO-Universities
Distribuido sólo con fines educativos. Only for educational purposes
The LAGO Project, lago@lagoproject.org, http://lagoproject.org
"""

import sys
import math

################ clase data 
## 
## 
## 

class lago:
  def __init__(self,dat):
    self.time=float(dat[0])
    self.pres=float(dat[1])
    self.temp=float(dat[2])
    self.flux=float(dat[3])
    self.bnds=dat[4:len(dat)]
    self.good=True

################################## mi programa
# aqui comienza mi código...

# verifico si estoy pasando un archivo al análisis
if (len(sys.argv)<2):
    print
    print "Error: you need to give the file to analyze"
    print "Usage:",sys.argv[0], "<filename>"
    print 
    sys.exit(1)

data = []

for line in open(sys.argv[1]): # leo el archivo, con el nombre dado en consola 
  if ((line.strip()).startswith("#")): # salto los comentarios que empiezan con '#'
    continue
  line.rstrip() # remueve el salto de línea final
  datum=lago(line.split()) 
  data.append(datum)

n=len(data)
if (not n):
    print
    print "Error: no survived data."
    print
    sys.exit(1)


# outsiders: determino la media y el desvío de los datos
avg=sum(x.flux for x in data)/n
av2=sum(x.flux**2 for x in data)/n # suma de cuadrados / n
dev=math.sqrt(av2-avg**2) # desvio = raiz_cuad(suma_cuad/n - media**2)

# ahora filtro los datos que esten a más de tantos sigmas
maxsig=5.
good_top=avg+maxsig*dev 
good_low=avg-maxsig*dev
nbad=0

for i in range(0,n):
    if (data[i].flux < good_low or data[i].flux > good_top):
        data[i].good=False
        nbad+=1


print "#",nbad,"/",n,"(","%.3f" % (nbad*100./n),"%) data points are ruled out by",maxsig,"sigma analysis"
# y ahora, calculo promedios cada 'interval' minutos
# sabiendo que tengo una medición por minuto
interval=10
sum_f=0.
sum_p=0.
f=0
bands=len(data[0].bnds)
flux_sum=[]
pres_sum=[]
bnds_sum=[]
n_sum=[]
t_medio=[]

sum_b = [0. for x in range(bands)]

for i in range(0,n,interval):
  for j in range(interval):
    if((i+j)<n):
      if data[i+j].good:
        sum_f+=data[i+j].flux
        sum_p+=data[i+j].pres
        for k in range(bands):
          sum_b[k]+=float(data[i+j].bnds[k])
        f+=1
  flux_sum.append(sum_f)
  pres_sum.append(sum_p)
  bnds_sum.append(sum_b)
  n_sum.append(f)
  t_medio.append(int(data[i].time+interval*60./2.))
  sum_f=0.
  sum_p=0.
  sum_b = [0. for x in range(bands)]
  f=0

# resultados en promedio.csv
fv=open("promedio.csv","w")

fv.write("#Time,Pressure,Flux")
for i in range(bands):
  fv.write(",band{0:02d}".format(i+1))
fv.write("\n")

for i in range(len(n_sum)):
  if n_sum[i]:
    pres_avg=pres_sum[i]/n_sum[i]
    flux_avg=flux_sum[i]/n_sum[i]
    fv.write("{0:d} {1:.2f} {2:.2f}".format(t_medio[i],pres_avg,flux_avg))
    for x in bnds_sum[i]:
      band_avg=float(x)/n_sum[i]
      fv.write(" {0:.2f}".format(band_avg))
    fv.write("\n")
fv.close()
