#!/usr/bin/python
try:
    metros = float(input("Quantos metros?\n"))
    centimetros = metros*100
    print(str(metros) + " metros são " + str(centimetros) + " centímetros.")
except:
    print("Me dê valores quantitativos.")