#!/usr/bin/python

import random

# Variáveis do Placar
countrobo = 0
counthumano = 0

while True:
    opcoes = ["papel", "tesoura", "pedra"] # Opções: tesoura, pedra e papel
    jogador = input("O que você escolhe, pedra, papel, tesoura ou sair?\n").lower() # Opção do jogador
    robo = random.choice(opcoes) # Escolha aleatória do robô 

    if jogador in opcoes:
        print("Você escolheu " + jogador) # Output das oções do jogador
        print("Eu escolho " + robo) # Output das oções do robô
        if jogador == robo: # Empate
            print("Houve empate. \n :|")
        elif jogador == "papel": # PAPEL
            if robo == "tesoura":
                print("Eu venci! Minha tesoura cortou seu papel. \n :)")
                countrobo += 1
            else: # robo == "pedra"
                print("Você venceu! Seu papel cobriu minha pedra. \n :(")
                counthumano += 1
        elif jogador == "tesoura": # TESOURA
            if robo == "papel":
                print("Você venceu! Sua tesoura cortou meu papel. \n :(")
                counthumano += 1
            else: # robo == "pedra"
                print("Eu venci! Minha pedra quebrou sua tesoura. \n :)")
                countrobo += 1
        elif jogador == "pedra": # PEDRA
            if robo == "papel":
                print("Eu venci! Meu papel enrolou sua pedra. \n :)")
                countrobo += 1
            else: # robo == tesoura
                print("Você venceu! Sua pedra quebrou minha tesoura. \n :(")
                counthumano += 1
        print("---------PLACAR---------")
        print("EU: " + str(counthumano))
        print("Robô: " + str(countrobo))
        print("------------------------")
    elif jogador == "sair":
        break
    else:
        print("Escolha uma das opções: pedra, papel ou tesoura")
