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


################################## mi programa

k=8.988

q1=0.
r1=vector([-1.0,0,0])
q2=1.
r2=vector([0,0,0])
q3=0.
r3=vector([1.0,0,0])
q4=0.
r4=vector([0,1.0,0])
q5=0.
r5=vector([0,-1.0,0])

q=-0.05
res=4.
dr = 1./res
lim = 2.

for x in range(int(-lim*res),int((lim*res)+1)):
  for y in range(int(-lim*res),int((lim*res)+1)):
    for z in range(int(-lim*res),int((lim*res)+1)):
#   for z in range(0,1):
      r=vector([x*dr,y*dr,z*dr])

      d1=resta(r,r1)
      d2=resta(r,r2)
      d3=resta(r,r3)
      d4=resta(r,r4)
      d5=resta(r,r5)

      if (d1.mod and d2.mod and d3.mod and d4.mod and d5.mod):
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

        Fa=suma(F1,F2)
        Fb=suma(F3,F4)
        Fc=suma(Fa,Fb)
        F=suma(F5,Fc)

        for i in range (0,3): 
          print r.x[i],
        for i in range (0,3): 
          print F.x[i],
        print F.mod
