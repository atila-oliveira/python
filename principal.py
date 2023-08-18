import adivinhacao
import forca
print("\33[32m-="*20)
print("Bem vindo a Sala de Jogos!")
print("-="*20,"\33[m")

print('Digite 1 para jogar ADIVINHAÇÃO ou 2 para FORCA')
escolha = int(input("Qual jogo você deseja jogar?"))

if escolha == 1:
    adivinhacao.jogar()
elif escolha == 2:
    forca.jogar()
