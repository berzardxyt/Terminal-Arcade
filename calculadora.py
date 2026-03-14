import sys
def calcular():
    """Função principal da calculadora"""
    
    while True:
        try:
            num1 = float(input("\nEscolha o primeiro número: "))
            num2 = float(input("Escolha o segundo número: "))
            op = input("Escolha a operação (+,-,*,x,×,/,÷): ").strip().lower()

            if op not in ["+","-","*","×","x","/","÷"]:
                print("Operação inválida! Operações disponíveis: +,-,*,x,×,/,÷").strip().lower()
                continue

            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op in ["*","×","x"]:
                result = num1 * num2
            elif op in ["/","÷"]:
                if num2 == 0:
                    print("Não é possível dividir por zero!")
                    continue
                result = num1 / num2

            print(f"O resultado é:{result:.2f}")

            while True:
                stop = input("Quer fazer outra conta? (y/n) ")
                if stop == "y":
                    break
                elif stop == "n":
                    return
                else:
                    print("Escolha y ou n!")
        except ValueError:
            print("Para números com casas decimais, use ponto (.) Ex: 77.2")
        except Exception as e:
            print("Erro detectado inesperado:", e)