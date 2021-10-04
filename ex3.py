#Faça um programa em Python que solicite ao usuário que digite uma frase. Este programa deverá inverter a ordem das palavras e apresentá-las na tela.

#Exemplo:
#Frase digitada: Programa Feito em Python
#Saída na tela: Python em Feito Programa


frase = input ("Digite uma frase: ")


palavras = frase.split(" ")

palavras.reverse ()

for palavra in palavras:
  print (palavra)
