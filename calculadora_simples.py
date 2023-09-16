# Peça ao usuário para inserir dois números e uma operação (+, -, *, /).
# Realize a operação e exiba o resultado.

print ("------------Calculadora Simples------------")
print ()
num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))
operacao = input("Escolha uma operação (+, -, *, /) ")

print ()

resultado = ''

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if (num2 == 0):
        print("Não é possível dividir por 0")
    else:
        resultado = num1 / num2
else:
    print("Operação não reconhecida.")

if resultado != '':
    print (f"O resultado é: {resultado}")
    