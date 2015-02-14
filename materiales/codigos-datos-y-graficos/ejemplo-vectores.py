#!/usr/bin/python
# -*- coding: utf8 -*-

"""
Código hecho en clases prácticas de Introducción a la Física
E. de Física - UIS - Santander - 2014
H. Asorey y C. Sarmiento

Ejemplo sobre como utilizar nuestra clase vector y operaciones entre vectores 
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


################################## mi programa
# aqui comienza mi código...

a=vector([3,1,0])

print "Las componentes del vector a son: ", a.componentes
print "La dimensión de a es: ", a.dim
print "El módulo del vector a es: ", a.mod

b=vector([-3,1,1])

print "Producto escalar a·b=", prod_escalar(a,b)
print "Producto escalar b·a=", prod_escalar(b,a)

c=suma(a,b)
d=resta(a,b)

print "a=",a.componentes
print "b=",b.componentes
print "a+b=",c.componentes
print "a-b=",d.componentes

julio=vector_escalar(b,5.0)

print "El vector obtenido multiplicando al vector b por 5 es:", julio.componentes
print "El coseno del ángulo formado por los vectores a y b es:", coseno(a,b)
print "El coseno del ángulo formado por los vectores a y julio es:", coseno(a,julio)

