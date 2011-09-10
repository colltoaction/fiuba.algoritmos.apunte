#/usr/bin/env python
#encoding: latin1

def quick_sort(lista):
    """ Ordena la lista de forma recursiva.
        Pre: los elementos de la lista deben ser comparables.
        Post: la lista est� ordenada. """

	_quick_sort(lista, 0, len(lista)-1)

def _quick_sort(lista, inicio, fin):
	""" Funci�n quick_sort recursiva.
		Pre: los �ndices inicio y fin indican sobre qu� porci�n operar. 
		Post: la lista est� ordenada.
	""" 
    # Caso base
    if inicio >= fin:
        return

    # Caso recursivo
    menores = _partition(lista, inicio, fin)
    _quick_sort(lista, inicio, menores-1)
    _quick_sort(lista, menores+1, fin)

def _partition(lista, inicio, fin):
	""" Funci�n partici�n que trabaja sobre la misma lista.
		Pre: los �ndices inicio y fin indican sobre qu� porci�n operar. 
		Post: los menores est�n antes que el pivote, los mayores despu�s.
		Devuelve: la posici�n en la que qued� ubicado el pivote. """
		
    pivote = lista[inicio]
    menores = inicio

	# Cambia de lugar los elementos 
    for i in xrange(inicio+1, fin+1):
        if lista[i] < pivote:
            menores += 1
            if i != menores:
                _swap(lista, i, menores)
	# Pone el pivote al final de los menores
    if inicio != menores:
        _swap(lista, inicio, menores)
	# Devuelve la posici�n del pivote
	return menores

def _swap(lista, i, j):
	""" Intercambia los elementos i y j de lista. """
    lista[j], lista[i] = lista[i], lista[j]
