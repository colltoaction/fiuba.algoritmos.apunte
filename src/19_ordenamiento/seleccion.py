#/usr/bin/env python
#encoding: latin1

def ord_seleccion(lista):
    """ Ordena una lista de elementos seg�n el m�todo de selecci�n.
        Pre: los elementos de la lista deben ser comparables.
        Post: la lista est� ordenada. """

    # n = posicion final del segmento a tratar, comienza en len(lista)-1
    n = len(lista)-1

    # cicla mientras haya elementos para ordenar (2 o m�s elementos)
    while n > 0:

        # p es la posicion del mayor valor del segmento
        p = buscar_max(lista, 0, n)

        # intercambia el valor que est� en p con el valor que 
        # est� en la �ltima posici�n del segmento
        lista[p], lista[n] = lista[n], lista[p]

        print "DEBUG: ", p, n, lista

        # reduce el segmento en 1
        n = n - 1

def buscar_max(lista, ini, fin):
    """ Devuelve la posici�n del m�ximo elemento en un segmento de
        lista de elementos comparables.  
        Se trabaja sobre lista, que no debe ser vac�a.
        ini es la posici�n inicial del segmento, debe ser v�lida.
        fin es la posici�n final del segmento, debe ser v�lida. """
        
    pos_max = ini
    for i in xrange(ini+1, fin+1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max
