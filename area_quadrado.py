#!/usr/bin/python

try:
    a = float(input("Me dê a medida de um dos lados do quadrado:\n"))
    area = a**2
    areadouble = 2 * area
    print("A área do quadrado é " + str(area) + ".")
    print("O dobro da área do quadrado é " + str(areadouble) + ".")
except:
    print("Me dê valores quantitativos.")
# A = a2