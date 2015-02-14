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
    if (abs(r.x[i]) >= caja[i]):
      if (r.x[i] < 0):
        r.x[i] = -caja[i]
      else:
        r.x[i] = caja[i]

      v.x[i] = -v.x[i] * restitucion

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
#g=vector([0,0,-9.8])  # en m/s^2
g=vector([0,0,0])  # en m/s^2


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
      print r.x[i],
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
