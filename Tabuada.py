# Exercício 2 - Tabuada
# - Escreva o código para imprimir a tabuada do 2 usando um laço for.
# - Refatore o código para solicitar ao usuário qual tabuada deve ser impressa.

# print ("-------- Tabuada do 2 --------")
# tabuada = 2
# for numero in range (0 , 11):
#       print(f"{tabuada} x {numero} = {tabuada*numero}")
# print ("------------------------------")


print ("------------- TABUADA -------------")
tabuada = int(input("Escolha uma tabuada para ser impressa: "))
for numero in range (0, 11):
    total = tabuada * numero
    print(f"{tabuada} x {numero} = {total}")
print("------------------------------------")

