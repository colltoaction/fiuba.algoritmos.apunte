#!/usr/bin/env python
# encoding: latin1
""" M�dulo para inscribir alumnos al curso - versi�n 0 """

# Iniciamos la interacci�n con el usuario
print "Inscripcion en el curso 04 de 75.40"

# Leemos el primer padr�n
padron=input("Ingresa un padr�n (<=0 para terminar): ")

# Procesamos los padrones
# Inicialmente no hay inscriptos
ins = []
while padron > 0:
       # Agregamos el padr�n le�do a la lista de inscriptos
       ins.append(padron)

       # Leemos otro padr�n m�s
       padron=input("Ingres� un padr�n (<=0 para terminar): ")

# Mostramos el resultado       
print "Esta es la lista de inscriptos: ", ins
