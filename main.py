import sys  
import time
import os
import random
# serviços  
from calculadora import calcular  
  
# jogos  
from jokenpo import rps  
#version 1.1.0  
caixa = "                     " + "====================" +  "                     "  
line = "___________________________________________________________"
main = True
def info():
    print("\nTarcade™")  
                    
    print("\nVersão: 1.1.0")
    print("Creditos")  
    print("Propietário: @Berz4rdX (Bernardo)")  
    print("\nInspirações:")  
    print("Membros MastCode (discord)")  
    print("Membros do Mimo Max Comunnity (discord)") 
    print("nkevin75 (Kevin)")
    print("\nReferencias:")
    print("Linux")
    print("\nMódulos")
    print("sys, time, os e random")
    input("\nAperte Enter para sair: ")

while True:  
  try:
    frases = ["Tarcade v1.1... Em que dia chegaremos no major? :?","Mais um dia usando Python, e cada vez mais tiltado :/","Nossa, pra que fazet uma referencia desse jeito? >:(" ,"Alguém lê isso?","Oi! Tu tá aí?"]
    fala = random.choice(frases)
    print(caixa)
    print("                     " + "      Tarcade™" + "                     ")
    print(caixa)
    print(fala)
    print(line)
    print("\n     Serviços     ",end=" | ")  
    print("     Jogos      ",end=" | " )  
    print("     Avançado    | ")  
    print(line)  
              
    print("\n1 Calculadora     ",end=" | ")  
    print("""2 RPS - Pedra, |
                  Papel e Tesoura""",end="   |")
    print(" 0 Sair")
    print(line)
    print("\n                                    |  3 Info")
    print(line)
    print("\nQual serviço/jogo você quer usar?")
    choose = int(input("user_tarcade/ $ ")) 
              
    match choose:  
        case 1:  
          calcular()  
        case 2:  
           rps()  
        case 3:
            info()
        case 0:
           sys.exit()  
        case _:  
            print("\nEi! Escolha uma opção valida! CODE_ERR:invalid_choice")  
              
  except ValueError:  
            print("\nEi, não digite letras! Digite números! CODE_ERR:input_value_err")
            time.sleep(2)
            os.system("clear")
if __name__ == "__main__":
    main()