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

Q1=-3.1416
r1=vector([1.,0.,0.])

Q2=-2
r2=vector([0.,1.,0.])

Q3=+1
r3=vector([0.,0.,0.])




r=vector([1,1,1])

d1=resta(r,r1)
V1=k*Q1/d1.mod

d2=resta(r,r2)
V2=k*Q2/d2.mod

d3=resta(r,r3)
V3=k*Q3/d3.mod

V=V1+V2+V3

E1=vector_escalar(d1,k*Q1/d1.mod**3)
E2=vector_escalar(d2,k*Q2/d2.mod**3)
E3=vector_escalar(d3,k*Q3/d3.mod**3)

E12=suma(E1,E2)
E=suma(E12,E3)

for i in range (0,r.dim): 
  print r.x[i],
for i in range (0,r.dim): 
  print E.x[i],
print E.mod,V

import sys
sys.exit()


for x in range(-5,1):
  print
  for y in range(-5,1):
    r=vector([x,y,0])
    V=1e10
    if (resta(r,r1).mod !=0 and resta(r,r2).mod != 0):
      V1=k*Q1/resta(r,r1).mod
      V2=k*Q2/resta(r,r2).mod
      V=V1+V2
    for i in range (0,r.dim): 
      print r.x[i],
    print V







import sys
sys.exit()
# 
# limite=5
# 
# for x in range(-limite,limite+1):
#   print
#   for y in range(-limite,limite+1):
#     r=vector([x,y,0.])
#     
#     d1=resta(r,r1)
#     d2=resta(r,r2)
#     d3=resta(r,r3)
#     if d1.mod != 0 and d2.mod !=0 and d3.mod != 0:
#       V1 = k * q1 / d1.mod
#       V2 = k * q2 / d2.mod
#       V3 = k * q3 / d3.mod
#       V = V1 + V2 + V3 
#       
#       for i in range (0,r.dim): 
#         print r.x[i],
#       print V
# 
# 
# 
# 
# 
# res=5.
# dr = 1./res
# lim = 0.5
# 
# 
# 
# # for x in range(int(-lim*res),int((lim*res)+1)):
# #  for y in range(int(-lim*res),int((lim*res)+1)):
# #    for z in range(int(-lim*res),int((lim*res)+1)):
# #    for z in range(0,1):
# #      r=vector([x*dr,y*dr,z*dr])
