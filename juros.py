# programa para calcular juros 

print ("--------------------------------------------")
print ("--------Calculadora de Juros Simples--------")
print ("--------------------------------------------")

valor = float(input("Qual o valor principal? "))
jurosanual = float(input("Qual é a taxa anual em porcentagem "))
tempo = float (input("Qual foi o período de Tempo em Anos ? "))

print ("--------------------------------------------")

montante = valor + (valor * (jurosanual /100) * tempo)

print (f"O montante é {montante}.")