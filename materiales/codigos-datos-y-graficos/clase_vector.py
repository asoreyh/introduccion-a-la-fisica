#!/usr/bin/python
# -*- coding: utf8 -*-

"""
Código hecho en clases prácticas de Introducción a la Física
E. de Física - UIS - Santander - 2013, 2014
H. Asorey y C. Sarmiento

Clase de python que permite realizar operaciones algebráicas entre vectores:
Para el vector r, tenemos: 
r=vector(lista) # crea el vector r. lista es una lista de python con las componentes del vector
r.componentes es una lista con las componentes del vector r
r.dim es la dimensión del vector r
r.mod es el módulo del vector r

Además, realiza operaciones entre vectores. Sean los vectores r y v:
  
prod_escalar(r,v)  calcula el producto escalar de los vectores r y v, r·v
coseno(r,v)        calcula el coseno del ánqulo que forman los vectores r y v
suma(r,v)          devuelve el vector resultante de sumar r y v
resta(r,v)         devuelve el vector resultante de restar r - v

y entre vectores y escalares. Sea el vector r y el escalar k: 

vector_escalar(r,k) devuelve el vector resultante de multiplicar al vector r por el escalar k
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
