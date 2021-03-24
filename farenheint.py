#!/usr/bin/python
try:
    f = float(input("Me dê a temperatura em Farenheit:\n"))
    c = 5 * ((f - 32)/9)
    print("A temperatura em Celsius é " + str(c) + "°.")
except:
    print("Me dê valores quantitativos")
# C = 5 * ((F-32) / 9).