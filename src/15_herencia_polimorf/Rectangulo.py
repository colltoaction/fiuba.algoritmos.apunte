#! /usr/bin/env python
#encoding: latin1

from Punto import Punto

class Rectangulo(object):
    """ Esta clase modela un rect�ngulo en el plano. """

    def __init__(self, base, altura, origen):
        """ base (n�mero) es la longitud de su base,
            altura (n�mero) es la longitud de su base,
            origen (Punto) es el punto del plano de su esquina
                           inferior izquierda. """
        self.base = base
        self.altura = altura
        self.origen = origen

    def trasladar(self, dx = 0, dy = 0):
        self.origen = self.origen + Punto(dx,dy)

    def area(self):
        return self.base * self.altura

    def __str__(self):
        """ muestra el rect�ngulo """
        return "Base: %s, Altura: %s, Esquina inf. izq.: %s " % \
               (self.base, self.altura, self.origen)

