# Programa que peça o nome,idade,peso e altura de uma pessoa

print ("------- IMC ------- \n")

nome = input ("Qual é o seu nome: ")
idade = int (input ("Idade: "))
peso = float (input ("Peso: "))
altura = float (input ("Altura: "))

imc = peso/(altura*altura)

print (f"Olá {nome}")
print (f"Sua idade é de {idade}")
print (f"Seu IMC é de {imc: .2f};")