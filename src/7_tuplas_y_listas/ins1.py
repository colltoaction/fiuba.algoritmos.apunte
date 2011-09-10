#!/usr/bin/env python
# encoding: latin1
""" M�dulo para inscribir alumnos al curso - versi�n 1 """

# Iniciamos la interacci�n con el usuario
print "Inscripcion en el curso 04 de 75.40"

# Leemos el primer padr�n
padron=input("Ingresa un padr�n (<=0 para terminar): ")

# Procesamos los padrones
# Inicialmente no hay inscriptos
ins = []
while padron > 0:
       # Si todav�a no est�, agregamos el padr�n a la lista de inscriptos,
       if padron not in ins:
              ins.append(padron)
       # de lo contrario avisamos que ya figura
       else:
              print "Ya figura en la lista"

       # Leemos otro padr�n mas
       padron=input("Ingres� un padr�n (<=0 para terminar): ")

# Mostramos el resultado       
print "Esta es la lista de inscriptos: ", ins
