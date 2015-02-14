#!/usr/bin/python
# -*- coding: utf8 -*-

import math

####################### mi clase vector

class vector:
    def __init__(self,lista):
        self.x=[]
        for xi in lista:
          self.x.append(float(xi))
        self.dim=len(self.x)
        self.mod=math.sqrt(self.prod_escalar(self))

    def prod_escalar(self,a):
        if (self.dim == a.dim):
            pesc=0.
            for i in range(0,self.dim):
                pesc += (self.x[i] * a.x[i])
            return pesc
        else:
            print "El productor escalar se define para vectores de la misma dimension"
            return None

def suma(a, b):
    suma=[]
    if (a.dim == b.dim):
       for i in range(0,a.dim):
          suma.append(a.x[i]+b.x[i])
       return vector(suma)
    else:
       return None

def resta(a, b):
    resta=[]
    if (a.dim == b.dim):
       for i in range(0,a.dim):
          resta.append(a.x[i]-b.x[i])
       return vector(resta)
    else:
       return None

def vector_escalar(a, num):
    escalar=[]
    for i in range(0,a.dim):
      escalar.append(num*a.x[i])
    return vector(escalar)



############## funcion rebote

# verifica si la pelotita alcanzo la pared o el piso
# y rebota si eso ocurrio

pared=1. # a 1 m del origen en la direccion x
piso=0. # el piso esta en z=0
def rebote(r, v, restitucion):
  # hay dos paredes, en x = +1 y en x=-1 
  if (abs(r.x[0]) >= pared): 
    v.x[0] = -v.x[0] * restitucion
    if (r.x[0] >= pared):
      r.x[0] = pared
    else:
      r.x[0] = -pared
  # piso en z=0
  if (r.x[1] <= piso): 
    r.x[1] = piso
    v.x[1] = -v.x[1] * restitucion

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
for n in range(0,int(tiempo*res)+1): # p. ej, 5 segundos
    # movimiento de a pasitos: divido el tiempo en intervalos
    # movimiento: r(t) = r0 + v(t) t, v(t) = v0+g*t


    # imprimo el paso, el tiempo (s) y la posicion (m):
    print n,n*dt,
    for i in range (0,r.dim):
      print r.x[i],
    print

    # miro si choque la pared o el piso. 0.9 es el coeficiente de restitucion.

    # la funcion espera la posicion, la velocidad y el coef. de restitucion
    # para choques elasticos, deberia usar 
    # rebote(r,v,1.0)

    # choque parcialmente inelastico
    rebote(r,v,0.9)

    # actulizo la posicion y la velocidad
    r=suma(r,vector_escalar(v,dt))
    v=suma(v,vector_escalar(g,dt))
