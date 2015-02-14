#!/usr/bin/python
# -*- coding: utf8 -*-

"""
Código hecho en clases prácticas de Introducción a la Física
E. de Física - UIS - Santander - 2013, 2014
H. Asorey y C. Sarmiento

Calcula los rebotes de una pelota con coeficiente de restitución definido
por el usuario sobre una pared vertical y un piso horizontal. 
"""

import math

####################### mi clase vector

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

# verifica si la pelotita alcanzo la pared o el piso
# y rebota si eso ocurrio

pared=1. # a 1 m del origen en la direccion x
piso=0. # el piso esta en z=0
def rebote(r, v, restitucion):
  # hay dos paredes, en x = +1 y en x=-1 
  if (abs(r.componentes[0]) >= pared): 
    v.componentes[0] = -v.componentes[0] * restitucion
    if (r.componentes[0] >= pared):
      r.componentes[0] = pared
    else:
      r.componentes[0] = -pared
  # piso en z=0
  if (r.componentes[1] <= piso): 
    r.componentes[1] = piso
    v.componentes[1] = -v.componentes[1] * restitucion

################################## mi programa
# Necesito el vector posicion de la particula que se mueve
# movimiento 2D, trabajo en R2 (xz), en coordenadas cartesianas
# unidades de distancia en m, de tiempo en s


#posicion incial de la pelotita x=0, z=1.8 m
r=vector([0,1.8])

#ahora el vector velocidad
v=vector([1,0]) # movimiento horizontal, en m/s

# la aceleracion de la gravedad
g=vector([0,-9.8])  # movimiento acelerado, en m/s^2

# tiempo total de simulacion, en segundos
tiempo=10.0

# resolucion temporal, numero de pasos por segundo
res=1000.

# en cada paso, el tiempo avanza dt = 1/res:
dt=1./res

# y avanza a pasos discretos. Uso n:
for n in range(0,int(tiempo*res)+1): # p. ej, tiempo=10 segundos
    # movimiento de a pasitos: divido el tiempo en intervalos
    # movimiento: r(t) = r0 + v(t) t, v(t) = v0+g*t


    # imprimo el paso, el tiempo (s) y la posicion (m):
    print n,n*dt,
    for i in range (0,r.dim):
      print r.componentes[i],
    print

    # miro si choque la pared o el piso.

    # la funcion espera la posicion, la velocidad y el coef. de restitucion
    # para choques elasticos, deberia usar 
    # rebote(r,v,1.0)

    # choque parcialmente inelastico. 0.9 es el coeficiente de restitucion.
    rebote(r,v,0.9)

    # actulizo la posicion y la velocidad
    r=suma(r,vector_escalar(v,dt))
    v=suma(v,vector_escalar(g,dt))
