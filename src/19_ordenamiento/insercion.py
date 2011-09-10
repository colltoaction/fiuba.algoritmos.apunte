#!/usr/bin/env python
#encoding: latin1

def ord_insercion(lista):
    """ Ordena una lista de elementos seg�n el m�todo de inserci�n.
        Pre: los elementos de la lista deben ser comparables.
        Post: la lista est� ordenada. """

    # i va desde la primera hasta la pen�ltima posici�n de la lista
    for i in xrange(len(lista)-1):

        # Si el elemento de la posici�n i+1 est� desordenado respecto
        # al de la posici�n i, reubicarlo dentro del segmento [0:i]
        if lista[i+1]< lista[i]:
            reubicar(lista, i+1)

        print "DEBUG: ", lista

def reubicar(lista, p):
    """ Reubica al elemento que est� en la posici�n p de la lista 
        dentro del segmento [0:p-1].
        Pre: p tiene que ser una posicion v�lida de lista. """

    # v es el valor a reubicar
    v = lista[p]

    # Recorre el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posici�n j tal que lista[j-1] <= v < lista[j].
    j = p 
    while j > 0 and v < lista[j-1]:
		# Desplaza los elementos hacia la derecha, dejando lugar
		# para insertar el elemento v donde corresponda.
        lista[j] = lista[j-1]
		# Se mueve un lugar a la izquierda
        j -= 1

    # Ubica el valor v en su nueva posici�n
    lista[j] = v
