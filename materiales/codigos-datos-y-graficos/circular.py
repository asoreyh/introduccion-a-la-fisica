#!/usr/bin/python
# -*- coding: utf8 -*-

"""
Código hecho en clases prácticas de Introducción a la Física
E. de Física - UIS - Santander - 2014
H. Asorey y C. Sarmiento

Ejemplo sobre como utilizar la nuestra clase vector y el algoritmo visto en clase para calcular trayectorias en R3
"""

####################### mi clase vector
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



################################## mi programa
# aqui comienza mi código...

# Necesito el vector posición de la partícula que se mueve
# movimiento 3D, trabajo en R3, en coordenadas cartesianas
# unidades de distancia en m, de tiempo en s


##### CONDICIONES INICIALES
# posicion inicial, empiezo en x=1 m
r=vector([1,0,0])
# ahora el vector velocidad, perpendicular a r, lo pongo en la dirección y
v=vector([0,2,0])
# y defino el vector aceleración, que por ahora vale 0 (se calcula en el bucle)
a=vector([0,0,0]) # empiezo con 0, porque despues la cambio 

# Defino cuantas vueltas daremos
n=1
# sabemos que v = (2*pi*r)/T, entonces el periodo T es
periodo=2*math.pi*r.mod/v.mod
# y como son n vueltas, el tiempo de simulación vale: 
tiempo=n*periodo

# el tiempo avanza a pasos discretos. Dividimos el periodo en 'res' intervalos
res=10000.
dt=periodo/res # el tiempo avanza en forma discreta a pasos de duración dt

for i in range(0,int(n*res)):
    # imprimo el paso i, el tiempo 
    print i,i*dt,
    for j in range (0,3):  # y las coordenadas del vector posición
      print a.componentes[j],
    print

    # en el movimiento circular, la aceleración es la aceleración centrípeta
    # que tiene dirección radial, sentido hacia dentro y módulo 
    # |a| = (|v|^2)/|r|
    # entonces la aceleración es:
    # a = -((|v|^2)/|r|) * (r/|r|)
    # y luego, el movimiento es el de siempre:
    # movimiento: r(t) = r + v dt
    #             v(t) = v + a dt

    # actualizo la posición r_{i+1} = r_i + v_i dt
    r=suma(r,vector_escalar(v,dt))
    # determino un vector con dirección r, sentido hacia dentro y módulo 1
    r_unit=vector_escalar(r,(-1.)/r.mod)
    # ahora, calculo la aceleración
    a=vector_escalar(r_unit,(v.mod**2/r.mod)) 
    # y actualizo la velocidad v_{i+1} = v_i + a_i dt
    v=suma(v,vector_escalar(a,dt))
    # itero res veces
