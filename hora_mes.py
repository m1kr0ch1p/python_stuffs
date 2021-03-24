#!/usr/bin/python
try:
    vh = float(input("Quanto custa sua hora de trabalho em Real (digite apenas o valor em números)?\n"))
    hm = float(input("Quantas horas você trabalha no mês?\n"))
    t = vh * hm
    print("Você recebe R$ " + str(t) + " por mês.")
except:
    print("Preciso de valores quantitativos.")