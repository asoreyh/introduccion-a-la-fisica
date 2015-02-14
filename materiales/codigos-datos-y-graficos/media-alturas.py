#!/usr/bin/python
# -*- coding: utf8 -*-

"""
Código hecho en clases prácticas de Introducción a la Física
E. de Física - UIS - Santander - 2013, 2014
H. Asorey y C. Sarmiento

Ejemplo para calcular la media de un conjunto de datos
"""

####################### las cosas que necesita
import math

####################### mis definiciones y clases

################################## mi programa
# aqui comienza mi código...
n=0.0;
suma_alturas = 0.0;

alturas=(1.68, 1.76, 1.52, 1.98, 1.75);

n=len(alturas);

if (n > 0.0):
  for h_i in alturas:
    suma_alturas += h_i;
  media = suma_alturas / n;
  print "Tengo",n,"alturas";
  print "La media es : ", media;
else:
  print "Error. Debo tener al menos una altura para calcular la media";
















