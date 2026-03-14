import sys
#serviços
from calculadora import calcular
#jogos
from jokenpo import rps
caixa = "===================="
print("Terminal Arcade")
while True:
    try:
        print(caixa)
        print("Serviços")
        print("1 Calculadora(1.0)")
        print("\nJogos")
        print("2 Pedra, papel e tesoura")
        print("3 Tic tac toe com BOT (👨‍💻 Em desenvolvimento)")
        print("\nAvançado")
        print("0 Sair")
        print(caixa)
        choose = int(input("\nQual serviço/jogo você quer usar? "))
        print("\n©Bernardo - 2026, Todos os direitos reservardos")
        match choose:
            case 1:
                calcular()
                continue
            case 2:
                rps()
                continue
            case 3:
                print("Em desenvolvimento!")
                continue
            case 0:
                sys.exit()
            case _:
                print("\nEi! Escolha apenas 1 para calculadora, 2 para pedra papel e tesoura e 0 para sair! ")
    except ValueError:
        choose = print("\nEi, não digite letras! Digite numeros!")
