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

k=6.67

q1=2.
r1=vector([0,0,0])
q2=1.
r2=vector([1,0,0])

q=0.01

res=2.
dr = 1./res
lim = 2.

for x in range(int(-lim*res),int((lim*res)+1)):
  for y in range(int(-lim*res),int((lim*res)+1)):
    for z in range(int(-lim*res),int((lim*res)+1)):
#   for z in range(0,1):
      r=vector([x*dr,y*dr,z*dr])

      d1=resta(r,r1)
      d2=resta(r,r2)

      if (d1.mod and d2.mod):
        F1_mod = -k*q1*q / d1.mod**3
        F1 = vector_escalar(d1,F1_mod)
        F2_mod = -k*q2*q / d2.mod**3
        F2 = vector_escalar(d2,F2_mod)

        F=suma(F1,F2)
        U1=-k*q1*q / d1.mod
        U2=-k*q2*q / d2.mod
        U=U1+U2

        for i in range (0,3): 
          print r.x[i],
        for i in range (0,3): 
          print F.x[i],
        print F.mod, U

