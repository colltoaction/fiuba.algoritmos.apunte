#! /usr/bin/env python
#encoding: latin1

class Cola:
    """ Representa a una cola, con operaciones de encolar y
        desencolar.  El primero en ser encolado es tambi�n el primero
        en ser desencolado. """

    def __init__(self):
        """ Crea una cola vac�a. """
        # La cola vac�a se representa por una lista vac�a
        self.items=[]

    def encolar(self, x):
        """ Agrega el elemento x como �ltimo de la cola. """
        self.items.append(x)

    def desencolar(self):
        """ Elimina el primer elemento de la cola y devuelve su 
            valor. Si la cola est� vac�a, levanta ValueError. """
        try:
          return self.items.pop(0)
        except:
          raise ValueError("La cola est� vac�a")

    def es_vacia(self):
        """ Devuelve True si la cola esta vac�a, False si no."""
        return self.items == []
