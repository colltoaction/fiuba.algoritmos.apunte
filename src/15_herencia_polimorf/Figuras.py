#!/usr/bin/env python
#encoding: latin1

from math import pi

class Figura(object):
    """ Una figura en el plano. """
    def area(self):
        " Este m�todo debe ser redefinido. "
        pass

class Circulo(Figura):
    """ Un c�rculo en el plano. """
    def __init__(self, radio=0):
        " Constructor de c�rculo. "
        self.radio = radio

    def area(self):
        " Devuelve el �rea del c�rculo. "
        return pi * self.radio * self.radio

class Triangulo(Figura):
    """ Un tri�ngulo en el plano. """
    def __init__(self, base=0, altura=0):
        " Constructor de tri�ngulo. "
        self.base = base
        self.altura = altura

    def area(self):
        " Devuelve el �rea del tri�ngulo. "
        return self.base * self.altura / 2.

