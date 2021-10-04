#Faça um programa em Python que solicite para o usuário digitar 3 frases.Estas frases deverão ser gravadas em um array. Depois solicite para o usuário digitar um texto de busca. Faça um algoritmo para procurar o texto de busca nas frases digitadas.  E apresente para o usuário quais frases que contém o texto da busca. 

#Ex:Digite a frase 1: Python é uma linguagem multiplataforma
#Digite a frase 2: PHP é uma linguagem muito utilizada na WEB
#Digite a frase 3: PostgreSQL é um banco de dados OpenSource.

#Digite a Busca: linguagem

#Foram encontrados 2 resultados:
#1 - Python é uma linguagem multiplataforma
#2 - PHP é uma linguagem muito utilizada na WEB


texto = ""
frases = [ ]


for i in range(3):
  texto = input("Digite uma frase: ")
  frases.append(texto)


busca = input("Digite a busca: ")

for frase in frases:
  indice = frase.find(busca)
  if indice != -1:
    print (frase)