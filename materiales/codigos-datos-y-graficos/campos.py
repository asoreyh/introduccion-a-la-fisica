#!/usr/bin/python
# -*- coding: utf8 -*-

"""
Código hecho en clases prácticas de Introducción a la Física
E. de Física - UIS - Santander - 2013, 2014
H. Asorey y C. Sarmiento

Calcula la fuerza electrostática sobre una carga q producida por por 
hasta cinco cargas Q_i en las posiciones r_i (i=1...5).

Lo hace sobre una cuadrícula 3D entre -lim <= x_i <= lim, con una 
resolución espacial de 1/res.
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

k=8.988e9  ## Constante de Coulomb

q1=0.       # carga 1 
r1=vector([-1.0,0,0])   # posición carga 1 
q2=1.       # ...
r2=vector([0,0,0])
q3=0.
r3=vector([1.0,0,0])
q4=0.
r4=vector([0,1.0,0])
q5=0.
r5=vector([0,-1.0,0])

q=1.0       # carga de prueba
res=4.      # resolución = 1/res
dr = 1./res  
lim = 2.    # la cuadrícula va entre -lim <= x_i <= lim


# cuadrícula
for x in range(int(-lim*res),int((lim*res)+1)):
  for y in range(int(-lim*res),int((lim*res)+1)):
    for z in range(int(-lim*res),int((lim*res)+1)):
      # posición de la carga de prueba
      r=vector([x*dr,y*dr,z*dr])

      # calculamos la pos. relativa a las cargas
      d1=resta(r,r1)
      d2=resta(r,r2)
      d3=resta(r,r3)
      d4=resta(r,r4)
      d5=resta(r,r5)

      # si no estoy sobre alguna de las cargas
      if (d1.mod and d2.mod and d3.mod and d4.mod and d5.mod):
        # calculo las fuerzas individuales
        F1_mod = k*q1*q / d1.mod**3
        F1 = vector_escalar(d1,F1_mod)
        F2_mod = k*q2*q / d2.mod**3
        F2 = vector_escalar(d2,F2_mod)
        F3_mod = k*q3*q / d3.mod**3
        F3 = vector_escalar(d3,F3_mod)
        F4_mod = k*q4*q / d4.mod**3
        F4 = vector_escalar(d4,F4_mod)
        F5_mod = k*q5*q / d5.mod**3
        F5 = vector_escalar(d5,F5_mod)

        # superposición
        Fa=suma(F1,F2)
        Fb=suma(F3,F4)
        Fc=suma(Fa,Fb)
        F=suma(F5,Fc)

        # resultados
        for i in range (0,3): 
          print r.componentes[i],
        for i in range (0,3): 
          print F.componentes[i],
        print F.mod
