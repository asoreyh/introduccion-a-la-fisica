#!/usr/bin/python
# -*- coding: utf8 -*-
"""
Código hecho en clases prácticas de Introducción a la Física
E. de Física - UIS - Santander - Abril 2013
Lee un archivo con seis columnas con datos de exoplanetas e imprime 
la masa de la estrella en kg y el semieje mayor en m
"""

masa_sol=1.988e30 # en kg
masa_jupiter=1.898e27 # en kg
ua=1.496e11 # en m

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
    if (exo.semieje > 100*ua): # muestro aquellos cuyo semieje mayor es mayor que 100 UA
      print exo.numero, exo.nombre, exo.masa_planeta, exo.masa_estrella, exo.e, exo.semieje  #imprimo algunos valores
