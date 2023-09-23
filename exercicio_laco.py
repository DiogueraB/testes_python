# Exercício de Laços de repetição

## Exercício 1 - Impressão de números 

# for numero in range(1,11):
#     print (numero)

# print("----------------------------------------------")
# maximo = int(input("De um número máximo para imprimir: "))
# for numero in range(1, maximo + 1):
#     print(numero)
# print("----------------------------------------------")

print("----------------------------------------------")
maximo = int(input("Qual número máximo: "))
ordem = input ("Qual a ordem que deseja imprimir (C/D): ")

if ordem == 'C':
    for numero in range(1, maximo + 1):
        print(numero)
elif ordem == 'D':
    for numero in range (maximo, 0 , -1):
        print(numero)
else:
    print ("Ordem Inválida")
    


