import random
import time
def rps():
 win_user = 0
 win_bot = 0
 try:
  print("Vamos jogar pedra, papel e tesoura? ")
  def think():
   """Função com efeito placebo que o bot realmente escolhe com time.sleep"""
   print("Bot pensando...")
   time.sleep(2)
   print(f"Escolha do bot:{bot_choice}") 
  while True:
   if win_bot >= 3:
    print("BOT ganhou!")
    break
   if win_user >= 3: 
    print("USER ganhou!")
    break
   bot_choice = random.choice([1,2,3])
   user_choice = int(input("\nEscolha pedra(1) ,papel(2) ou tesoura(3) "))
 
   if bot_choice == user_choice:
    think()
    print("Empate :|")
    print(f"Placar: BOT {win_bot} - USER {win_user}")
   elif (user_choice,bot_choice) in [(1,3), (2,1), (3,2)]:
    win_user += 1
    think()
    print("Vitoria! :D")
    print(f"Placar: BOT {win_bot} - USER {win_user}")
   elif (bot_choice,user_choice) in [(1,3), (2,1), (3,2)]:
    win_bot += 1
    think()
    print("Derrota... :(")
    print(f"Placar: BOT {win_bot} - USER {win_user}")
   else:
    print("\nValor invalido")
 except ValueError:
  print("\nNão escreva letras! Escreva 1 para papel, 2 para pedra, 3 para tesoura")