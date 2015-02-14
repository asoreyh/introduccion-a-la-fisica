#!/usr/bin/python
# -*- coding: utf8 -*-
"""
Código hecho en clases prácticas de Introducción a la Física
E. de Física - UIS - Santander - Abril 2013
Lee un archivo con seis columnas con datos de exoplanetas e imprime 
la masa de la estrella en kg y el semieje mayor en m
"""

import math
masa_sol=1.988e30 # en kg
masa_jupiter=1.898e27 # en kg
ua=1.496e11 # en m
G=6.67e-11

class exoplaneta:
  def __init__(self,lista):
    self.numero=float(lista[0])
    self.nombre=lista[1]
    self.masa_planeta=float(lista[2])*masa_jupiter
    self.masa_estrella=float(lista[3])*masa_sol
    self.semieje=float(lista[4])*ua
    self.e=float(lista[5])

lista=[]
for linea in open("problema.dat"):  # itero sobre todo el archivo problema.dat
  lista=linea.split() # tranforma la linea leida en una lista separando por espacios
  if len(lista)==6:   # si la lista tiene 6 elementos, entonces:
    exo=exoplaneta(lista) # creo el objeto 'exoplaneta' a partir de la lista de parámetros
    if ((exo.masa_estrella/exo.masa_planeta) >= 200. and exo.e >=0.3):
	    foco=exo.semieje*exo.e
	    b=math.sqrt(exo.semieje**2-foco**2)
	    pe=exo.semieje-foco
	    ap=exo.semieje+foco
	    T=math.sqrt(4. * math.pi**2 * exo.semieje**3 / (G*exo.masa_estrella))
	    print exo.numero, exo.nombre, exo.masa_planeta, exo.masa_estrella, exo.semieje, exo.e, b, foco, pe, ap, T/(365.25*86400)
