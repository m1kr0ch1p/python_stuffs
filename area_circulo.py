#!/usr/bin/python

from math import pi

try:
    r = float(input("Me dê o raio do círculo:\n"))
    a = pi * (r**2)
    print("A área do círculo é " + str(a) + ".")
except:
    print("Me dê valores quantitativos.")
# A = π. r2