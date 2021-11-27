from random import randint


print("************************************\n*** Avaliação Algoritmo e Lógica "
    "***\n************************************\n\nSelecione a Opção\n\n1. Percorrer Palavra\n2. Jogo da Quina\n\n9. "
    "Finalizar o programa\n\n")
opcao = int(input())



def Palavra():
  print ("UTILIZE LETRAS MAISCULAS")
  print ("")
  print ("")
  print ("")
  palavra = input("Digite uma palavra: ")

  alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  posAlfabeto = 0

  tamPalavra = len(palavra)

  x = 0
  y = 0

  for x in range(tamPalavra):
      for y in range(26):
          if (palavra[x] == alfabeto[y]):
              print("****************************************")
              print("Letra da palavra: " + str(palavra[x]) + " - " + "Posição: " + str(x+1))
              print("Posição no alfabeto: " + str(y+1))
          y = y + 1
      x = x + 1
  input("Digite algo para voltar ao menu")
  opcao = 0


def quina():

  x = 0
  y = 0

  valorA = []
  valorS = []
  AE = ["Errou","Errou","Errou","Errou","Errou","Errou"]

  for a in range(6):
    valorA.append(randint(1, 60))
    valorS.append(randint(1, 60))

  print("Numeros Apostados: ", valorA)
  print("Numeros Sorteados: ", valorS)

  for x in range(6):

    for y in range(6):
      if (valorA[x] == valorS[y]):
          AE.pop(x)
          AE.insert(x, "Acertou")
      elif(AE[x] != "Acertou" and valorA[x] == valorS[y]):
          AE.insert(x, "Errou")

      y = y + 1

    print("****************************************")
    print("Numero apostado: " + str(valorA[x]) + " " + AE[x])
    x = x + 1

  input("Digite algo para voltar ao menu")
  opcao = 0
  
  





  



if (opcao == 1): 
  Palavra()
elif (opcao == 2):
  quina()
elif (opcao == 9)
  print("Finalizando programa...")
  
