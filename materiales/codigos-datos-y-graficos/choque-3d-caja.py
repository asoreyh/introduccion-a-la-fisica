#!/usr/bin/python
# -*- coding: utf8 -*-

"""
Código hecho en clases prácticas de Introducción a la Física
E. de Física - UIS - Santander - 2013, 2014
H. Asorey y C. Sarmiento

Calcula los rebotes de una pelota con coeficiente de restitución definido
por el usuario en una caja tridimensional cerrada, con o sin gravedad
"""

import math

class vector:
    def __init__(self,lista):
        self.componentes=[]
        for componente_i in lista:
          self.componentes.append(float(componente_i))
        self.dim=len(self.componentes)
        self.mod=math.sqrt(prod_escalar(self,self))

###################### Operaciones entre vectores

def prod_escalar(a,b):
    if (a.dim == b.dim):
        pesc=0.
        for i in range(0,a.dim):
            pesc += (a.componentes[i] * b.componentes[i])
        return pesc
    else:
        print "El productor escalar se define para vectores de la misma dimension"
        return None

def coseno(a,b):
    if (a.dim == b.dim):
      mods=a.mod*b.mod
      if (mods != 0 ):
        return (prod_escalar(a,b) / mods)
      else:
        print "Para calcular el coseno los vectores no pueden ser nulos"
        return None
    else:
        print "Sólo se calcula el coseno para vectores de la misma dimension"
        return None

def suma(a, b):
    suma=[]
    if (a.dim == b.dim):
       for i in range(0,a.dim):
          suma.append(a.componentes[i]+b.componentes[i])
       return vector(suma)
    else:
       print "La suma se define para vectores de la misma dimension"
       return None

def resta(a, b):
    resta=[]
    if (a.dim == b.dim):
       for i in range(0,a.dim):
          resta.append(a.componentes[i]-b.componentes[i])
       return vector(resta)
    else:
       print "La resta se define para vectores de la misma dimension"
       return None

################################## Producto por un escalar

def vector_escalar(a, num):
    escalar=[]
    for i in range(0,a.dim):
      escalar.append(num*a.componentes[i])
    return vector(escalar)

############## funcion rebote

# verifica si la pelotita alcanzo los bordes de la caja
# y rebota si eso ocurrio

# estos son los limites de la caja, entre -1 y +1 en cada eje
caja=[1.,1.,1.]
# la caja es una región del espacio entre 
# -1 <= x <= +1
# -1 <= y <= +1
# -1 <= z <= +1

def rebote(r, v, restitucion):
  for i in range(0,r.dim):
    if (abs(r.componentes[i]) >= caja[i]):
      if (r.componentes[i] < 0):
        r.componentes[i] = -caja[i]
      else:
        r.componentes[i] = caja[i]

      v.componentes[i] = -v.componentes[i] * restitucion

#########
######################### mi programa

# Necesito el vector posicion de la particula que se mueve
# movimiento 3D, trabajo en R3 (xyz), en coordenadas cartesianas
# unidades de distancia en m, de tiempo en s

# sale del origen (el centro geometrico de la caja)
r=vector([0,0,0])

# ahora el vector velocidad
# conviene usar valores diferentes en los tres ejes
# y tratando que sean números irracionales
v=vector([1.,2.,3.]) # en m/s

# aceleracion, en este caso, gravedad terrestre
g=vector([0,0,-9.8])  # en m/s^2
# g=vector([0,0,0])  # en m/s^2 // esto es sin gravedad
# g=vector([0,0,-1.6])  # en m/s^2 // estoy en la luna 

# tiempo total de simulacion, en segundos
tiempo=200.

# resolucion temporal, numero de pasos por segundo
res=1000.

# en cada paso, el tiempo avanza dt = 1/res:
dt=1./res

# y avanza a pasos discretos. Uso n:
for n in range(0,int(tiempo*res)+1): # p. ej, 5 segundos
    # movimiento de a pasitos: divido el tiempo en intervalos
    # movimiento: r(t) = r0 + v(t) t, v(t) = v0+g*t
  
    # imprimo el paso, el tiempo (s) y la posicion (m):
    print n,n*dt,
    for i in range (0,r.dim):
      print r.componentes[i],
    print

    # verifico si alcance las paredes de la caja. 0.6 es el coeficiente de restitucion.
    # la funcion espera la posicion, la velocidad y el coef. de restitucion
    # para choques elasticos, deberia usar 
    # rebote(r,v,1.0)

    # choque parcialmente inelastico
    rebote(r,v,1.0)

    # actulizo la posicion y la velocidad
    r=suma(r,vector_escalar(v,dt))
    v=suma(v,vector_escalar(g,dt))
