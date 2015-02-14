#!/usr/bin/python
# -*- coding: utf8 -*-

import math

"""
Código hecho en clases prácticas de Introducción a la Física
E. de Física - UIS - Santander - 2013, 2014
H. Asorey y C. Sarmiento

Calcula el potencial y el campo eléctrico en un punto del espacio (r) 
para una configuración con n cargas con valor Q_i ubicadas en r_i (i=1,n)
"""

####################### mi clase vector
# Nuestra clase vector

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
# el codigo

# constante de Coulomb
k=8.988e9

# mis cargas
# En este ejemplo tengo tres cargas: 
Q1 = 1.
r1 = vector([-1.0,0,0])

Q2 = -1.
r2=vector([0,0,0])

Q3 = 1.
r3=vector([1.0,0,0])

# y quiero calcular el potencial y el campo en :
r=vector([1.,1.,1.])

# recuerdo las definicions. Primero, calculo los vectores resta
d1 = resta(r,r1)
d2 = resta(r,r2)
d3 = resta(r,r3)

# y el potencial debido a cada carga en r
V1 = k*Q1/d1.mod
V2 = k*Q2/d2.mod
V3 = k*Q3/d3.mod

# y ahora, segun el ppio de superposicion, el potencial total es
# la suma de cada potencial:
V = V1 + V2 + V3  

# Ahora calculo el campo electrico (es una magnitud vectorial)
# Entonces, calculo el campo electrico debido a cada carga individual
# en vez de usar el vector unitario, uso el vector y divido por el 
# modulo al cubo
E1 = vector_escalar(d1, k * Q1 / d1.mod**3)
E2 = vector_escalar(d2, k * Q2 / d2.mod**3)
E3 = vector_escalar(d3, k * Q3 / d3.mod**3)

# Principio de superposicion: el campo electrico es la suma de cada
# campo individual
E12 = suma(E1, E2)
E = suma(E12,E3)

# finalmente imprimo las coordenadas de r, 
for i in range (0,r.dim):
  print r.componentes[i],

# las coordenadas del campo electrico E(r)
for i in range (0,r.dim):
  print E.componentes[i],

# y el modulo del campo electrico |E(r)| y el potencial V(r)
print E.mod,V
