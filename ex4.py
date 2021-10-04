#Faça um programa em Python para interpretar as expressões abaixo:

#somar 1 2
#dividir 4 2
#multiplicar 5 3
#subtrair 8 2

#Obs: O usuário poderá entrar somente com números com uma casa decimal. Não precisa validar.
 

#Exemplo de execução:

#==============================
#Digite a expressão: somar 2 2
#Resultado da Soma: 4

#==============================


import random

print("==============================")

while True :
  x = input("Digite a expressão: ")

  if x == "sair" :
    random.exit()

  exp = x.split()

  operacao = exp[0]
  num1 = float(exp[1])
  num2 = float (exp[2])

  if operacao == "somar" :
    res = num1 + num2
    print (f"Resultado da soma: {res}")
    print("==============================")

  if operacao == "dividir" :
    res = num1/num2
    print (f"Resultado da divisão: {res}")
    print("==============================")

  if operacao == "multiplicar" :
    res = num1*num2
    print (f"Resultado da multiplicação: {res}")
    print("==============================")

  if operacao == "subtrair" :
    res = num1-num2
    print(f"Resultado da subtração: {res}")
    print("==============================")

  








