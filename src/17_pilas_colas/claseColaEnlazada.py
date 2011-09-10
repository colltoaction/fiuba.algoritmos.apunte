#! /usr/bin/env Python
#encoding: latin1

from claseNodo import Nodo

class Cola:
    """ Representa a una cola, con operaciones de encolar y
        desencolar.  El primero en ser encolado es tambi�n el primero
        en ser desencolado. """

    def __init__(self):
        """ Crea una cola vac�a. """
        # En el primer momento, tanto el primero como el �ltimo son None
        self.primero = None
        self.ultimo = None

    def encolar(self, x):
        """ Agrega el elemento x como �ltimo de la cola. """
        nuevo = Nodo(x)        
        # Si ya hay un �ltimo, agrega el nuevo y cambia la referencia.
        if self.ultimo:
            self.ultimo.prox = nuevo
            self.ultimo = nuevo
        # Si la cola estaba vac�a, el primero es tambi�n el �ltimo.
        else:
            self.primero = nuevo
            self.ultimo = nuevo

    def desencolar(self):
        """ Elimina el primer elemento de la cola y devuelve su 
            valor. Si la cola est� vac�a, levanta ValueError. """
        # Si hay un nodo para desencolar
        if self.primero:
            valor = self.primero.dato
            self.primero = self.primero.prox
            # Si despu�s de avanzar no qued� nada, tambi�n hay que
            # eliminar la referencia del �ltimo.
            if not self.primero:
                self.ultimo = None
            return valor
        else:
            raise ValueError("La cola est� vac�a")

    def es_vacia(self):
        """ Devuelve True si la cola esta vac�a, False si no."""
        return self.primero == None
