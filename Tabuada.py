# Exercício 2 - Tabuada
# - Escreva o código para imprimir a tabuada do 2 usando um laço for.
# - Refatore o código para solicitar ao usuário qual tabuada deve ser impressa.

# print ("-------- Tabuada do 2 --------")
# for numero in range (0 , 11):
#       print(f" 2 x {numero} = {numero * 2}")
# print ("------------------------------")


print ("------------- TABUADA -------------")
tabuada = int(input("Escolha uma tabuada para ser impressa: "))
for numero in range (0, 11):
    total = numero * tabuada
    print(f"{tabuada} x {numero} = {total}")
print("------------------------------------")

