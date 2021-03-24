#!/usr/bin/python

try:
    nota_1 = float(input("Insira a nota do primeiro bimestre:\n"))
    nota_2 = float(input("Insira a nota do segundo bimestre:\n"))
    nota_3 = float(input("Insira a nota do terceiro bimestre:\n"))
    nota_4 = float(input("Insira a nota do quarto bimestre:\n"))
    media = (nota_1+nota_2+nota_3+nota_4)/4
    print("A média de suas notas é: " + str(media))
    if media < 7.0:
        print("Você não foi aprovado. Estude mais.")
    else:
        print("Você foi aprovado. Parabéns!")
except:
    print("Insira suas notas em números.")