#!/usr/bin/python

try:
    a = int(input("Me dê o primeiro número\n"))
    b = int(input("Me dê o segundo número\n"))
    c = a + b
    print("A soma dos número é igual a " + str(c))   
except:
    print("Já disse que trabalhamos apenas com números.")