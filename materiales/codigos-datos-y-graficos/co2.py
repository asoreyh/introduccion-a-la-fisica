#!/usr/bin/python
# -*- coding: utf8 -*-

"""
Código hecho en clases prácticas de Introducción a la Física
E. de Física - UIS - Santander - 2013, 2014
H. Asorey y C. Sarmiento

Calcula la media y el desvío del registro histórico de la concentración
de CO2 en el aire, para el período t_i <= t <= t_f definido por el usuario 
"""

####################### las cosas que necesita
import math

####################### mis definiciones y clases

################################## mi programa
# aquí comienza mi código...

# Auxiliares  
suma=0.  # la suma de los datos
suma2=0. # la suma de los cuadrados
n=0  # la cantidad de datos que estoy sumando
datos = []  # una lista para contener la línea leída
tiempo = 0.  # el año del registro
co2 = 0.    # la concentración del registro

# Resultados
media=0. # la media
varianza=0. # la varianza
desvio=0.  # el desvío

#Voy a mirar el CO2 en el periodo comprendido entre ti y tf
ti=-1000000.  # en este caso tomo 1 millón de años en el pasado
tf=1957.      # hasta que comienza el registro moderno (en 1958)

for linea in open("co2.dat"):
  if ((linea.strip()).startswith("#")): # salto los comentarios en los datos, empiezan con '#'
    continue
  linea.rstrip() # remueve el salto de línea final
  datos = linea.split()
  tiempo = float(datos[0])
  co2 = float(datos[1])
  # si el registro está dentro del periodo de interés, ti <= t <= tf, entonces uso el registro 
  if (tiempo >= ti and tiempo <= tf):
    n += 1  # cuento los registros que pasan el criterio de filtrado
    suma += co2  # sumo los valores
    suma2 += co2**2  # los valores al cuadrado

# Ahora tengo n elementos leídos, su suma y la suma de los cuadrados
# por las dudas, verifico que n>0 (podría tener el caso de que mi filtro deje 0 elementos)

if (n > 0.0):
  media = suma / n;
  varianza = suma2 / n - media**2
  desvio = math.sqrt(varianza)
  print
  print "Tengo",n,"registros en el periodo:",ti,"<= t <=",tf
  print "la media de la concentración de CO2 es", "%.3f"%media, "ppm de CO2"
  print "con un desvío de", "%.3f" % desvio , "ppm de CO2"
  print 
else:
  print "Error. El criterio de filtrado produjo 0 registros";
