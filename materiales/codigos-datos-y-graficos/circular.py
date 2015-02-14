#!/usr/bin/python
# -*- coding: utf8 -*-

"""
Código hecho en clases prácticas de Introducción a la Física
E. de Física - UIS - Santander - Junio de 2013

Ejemplo sobre como utilizar la nuestra clase vector y el algoritmo visto en clase
para calcular trayectorias en R3
"""

####################### mi clase vector
import math

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

    def coseno(self,a):
        if (self.dim == a.dim):
          mods=self.mod*a.mod
          if (mods):
            return (self.prod_escalar(a) / mods)
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
          suma.append(a.x[i]+b.x[i])
       return vector(suma)
    else:
       print "La suma se define para vectores de la misma dimension"
       return None

def resta(a, b):
    resta=[]
    if (a.dim == b.dim):
       for i in range(0,a.dim):
          resta.append(a.x[i]-b.x[i])
       return vector(resta)
    else:
       print "La resta se define para vectores de la misma dimension"
       return None

def vector_escalar(a, num):
    escalar=[]
    for i in range(0,a.dim):
      escalar.append(num*a.x[i])
    return vector(escalar)


################################## mi programa
# aqui comienza mi código...

# Necesito el vector posición de la partícula que se mueve
# movimiento 3D, trabajo en R3, en coordenadas cartesianas (da igual)
# unidades de distancia en m, de tiempo en s

r=vector([0,0,0])  # empiezo en el origen

#ahora el vector velocidad
v=vector([0,0,10]) # tiro oblicuo a 45°, en m/s

#y eventualmente un vector aceleración
a=vector([0,0,-9.8])  # uso g en la Tierra, dirección vertical, sentido negativo, en m/s^2

# el tiempo en segundos...
res=100. # voy a dividir cada segundo en res intervalos... 
tiempo=1.5
dt=1./res # el tiempo avanza en forma discreta, cada paso es 1/res segundos

for i in range(0,(int(tiempo*res)+1)):
    # movimiento: r(t) = r + v dt
    #             v(t) = v + a dt

    # imprimo el paso i, el tiempo 
    print i,i*dt,
    for i in range (0,3):  # y las coordenadas del vector posición
      print r.x[i],

    print 

    # cinemática
    vt=vector_escalar(v,dt)
    r=suma(r, vt) # actualizo la posición r_{i+1} = r_i + v_i dt
    v=suma(v,vector_escalar(a,dt)) # actualizo la velocidad v_{i+1} = v_i + a_i dt







