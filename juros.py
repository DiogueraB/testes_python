# programa para calcular juros 

print ("--------------------------------------------")
print ("--------Calculadora de Juros Simples--------")
print ("--------------------------------------------")

valor = float(input("Qual o valor principal? "))
jurosanual = float(input("Qual é o Juros Anual? "))
tempo = int (input("Qual foi o período de Tempo em Anos ? "))

juros = jurosanual/100

print ("--------------------------------------------")

montante = valor + (valor * juros * tempo)

print (f"O montante é {montante}.")