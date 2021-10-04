#Faça um programa em Python que leia uma String de dados da seguinte forma:
#nome=Robson,email=robson.luz@fae.edu;nome=Joao,email=joao@email.com

#E apresente para o usuário da seguinte forma:

#Usuários cadastrados: 2
#==============================================
#Usuário 1
#Nome: Robson
#E-mail: robson.luz@fae.edu
#==============================================
#Usuário 2
#Nome: Joao
#E-mail: joao@email.com
#============================================== 

texto = "nome=Robson,email=robson.luz@fae.edu;nome=Joao,email=joao@email.com"

registros = texto.split (";")

print (f"Usuários cadastrados: {len(registros)}")

print ("=============")

for registro in registros:
  campos = registro.split(",")
  for campo in campos:
    valores = campo.split("=")
    print(f"{valores[0].capitalize()}: {valores[1]}")
  print("=============")














