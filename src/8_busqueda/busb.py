#!/usr/bin/env python
# encoding: latin1

def busqueda_binaria(lista, x):
    """B�squeda binaria
    Precondici�n: lista est� ordenada
    Devuelve -1 si x no est� en lista;
    Devuelve p tal que lista[p] == x, si x est� en lista
    """

    # Busca en toda la lista dividi�ndola en segmentos y considerando
    # a la lista completa como el segmento que empieza en 0 y termina
    # en len(lista) - 1.

    izq = 0              # izq guarda el �ndice inicio del segmento
    der = len(lista) - 1 # der guarda el �ndice fin del segmento

    # un segmento es vac�o cuando izq > der:
    while izq <= der:
        # el punto medio del segmento
        medio = (izq+der)/2

        print "DEBUG:", "izq:", izq, "der:", der, "medio:", medio

        # si el medio es igual al valor buscado, lo devuelve
        if lista[medio] == x:
            return medio
        # si el valor del punto medio es mayor que x, sigue buscando
        # en el segmento de la izquierda: [izq, medio-1], descartando la
        # derecha
        elif lista[medio] > x:
            der = medio-1
        # si no, sigue buscando en el segmento de la derecha:
        # [medio+1, der], descartando la izquierda
        else:
            izq = medio+1
        # si no sali� del ciclo, vuelve a iterar con el nuevo segmento

    # sali� del ciclo de manera no exitosa: el valor no fue encontrado
    return -1

# C�digo para probar la b�squeda binaria
def main():
    lista = input ("Dame una lista ordenada ([[]] para terminar): ")
    while lista != [[]]:
        x = input("�Valor buscado?: ")
        resultado = busqueda_binaria(lista, x)
        print "Resultado:", resultado
        lista = input ("Dame una lista ordenada ([[]] para terminar): ")

main()
