#!/usr/bin/python
# -*- coding: utf8 -*-

"""
Código hecho en clases prácticas de Introducción a la Física
E. de Física - UIS - Santander - Mayo de 2013
Clase de python que permite realizar operaciones algebráicas entre vectores:
Para el vector r, tenemos: 
r=vector(lista) # crea el vector r. lista es una lista de python con las coordenadas del vector
r.x es una lista con las coordenadas del vector r
r.dim es la dimensión del vector r
r.mod es el módulo del vector r

Además, realiza operaciones entre vectores. Sean los vectores r y v:
  
r.prod_escalar(v)  muestra el producto escalar de los vectores r y v, r·v
suma(r,v)  devuelve el vector resultante de sumar r y v
resta(r,v) devuelve el vector resultante de restar r - v
vector_escalar(r,num) devuelve el vector resultante de multiplicar al vector r por el escalar num
"""

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

    def coseno(self,a):
        if (self.dim == a.dim):
          mods=self.mod*a.mod
          if (mods):
            return (self.prod_escalar(a) / mods)
          else:
            print "Para calcular el coseno los vectores no pueden ser nulos"
            return None
        else:
            print "Solo se calcula el coseno para vectores de la misma dimension"
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
