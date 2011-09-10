#!/usr/bin/env python
# encoding: latin1

def busqueda_lineal(lista, x):
    """ B�squeda lineal.
	Si x est� en lista devuelve su posici�n en lista, de lo
    contrario devuelve -1.
    """

    # Estrategia: se recorren uno a uno los elementos de la lista
    # y se los compara con el valor x buscado.

    i=0 # i tiene la posici�n actual en la lista, comienza en 0

    # el ciclo for recorre todos los elementos de lista:
    for z in lista:
        # estamos en la posicion i, z contiene el valor de lista[i]
    
        # si z es igual a x, devuelve i
        if z == x:
            return i
      
        # si z es distinto de x, incrementa i, y contin�a el ciclo
        i=i+1

    # si sali� del ciclo sin haber encontrado el valor, devuelve -1
    return -1

