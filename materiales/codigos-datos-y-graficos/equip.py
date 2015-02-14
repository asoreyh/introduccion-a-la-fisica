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

q1=1.
r1=vector([0,0,0])

q=1e-1
mod=2.
F_mod = k * q1 * q / 8.

for q in range(0,91,5):
  for f in range(0,361,10):
    x=mod * math.sin(math.radians(q)) * math.cos(math.radians(f))
    y=mod * math.sin(math.radians(q)) * math.sin(math.radians(f))
    z=mod * math.cos(math.radians(q))
    r=vector([x,y,z])
    F = vector_escalar(r,F_mod)
    for i in range (0,3): 
      print r.x[i],
    for i in range (0,3): 
      print F.x[i],
    print F.mod 
